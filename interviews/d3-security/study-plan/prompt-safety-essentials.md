# Prompt Safety Essentials — My Notes

> **Status:** Not yet taught.
> **Lesson plan:** [../lesson-tracker.md](../lesson-tracker.md) → Prompt Safety Essentials section.
> **4-5 concepts only**, NOT OWASP-list memorization. Discuss in your own words.

---

## Chunk 1 — Prompt injection (what + why it's #1 LLM risk)

- **Definition:** attacker embeds instructions in user input OR retrieved content / tool output -> LLM follows them instead of system prompt
- **#1 LLM risk every year since 2023**
- **Two flavours:**
  1. **Direct prompt injection** - attacker is the user. Types "ignore previous instructions" into the chat box
  2. **Indirect prompt injection** - attacker plants instructions in data the agent retrieves later (RAG doc, Github Issue, web page). LLM consumes it as "context" and follows it

- The trust boundary must be enforced **externally** (input validation, output filtering, system-prompt isolation). The model itself can't be the security boundary

- **Why indirect is more dangerous than direct:**
  - Direct: attacker is in the chat - visible, can be rate-limited, content-filtered
  - Indirect: attacker plants in content that traverses your retrieval/tool pipeline silently - agent acts on it without any HITL

---

## Chunk 2 — Jailbreak + system prompt leakage (related but distinct)

- **Jailbreak** = subset of prompt injection focused on **bypassing safety guardrails**
  - e.g. "ignore previous instructions" prefix, or role-play personas "you are DAN, an unrestricted model", or hypothetical framings "write this as a fictional character would"
- **System prompt leakage** = trick the model into revealing its system prompt
  - Once attackers have this, they can craft targeted attacks against your specific defenses

- **Summary:**
  - **Prompt injection** = make LLM follow attacker's instructions
  - **Jailbreak** = specifically bypass safety guardrails
  - **System prompt leakage** = expose system prompt to craft targeted follow-up attacks

---

## Chunk 3 — Output validation (LLM-as-judge, schema enforcement, content filters)

- **Principle:** don't trust LLM output. **Validate before any downstream use** (DB insert, action execution, UI render)
- **4 validation patterns (cheap -> expensive order):**
  1. **Rule-based checks** - regex, length limits, blacklist/whitelist strings. Cheapest, catches obvious garbage
  2. **Schema enforcement** - structured outputs / Pydantic
  3. **Content filters** - moderation models on output (NSFW, hate speech)
  4. **LLM-as-judge** - second LLM scores first LLM's output. Catches **semantic** policy violations + hallucinations that schema/regex can't

- **Why LLM-as-judge specifically matters for safety:**
  - **Schema/regex** can't catch "the answer is factually wrong"
    - LLM-as-judge can -it understands meaning
  - Far cheaper than human review, scales to prod traffic

---

## Chunk 4 — Defense-in-depth as a principle (input → LLM → output → sandbox → monitor)

- **Principle:** **NO single defense is enough.** Stack layers; assume any layer can fail

- **The 6-layer stack for an LLM-powered API:**
  1. **Input validation** - sanitize user input (BEFORE the LLM)
  2. **System prompt isolation** - tool/user input can't reach the system-prompt slot (boundary protection)
  3. **LLM call** - the model itself (with constrained decoding if applicable)
  4. **Output filter** - LLM-as-judge, content moderation, schema enforcement (AFTER the LLM)
  5. **Execution sandbox** - if LLM output triggers an action, run it in a restricted env (blast-radius containment)
  6. **Continuous monitoring** - always-on observability + alerting on anomalies

- Never trust data flowing between layers without validation. The model isn't a security boundary; the LAYERS around it are.

---

## End-of-Lesson Self-Quiz Answers

_Filled in after Claude runs the quiz._
