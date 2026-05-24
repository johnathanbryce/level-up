# AI Engineering Foundations — My Notes

> **Status:** Not yet taught.
> **Lesson plan:** [../lesson-tracker.md](../lesson-tracker.md) → AI Engineering Foundations section.
> Take notes below as Claude teaches each chunk. Use whatever structure feels natural — these chunk headers are just an anchor.

---

## Chunk 1 — System vs user prompts (and prompt caching)

- **The Hard Boundary:**
  - When you call an LLM API, the request has two distinct lots:
    1. **System prompt** - the model's instructions, roles, rules, guardrails. Set by the dev. The user never sees these.
    2. **User prompt** - the actual input for this turn. From the end user or from app code on the users behalf
  - The system prompt is the **trust boundary** layer

- **What Goes Where**
  - **System prompt:**
    - Role assignment ("you are a security analyst assistant...")
    - Behavior rules ("never reveal internal IDs", "always cite sources")
    - Output format requirements ("Output all answers as plain text", "Output all answers as JSON in this structure...")
    - Safety guardrails
    - Tool descriptions
    - RAG context

- **Why the boundary matters: prompt caching**
    - Anthropic/OpenAI offer **prompt caching** - if you send the same prefix tokens repeatedly, you pay 90% less for the cached portion on cache hits
        - System prompt is stable across requests, its the perfect cache target

-- **Key vocab:**
    - system prompt, user prompt, prompt caching, cache hit (the cached portion of input gets discount), stable vs. dynamic content (determines what is cacheable)

---

## Chunk 2 — Production prompt structure

