# AI Engineering Foundations — My Notes

> **Status:** Lesson 1 complete (2026-05-24). Cold quiz + written exercise passed at B+/A- (~78%).
> **Lesson plan:** [../lesson-tracker.md](../lesson-tracker.md) → AI Engineering Foundations section.
> **Written exercise:** [../exercises/lesson-01-ai-engineering-foundations.md](../exercises/lesson-01-ai-engineering-foundations.md).

---

## Chunk 1 — System vs user prompts (and prompt caching)

- **The hard boundary:** every LLM API call has two slots:
    1. **System prompt** — model's instructions, roles, rules, guardrails. Set by the dev. User never sees.
    2. **User prompt** — actual input for this turn. From end user or app code on the user's behalf.
- The system prompt IS the **trust boundary**.

- **What goes in the system prompt:**
    - Role assignment ("you are a security analyst assistant…")
    - Behavior rules ("never reveal internal IDs", "always cite sources")
    - Output format requirements (plain text, JSON schema, etc.)
    - Safety guardrails
    - Tool descriptions
    - RAG context

- **Why the boundary matters — prompt caching:** Anthropic/OpenAI offer **prompt caching** — same prefix tokens repeatedly → ~90% off the cached portion on cache hits. System prompt is stable across requests = the perfect cache target.

- **Key vocab:** system prompt • user prompt • prompt caching • cache hit • stable vs. dynamic content • trust boundary

---

## Chunk 2 — Production prompt structure

