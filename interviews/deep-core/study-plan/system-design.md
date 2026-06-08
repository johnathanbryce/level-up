# System Design (Area 3 — concepts cram + AI framing)

> **Mon (today):** learn/refresh the core concepts in chunks + quizzes (active recall). **Tue:** grind interview-style "design X" questions at home.
> Bar = know the critical patterns at a high level + speak to trade-offs. No full URL-shortener grinds today.

## How to approach a "design X" question

1. **Clarify requirements** — what, for whom, what scale?
2. **Estimate scale** — rough numbers (users, RPS, data size)
3. **High-level components** — boxes + arrows
4. **Data model** — what's stored, how
5. **Deep-dive the bottleneck** — go deep where it matters
6. **Trade-offs** — name what you give up and why

> **Seniority tell:** clarify + estimate BEFORE naming any tech. Juniors say "I'd use Redis + Kafka." Seniors ask "how many users, how fresh must the data be?" first.

---

## Core concepts cram (high level — know cold)

### 1. Scaling: vertical vs horizontal
- **Vertical** = bigger machine. Simple, but a ceiling + single point of failure.
- **Horizontal** = more machines. Scales out; needs a load balancer + stateless servers.
- **Statelessness is the enabler:** keep no session state on the app server (push it to Redis/DB) → any server handles any request → horizontal scaling works.

### 2. Load balancing
- Distributes traffic across servers (round-robin, least-connections, weighted).
- Health checks route around dead instances.
- Session stickiness only if you must keep state on a server — avoid; prefer stateless.

### 3. Caching
- **Cache-aside:** check cache → miss → load from DB → populate cache (with **TTL**).
- **When NOT to cache:** highly personalized, rarely-read, staleness-sensitive data.
- **Invalidation is the hard part** (stale data is the classic bug).
- **AI angle:** cache LLM responses + embeddings (cuts cost AND latency); **semantic cache** for near-duplicate queries.

### 4. Async + queues (background jobs)
- Long/slow work doesn't belong in request-response → **enqueue a job, return a job ID, poll or stream status**.
- Decouples producer from consumer; smooths traffic spikes; enables retries.
- **AI / Deep Core angle:** a 3D model build takes minutes → background job + status polling. Same for batch evals.

### 5. Idempotency
- Same operation repeated = same result, no duplicate side effects.
- **Idempotency-Key** on writes so a retry doesn't double-execute / double-charge.
- Essential once you have retries + queues (at-least-once delivery means dupes happen).

### 6. Rate limiting
- **Token bucket** (capacity + refill rate — state BOTH).
- Protects expensive endpoints + prevents abuse.
- **AI angle:** anchor the limit to **$/hr-per-abusive-user** for LLM/compute endpoints.

### 7. Database + data scaling
- **Postgres as default.** Index what you filter/join on; **EXPLAIN ANALYZE** for slow queries.
- **Read replicas** (scale reads) BEFORE **sharding** (scale writes — complex, last resort).
- **pgvector** for vectors when already on Postgres; dedicated vector DB only at a named scale/throughput.
- Don't over-engineer at 2-person scale.

### 8. Replication & sharding
- **Replication** = copies of data → read scaling + failover. Usually async → **replica lag** (eventual consistency).
- **Sharding** = split data across nodes by a key → write scaling. Adds complexity (cross-shard queries, rebalancing).

### 9. Consistency (CAP)
- **CAP:** under a network partition, you choose **Consistency** or **Availability**.
- **Strong** = always latest (costs latency/availability). **Eventual** = converges over time (fast, may read stale).
- Most web systems lean AP + eventual; money/inventory wants strong.

### 10. Monolith vs microservices
- **Start with a (modular) monolith** — especially at 2-person scale.
- Microservices solve org/scale problems you don't have yet; premature split = distributed pain (network calls, debugging, ops).
- **Opinion-ready:** "monolith first, split when you can name the bottleneck."

### 11. Observability + reliability
- **Three pillars:** logs / metrics / traces.
- **LLM-specific:** cost-per-call, eval/faithfulness score, hallucination rate, token usage, drift.
- **Circuit breaker:** stop calling a failing/slow dependency. Slow dep is worse than down (holds threads → pool exhaustion → cascading failure). States: CLOSED → OPEN → HALF-OPEN.
- **Retries with backoff + jitter**; **graceful degradation** (serve a reduced experience instead of failing hard).

---

## Deep Core framing (map concepts → their product) — for Tue mock

- Long model build → async job + status polling (concept 4)
- Expensive LLM/geostat calls → caching + rate limiting (3, 6)
- Heterogeneous data sources → clean ingestion + MCP servers (Area 1)
- Trust/correctness → deterministic services + HITL gate (Area 1)
- Small team → modular monolith, don't over-engineer (concept 10)

## Supabase / Cesium — "if it comes up" only (NOT studied)

- **Supabase** = managed Postgres + RLS → maps to JWT/tenant isolation. Q: "RLS or app-layer isolation?"
- **Cesium** = web 3D engine; hard part = perf w/ large meshes. Q: "LOD / tiling / streaming for large meshes?"