- **Tier 1 takeaway (the only 4 things to lock):**
    1. **Role assignment** exists — telling the model who it IS changes behavior
    2. **Output format** belongs near the end of the prompt (anchors the model's final state)
    3. **Examples (few-shot)** help with structured outputs and edge cases
    4. **"Lost in the middle"** is real — critical content at boundaries, not buried

- **Reference: common prompt components** (don't memorize as a list — recognize them in a prompt)
    - Role, Task, Context, Instructions, Output Format, Constraints, Examples

- **"Lost in the middle" effect**
    - LLMs attend more strongly to the **start and end** of the prompt than the middle
    - Bury critical instructions in the middle of a long prompt → model may functionally ignore them
    - Production response: keep prompts in the 150-300 word sweet spot; put critical content at boundaries (role at start, output format/constraints at end)
    - Same effect applies inside RAG context windows — most-relevant chunks at start AND end, not buried

- **Three prompting patterns to know**
    - **Zero-shot** — task with no examples; model figures it out
    - **Few-shot** — 1-3 worked examples showing input → output; model pattern-matches; more reliable for structured outputs and edge cases
    - **Chain-of-Thought (CoT)** — force step-by-step reasoning before the final answer ("Let's think step by step"); improves multi-step accuracy at the cost of more output tokens. Increasingly handled by the model itself (Claude extended thinking, o-series) rather than prompt-engineered.


---

## Chunk 3 — Structured outputs

- When LLM output flows into downstream code (DB insert, API call, UI render), it needs a guaranteed shape — usually JSON.
- Naive approach (prompt the model to "respond with JSON" and parse the string) is fragile.
- **The pattern:** pass a structured schema to the LLM API — either as a JSON schema parameter (industry term: **"structured outputs"**) OR as the arguments of a tool/function call (**"tool use" / "function calling"**). Either way, the API constrains the model's output to match the schema. Invalid output is impossible by construction, not by hope.
- **Pydantic** is the Python de facto standard for defining the schema as a typed class; OpenAI and Anthropic SDKs accept Pydantic models directly.

---

## Chunk 4 — Streaming + SSE (and the nginx buffering trap)
- LLMs generate output token-by-token. A 500-token res can take 5-15 seconds end-to-end
- **Streaming** = sending tokens to the client as soon as the model produces them. User sees text appear in real time. Same total latency, dramatically better perceived performance
- The metric that matters: **TTFT - time-to-first-token** 

- **How it's delivered: SSE**
    - **Server-Sent Events (SSE)** is the de facto standard transport for LLM streaming
        - HTTP-based (not WebSocket) - works through any standard HTTP infrastructure
        - Stateless, one-way (server -> client)
        - The connection stays open; server pushes events as they're ready
        - Browser-native via the EventSource API
        - Both OpenAI and Anthropic streaming endpoints use SSE under the hood 
    - SDKs generally handle this, so no need to build from scratch 

- **The production trap: proxy buffering**
    - Classic incident: streaming works perfectly in local dev, but in prod users receive the text all at once - streaming is broken
    - **Cause:** the reverse proxy is buffering the entire response before forwarding it. The model is streaming ,the proxy is destroying the stream
        - **Fix:** disable response buffering on the streaming route
        - nginx: *proxy_buffering off;*

---

## Chunk 5 — Error handling + fallbacks (exponential backoff + jitter, circuit breakers)
- LLM APIs need more error handling than regular APIs
- LLM APIs add new failure models:
    - **Rate limit errors (429)** - you hit the per-minute token/request cap. Common at scale
    - **Capacity errors (529/overloaded)** 
    - **Slow responses** - a "normal" call can take 30s. A degraded one can take minutes. Timeouts must accommodate this
    - **Provider-wide outages**
- Prod LLM apps need retry and fallback

- **Exponential backoff + jitter**
    - The canonical retry pattern
        - **Exponential backoff** - retry intervals double each attempt (1s, 2s, 4s, 8s). Prevents hammering a recovering service
        - **Jitter** - add randomness to each retry delay. Without jitter, 100 clients that all failed simultaneously will retry at the same next instant
        - ***Retry-After* header** 

- **Circuit breakers for LLM providers**
    - **CLOSED** - normal operation, calls go through
    - **OPEN** - too many failures, fail fast (don't call provider for X seconds)
    - **HALF-OPEN** - cool-down elapsed, send on probe; success closes the breaker, failure goes back to OPEN

- **Fallback hierarchy + graceful degradation**
    - When the LLM is unreachable, what does your feature do? 3-tier fallback:
        1. **Primary** - preferred model (e.g. Claude Opus)
        2. **Secondary** - same provider, smaller model (e.g. Haiku) or a different provider (GPT-4)
        3. **Graceful degradation** - feature returns a non-LLM response (e.g. cached prev answer or a "service unavailable" message)

---

## Chunk 6 — Cost control + prompt caching (90% discount; stable-first / variable-last)
- Every LLM has variable cost driven by:
    - **Input tokens** - what you send in the prompt
    - **Output tokens** - what the model generates (usually 3-5x more expensive per token)
    - **Model choice** - Opus is ~5x the cost of Haiku for the same call

- **Prompt caching**
    - The single highest-leverage cost optimization which most major providers offer
        - **Anthropic** - explicit *cache_control* param on the prompt segments. You tell the API "this part is cacheable"
        - **OpenAI** - implicit/automatic caching
    - Discount: ~90% off input token cost on cache hits

- **The placement rule**
    - **Stable content FIRST. Variable content LAST**

        [CACHED prefix]
            System prompt with role + rules + tool descriptions
            Few-shot examples
            RAG context that's stable for this session
        [NOT CACHED — varies per call]
            User query / alert payload

- **Other cost levers**
    - **max_tokens cap**
    - **Batch API**
    - **Cheaper-model-first routing**

---

## Chunk 7 — Model routing / cascading (cheap first, escalate on low confidence)
- The problem: 80% of your calls are easy, 20% are hard (complex reasoning, multi-step analysis). If you send every call to your strongest model, you pay 5x more than necessary
- **Model routing / cascading** = use a cheap model first; escalate to an expensive model only when the cheap one fails or returns low confidence

- **Cascade pattern**
    1. Send request to cheap model
    2. Check the response for a confidence signal:
        - Model self-reports low confidence
        - Output fails schema validation
        - Heuristic check (output too short or contains "I'm not sure", etc)
    3. If confident -> return cheap answer
    4. If not -> escalate to expensive model

---

## Chunk 8 — Evaluation in production (eval harness, RAGAS, drift detection)
- LLM outputs are non-deterministic free text. You can't write traditional unit tests for them.
- **An eval harness is the unit-test equivalent for LLM features:** a fixed set of input cases + expected behavior + an automated way to grade the outputs. Runs on every prompt change, model swap, or system update

- **LLM-as-judge**
    - The grading mechanism: use *another* LLM to score the first LLM's output against your criteria. Cost-effective second opinion that scales beyond manual review

- **Eval matters MORE for agents**
    - A single LLM call has one chance to fail/succeed. An agent has *many* steps, and per-step quality drops 
    - this is the single most important reason to invest in eval - without it, small upstream regressions silently cascase into big end-to-end failures

---

## End-of-Lesson Self-Quiz Answers

_Filled in after Claude runs the quiz. Track which questions you missed for re-drill._