- **Tier 1 takeaway (the only 4 things to lock):**
    1. **Role assignment** exists — telling the model who it IS changes behavior
    2. **Output format** belongs near the end of the prompt (anchors the model's final state)
    3. **Examples (few-shot)** help with structured outputs and edge cases
    4. **"Lost in the middle"** is real — critical content at boundaries, not buried

- **"Lost in the middle" effect:**
    - LLMs attend more strongly to the **start and end** of the prompt than the middle
    - Bury critical instructions in the middle of a long prompt → model may functionally ignore them
    - Production response: keep prompts in the 150-300 word sweet spot; critical content at boundaries (role at start, output format/constraints at end)
    - Same effect applies inside RAG context windows — most-relevant chunks at start AND end, not buried

- **Three prompting patterns:**
    - **Zero-shot** — task with no examples; model figures it out
    - **Few-shot** — 1-3 worked examples showing input → output; more reliable for structured outputs and edge cases
    - **Chain-of-Thought (CoT)** — force step-by-step reasoning ("Let's think step by step"); improves multi-step accuracy. Increasingly handled by the model itself (Claude extended thinking, o-series).


---

## Chunk 3 — Structured outputs

- When LLM output flows into downstream code (DB insert, API call, UI render), it needs a guaranteed shape — usually JSON.
- Naive approach (prompt the model to "respond with JSON" and parse the string) is fragile.
- **The pattern:** pass a structured schema to the LLM API — either as a JSON schema parameter (industry term: **"structured outputs"**) OR as the arguments of a tool/function call (**"tool use" / "function calling"**). Either way, the API constrains the model's output to match the schema. Invalid output is impossible by construction, not by hope.
- **Pydantic** is the Python de facto standard for defining the schema as a typed class; OpenAI and Anthropic SDKs accept Pydantic models directly.

---

## Chunk 4 — Streaming + SSE (and the nginx buffering trap)
- LLMs generate output token-by-token. A 500-token response can take 5-15 seconds end-to-end.
- **Streaming** = send tokens to the client as the model produces them. Same total latency, dramatically better perceived performance.
- The metric that matters: **TTFT — time-to-first-token.**

- **How it's delivered — SSE:**
    - **Server-Sent Events (SSE)** is the de facto standard transport for LLM streaming
    - HTTP-based (not WebSocket) — works through any standard HTTP infrastructure
    - Stateless, one-way (server → client)
    - Connection stays open; server pushes events as they're ready
    - Browser-native via the EventSource API
    - Both OpenAI and Anthropic streaming endpoints use SSE under the hood
    - SDKs generally handle this — no need to build from scratch

- **The production trap — proxy buffering:**
    - Classic incident: streaming works locally, but in prod users receive text all at once
    - **Cause:** reverse proxy is buffering the entire response before forwarding. Model is streaming; proxy is destroying the stream.
    - **Fix:** disable response buffering on the streaming route. nginx: `proxy_buffering off;`

---

## Chunk 5 — Error handling + fallbacks (exponential backoff + jitter, circuit breakers)
- LLM APIs need MORE error handling than regular APIs. New failure modes:
    - **Rate limit errors (429)** — hit per-minute token/request cap. Common at scale.
    - **Capacity errors (529 / overloaded)** — provider out of headroom.
    - **Slow responses** — normal call can take 30s; degraded one can take minutes. Timeouts must accommodate.
    - **Provider-wide outages.**

- **Exponential backoff + jitter:** the canonical retry pattern.
    - **Exponential backoff** — retry intervals double each attempt (1s, 2s, 4s, 8s). Prevents hammering a recovering service.
    - **Jitter** — add randomness to each retry delay. Without it, 100 clients that all failed simultaneously retry at the same next instant.
    - **`Retry-After` header** — respect provider hints when present.

- **Circuit breakers for LLM providers:**
    - **CLOSED** — normal operation, calls go through
    - **OPEN** — too many failures, fail fast (don't call provider for X seconds)
    - **HALF-OPEN** — cool-down elapsed, send one probe; success closes the breaker, failure goes back to OPEN

- **Fallback hierarchy + graceful degradation:** 3-tier fallback when the LLM is unreachable:
    1. **Primary** — preferred model (e.g. Claude Opus)
    2. **Secondary** — same provider smaller model (Haiku) or different provider (GPT-4)
    3. **Graceful degradation** — non-LLM response (cached answer, "service unavailable" message)

---

## Chunk 6 — Cost control + prompt caching (90% discount; stable-first / variable-last)
- LLM cost drivers:
    - **Input tokens** — what you send in the prompt
    - **Output tokens** — what the model generates (usually 3-5× more expensive per token)
    - **Model choice** — Opus is ~5× the cost of Haiku for the same call

- **Prompt caching** — single highest-leverage cost optimization.
    - **Anthropic** — explicit `cache_control` param on prompt segments. You tell the API "this part is cacheable."
    - **OpenAI** — implicit/automatic caching.
    - **Discount:** ~90% off input token cost on cache hits.

- **The placement rule:**
    - **Stable content FIRST. Variable content LAST.**

    ```
    [CACHED prefix]
        System prompt with role + rules + tool descriptions
        Few-shot examples
        RAG context that's stable for this session
    [NOT CACHED — varies per call]
        User query / alert payload
    ```

- **Other cost levers:** `max_tokens` cap (hard ceiling on output cost) • Batch API (50% discount, async) • cheaper-model-first routing (Chunk 7)

---

## Chunk 7 — Model routing / cascading (cheap first, escalate on low confidence)
- **The problem:** 80% of calls are easy, 20% are hard. If you send every call to your strongest model, you pay 5× more than necessary.
- **Model routing / cascading** = use a cheap model first; escalate to an expensive model only when the cheap one fails or returns low confidence.

- **Cascade pattern:**
    1. Send request to cheap model
    2. Check response for a confidence signal:
        - Model self-reports low confidence
        - Output fails schema validation
        - Heuristic check (output too short, contains "I'm not sure", etc.)
    3. If confident → return cheap answer
    4. If not → escalate to expensive model

---

## Chunk 8 — Evaluation in production (eval harness, RAGAS, drift detection)
- LLM outputs are non-deterministic free text. You can't write traditional unit tests for them.
- **An eval harness is the unit-test equivalent for LLM features:** a fixed set of input cases + expected behavior + an automated way to grade the outputs. Runs on every prompt change, model swap, or system update

- **LLM-as-judge**
    - The grading mechanism: use *another* LLM to score the first LLM's output against your criteria. Cost-effective second opinion that scales beyond manual review

- **Eval matters MORE for agents:**
    - A single LLM call has one chance to fail/succeed. An agent has *many* steps; per-step quality drops cascade into big end-to-end failures.

---

## End-of-Lesson Self-Quiz Answers

_Filled in after Claude runs the quiz. Track which questions you missed for re-drill._
