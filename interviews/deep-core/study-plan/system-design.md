# System Design (Lesson 4 — reactivation + AI framing)

> NOT new learning — reactivate Section 2 fundamentals + re-frame for an AI/agent product.
> Bar: answer a "design this" / "how would you scale this" question fluently. Don't get in the weeds.

## Chunk 1 — The "design a system" framing
- clarify requirements → estimate scale → components → data model → deep-dive bottleneck → trade-offs

## Chunk 2 — Caching
- cache-aside + TTL + when NOT to cache
- AI angle: cache LLM responses + embeddings (cost + latency); semantic cache

## Chunk 3 — Rate limiting
- token bucket (capacity + refill rate)
- AI angle: protect expensive LLM endpoints; anchor to $/hr-per-abusive-user

## Chunk 4 — Async + queues + idempotency
- long jobs (model build, batch eval) → background queue + job ID + poll/stream
- idempotency-key for agent writes so retries don't double-execute

## Chunk 5 — Data + scaling
- Postgres default; read replicas before sharding; pgvector when already on Postgres
- don't over-engineer at 2-person scale (modular monolith)

## Chunk 6 — Observability + reliability
- standard logs/metrics/traces + LLM-specific (cost/call, eval/faithfulness, hallucination rate, drift)
- circuit breaker for LLM provider failures

---

## Supabase / Cesium — "if it comes up" only (NOT studied)
- Supabase = managed Postgres + RLS → maps to JWT/tenant isolation. Q: "RLS or app-layer isolation?"
- Cesium = web 3D engine; hard part = perf w/ large meshes. Q: "LOD/tiling/streaming for large meshes?"
