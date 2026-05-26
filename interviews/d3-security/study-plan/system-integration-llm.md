# System Integration (LLM) — My Notes

> **Status:** Not yet taught.
> **Lesson plan:** [../lesson-tracker.md](../lesson-tracker.md) → System Integration LLM section.
> ~60% reuses existing system design notes — anchor in `02-system-design/` rather than re-teach.

---

## Chunk 1 — LLM reference architecture (UI → API gateway → backend → LLM → tools → data → observability)

### The 7-layer reference architecture

```
[1] Client            (web / mobile / CLI)
       ↓
[2] API Gateway       (auth, rate limit, routing, $/user cap)
       ↓
[3] Backend           (business logic, orchestration)
       ↓
[4] LLM Service       (assembles prompt + RAG context + tool definitions)
       ↓
[5] LLM Provider      (Anthropic / OpenAI / Gemini)  ←→  [6] Tools (functions LLM calls)
       ↓                                                        ↓
   [streamed SSE response]                              [7] Data layer
                                                       (vector store, Postgres, cache, external APIs)

   [Observability sidechannel] ← async logs/metrics/traces from every layer
```

### Per layer — what it does + what's LLM-specific

1. **Client** — same as any web/mobile app. **LLM-specific:** must handle streaming responses (EventSource for SSE) and show partial tokens as they arrive.
2. **API Gateway** — auth + rate limit + routing. **LLM-specific:** rate limits as `$/hour-per-user` (not just request count), token-bucket cost protection.
3. **Backend** — orchestration layer. Decides which LLM service to call, threads user context. Stateless, horizontally scalable.
4. **LLM Service** — the part unique to AI apps. Assembles the full prompt: system prompt + RAG context + tool definitions + user message. Handles streaming, structured outputs, function calling, retries with backoff. *This is where most of the AI engineering complexity lives.*
5. **LLM Provider** — external API (Anthropic, OpenAI, Gemini). Treated as an unreliable external dependency — circuit breaker, fallback to secondary model, prompt caching.
6. **Tools** — functions the LLM can call (DB queries, third-party APIs, internal services). Each tool is itself a small service with its own auth/scopes. MCP standardizes this layer at scale.
7. **Data layer** — vector store (RAG), traditional DB (state), cache (Redis for prompt + response cache).

### Observability sidechannel (cross-cutting)

- **Async, never blocks** the request path. Logs + traces + metrics fire on a separate pipeline.
- Captures from every layer above — but adds 4 LLM-specific metrics (see Chunk 3).

### Killer interview line

*"Production LLM app = client → API gateway → backend → LLM service → LLM provider, with tools and data layer hanging off the LLM service, and an async observability sidechannel. Most of the AI engineering complexity lives in the LLM service layer — prompt assembly, RAG context, tool definitions, streaming, structured outputs, retries. Everything else is standard distributed system design."*

---

## Chunk 2 — Where existing system design concepts apply (rate limiting, idempotency, observability, queues)

1. **Rate limiting at API gateway** - same pattern as any API. LLM apps add: token-bucket per user, $/hour-per-user caps (cost protection, not just abuse protection)
2. **Idempotency for write operations from agents** - agent retries on failure -> without idempotency, you double-charge / double-execute. Use *Idempotency-Key* header with same value across retries; server caches first response
3. **Circuit breaker for LLM providers** - Anthropic/OpenAI go down. Pattern from sys design chunk: CLOSED -> OPEN -> HALF-OPEN with cool-down. Fail-fast to fallback
   
---

## Chunk 3 — LLM-specific observability (cost per call, faithfulness, drift, eval harness)
- Beyond standard logs/metrics, LLM apps need 4 metrics no other system has:
    1. **Per-call cost** - track API costs per-user for insights on super users
    2. **Faithfulness / eval score** - RAGAS-style. Is the LLM answer grounded in retrieved context, or hallucinated?
    3. **Drift detection** - eval scores tracked over time. Did this week's deploy or model update silently regress quality
    4. **Hallucination rate** - % of outputs flagged by output filter / LLM-as-judge ungrounded

---

## End-of-Lesson Self-Quiz Answers

_Filled in after Claude runs the quiz._
