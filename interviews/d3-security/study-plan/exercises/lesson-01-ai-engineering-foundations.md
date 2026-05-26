# Lesson 1 — End-of-Lesson Written Exercise

> **Lesson:** AI Engineering Foundations
> **Format:** D3-style short structured answer (bullets, ~6-8 total)
> **Time target:** under 10 minutes, closed notes
> **Date attempted:** 2026-05-24

---

## Prompt

You're shipping a Morpheus-style alert triage feature (LLM ingests security alerts, outputs structured triage decisions). Production users report:

1. **Average response latency feels slow** — 3-4 seconds before any text appears in the analyst UI
2. **The downstream pipeline** (which consumes the triage output as JSON) crashes intermittently on parse errors
3. **Last month's bill** from your LLM provider was 2.5x your budget

Diagnose each symptom and write a 1-2 bullet fix for each. **3 problems, 3 fixes, ~6 bullets total.**

---

## My Answer


### Problem 1 — Slow first-token latency
- Let's first ensure that our reverse proxy nginx file has buffering turned off. This would prevent Streaming text and perceived latency reduction
- We would need to diagnose TTFT and why this latency is occurring. The fix might be as simple as adjusting our system prompt to ensure the model understands it's role, or alter/edit any existing guardrails or few-shot prompts that could be outdated or lacking in proper structure causing the model to have to process extra hard unnecessarily
- We also need to determine what LLM models we are using and why. Do we have multi-model handling in effect? 


### Problem 2 — JSON parse failures downstream
- In pre-production, adding in an eval agent or system to evaluate the responses from the LLM. Especially if they are expected to produce structured JSON. This fix could be multi-faceted: 1. an additional API eval call to another LLM to inspect the output (only in dev) 2. if we are in fact expecting structured output, an internal function that takes in the output of the API call and compares it to the structure of the expected JSON. If it passes, we return True and the function continues to the next call with the proper output. If False, return and this will trigger another API call to a more expensive model using the original users input for a better response


### Problem 3 — Bill 2.5x over budget
- The first and more important check: are we caching the system prompt. If not, this must be handled immediately as this is an immediate 90% reduction in the system prompt hit
- Are we using multi-model calls? Unless our API requires complicated processing there is no need to automatically use the most expensive model for all LLM API calls. This will entirely depend on the API in question, but at the very least ensure the first API call uses the cheapest model and then have internal validation against the output (could be structured JSON text, or looking for keywords in the text response of the model like "I am not sure", or by examining the models confidence_level) and, only if necessary, route to the more expensive model

---

## Grading (filled in by Claude)

_Rubric pass-bar: 75%. Below 70% = re-drill weakest chunks before Lesson 2._

- **Problem 1 — Slow first-token latency: B/B+ (~80%).** Led correctly with nginx proxy buffering — that's the canonical fix for this symptom. TTFT named as the diagnostic metric. Other two bullets (system prompt optimization, multi-model choice) are weaker secondary considerations — they're more "next questions to ask" than focused fixes. The system-prompt-length angle is real but marginal; smaller/faster model is the better latency lever and you didn't quite name it explicitly. Tighter answer would have been: (1) verify streaming is enabled, (2) check `proxy_buffering off` in nginx, (3) if still slow consider a smaller/faster model.
- **Problem 2 — JSON parse failures: C+/B- (~70%).** Missed the canonical architectural fix entirely. The answer to "downstream pipeline crashes on JSON parse" is **use structured outputs / function calling with a Pydantic schema** — this was Chunk 3. When the API constrains output at the schema level, parse failures become impossible by construction, not by validation-and-retry. What you proposed (eval agent + structure check + escalation) is a workable retry-and-validate system, but it solves the problem at the wrong layer — you're papering over a structural fix with operational complexity. The right answer fixes it upstream so the eval/retry isn't needed.
- **Problem 3 — Bill 2.5x over budget: A-/B+ (~85%).** Strong. Led with prompt caching at 90% discount — correct priority and impact framing. Multi-model routing covered with multiple concrete escalation signals (structured validation, uncertainty keywords, confidence). Missing: `max_tokens` cap (you named it in cold quiz unprompted — would've completed the answer here) and batch API for non-realtime jobs. Output token premium (3-5x input) also worth dropping in for senior framing.
- **Overall: B+/A- (~78%). PASS** (above 75% bar). Best work on cost control; solid streaming fix; meaningful miss on structured outputs as the architectural fix to JSON failures.

---

## Re-drill items surfaced

_Concepts/vocab that need reinforcement. Carry forward into mock test prep._

- **Structured outputs as a FIX, not just a concept.** You own the concept (Chunk 3 + cold quiz). But on the applied scenario you reached for eval/retry instead of structured outputs. This is the "knows-the-rule, doesn't-apply-under-pressure" pattern. Drill: any time a problem statement mentions "JSON parse failures" or "downstream consumes structured data" → first answer is **structured outputs / function calling with a Pydantic schema**.
- **System-prompt placement reasoning is missing the caching angle under cold recall.** Flagged for the 2nd time today (cold quiz Q1, opening chunk-1 check question). When the system-vs-user-prompt question appears in any form, force both reasons: (a) trust boundary, (b) prompt caching benefit.
- **`max_tokens` cap.** Named in cold quiz, missed in exercise. Add to the cost-control checklist; should be reflex when "LLM bill is X% over budget" appears.
