# System Design (Area 3 — concepts refresh)

## How to approach a "design X" question
1. **Clarify requirements** - what are we building, for whom, what must it do?
2. **Estimate scale** - rough numbers: users, requests/sec, data size. Grounds every later choice
3. **High-level components** - the boxes and arrows
4. **Data model** - what is stored and how
5. **Deep-dive the bottleneck** - go deep only where it matters
6. **Trade-offs** - name what you're giving up and why

## 1. Scaling: vertical vs horizontal (+ statelessness)
- **Vertical scaling** = making the machine bigger. Ceiling to this and is a single point of failure
- **Horizontal scaling** = add more machines. Scales but needs a **load balancer** in front and **stateless app servers** to work
- **Statelessness is the enabler:** if an app server stores no per-user state (no in-memory sessions), then *any* server can handle *any* request. 
    - Push state to a shared store (Redis/DB). 
    - Now you can add/remove servers freely and the LB can route anywhere
        - Flip side: if a server holds session state in memory, you're forced into **sticky sessions** (a user pinned to one server). If that server dies, their state is gone

## 2. Load balancing
- A component in front of your servers that **distributes incoming traffic** across them, so no single server gets overwhelmed
- **Common algos:**
    - **Round-robin** - rotate through servers evenly. Default, simple.
    - **Least-connections** - send to the server with the fewest active requests.
    - **Weighted** - bigger servers get more traffic
- **Health checks** - the LB pings each server. If one stops responding, it **rotates around the dead instance automatically**. This is where horizontal scaling gets its resilience
- **Sticky sessions** - pin a user to one server. **Avoid this if possible** - it breaks even load distribution and loses state if that server dies. Statelessness is what lets you skip it.
- **Bonus framing:** an LB is one job of a **reverse proxy** (which also does TLS termination, routing, sometimes caching). Nginx / a cloud LB are common

- **Deep Core:** the app tier sits behind a standard LB. For the compute tier, the equivalent of "load balancing" is a **job queue** - workers pull work when free, which naturally balances load

## 3. Caching
- Serve hot data from fast memory instead of re-hitting the DB / recomputing / re-calling an API
- Cuts **latency** and **load/cost**
- **Cache-aside (the default pattern)**: app checks cache 
    - hit = return it from cache
    - miss = load from DB, **write it to the cache with a TTL** and return it
- **TTL (time to live)**: expiry on each entry. Short TTL = fresher but more misses; long TTL = cheaper but staler
- **Invalidation is the hard part** - stale data is the classic bug
    - Strategies:
      - TTL (lazy) or **invalidate-on-write** (delete/refresh the cache entry when the underlying data changes)
- When NOT to cache: highly personalized data, rarely-read data, and staleness-sensitive data (where serving old data is worse than serving slow)
- **AI angle:** cache **LLM responses** and **embedings**. **Semantic cache** = if a new query is semantically near a past one, serve the cached answer

- **Deep Core relevance:** cache expensive **geostat results** and **LLM calls** keyed by inputs. If the same dataset + params come through, return the prior result

## 4. Async + queues (background jobs)
- Some work is too slow for request-response. If a request takes 2 mins, you can't hold the HTTP connection open
- **The pattern:** **queue a job, return immediately with a job ID, process in the background, let the client poll or stream for status/result**
    - Request comes in -> drop a message on a **queue** -> respond 202 accepted + job_id
    - A pool of **workers** pulls jobs off the queue, does the slow work, writes the result somewhere (DB / object storage)
    - Client checks GET /jobs/{id} (polling) or gets pushed updates (WebSockets/SSE)
- **Why a queue specifically:**
    - **Decouples** producer (web tier) from consumer (workers)
    - **Smooths spikes** - a burst of 100 requests doesn't crash you; they line up an drain at worker capacity
    - **Enables retries** - if a worker dies mid-job, the message goes back on the queue 
- **The catch:** queues are usually **at-least-once** delivery, so a job can run **twice**. That is why you need idempotency

- **Caseway angle:** anything slow/bursty - bulk document ingestion, embedding a large upload, batch processing
- **Deep core angle:** a **3D model build takes minutes** -> it MUST be a background job: geologist submits hypothesis + data -> you return a job ID -> geostate workers run on build -> status streams back -> render when done 
    - In the AI pipeline, this queue would be implemented at the 3D model step:
        - plan generated → awaiting_approval → queued → running (compute) → rendering → complete
    - *"Planning and validation are synchronous; the moment the approved plan needs real compute or rendering, it becomes a background job — the agent triggers it via a tool call, my code enqueues it, workers process it, and status streams back to the geologist."*
 
## 5. Idempotency
- An operation is **idempotent** if running it multiple times produces the **same result with no extra side effects**. Run it once or five times = same end state
    - GET/PUT/DELETE are naturally idempotent. **POST IS NOT** (two POSTS = two records)
- **When you need it:** the moment you have **queues + retries**. Operations will run more than once
- **The mechanism - Idempotency Key**: the caller attaches a unique key to the operation. The server records "I've processed key X -> here is the result". If the same key arrives again, it **returns the stored result instead of re-executing**
    - Key must be the same across retries of the same logical pattern (that's what makes the dedup work)
- Idempotency is what makes retries *safe*. Retries give you reliability; idempotency stops reliability from corrupting your data 

- **Caseway angle:** idempotency keys for Stripe Webhooks for account actions 
- **Deep core angle:** you do not want two expensive 3D builds running. Attach an idempotency key to the build request

## 6. Rate limiting
- Capping how many request a client can make in a window - prevent abuse and protect expensive resources
- **Token bucket:** each user has a bucket with a **capacity** (max burst) that **refills at a fixed rate**. Each request spends a token; empty bucket = 429 Too Many Requests
    - State both numbers - capacity and refill rate. e.g. Capacity 10, refill 1/sec
  - **Why token bucket:** it allows short **bursts** (good UX) while bounding the **sustained** rate. Other algo's exist but token bucket is the default answer

## 7. Database + data scaling
- **Indexing** - the first lever for slow queries:
    - An index is a lookup structure so the DB doesn't scan every row. **Index the columns you filter (WHERE) and join on**
    - It is like an index at the back of a book. Instead of reading every page to find a topic, you jump straight to the right page.
- **Scaling reads -> read replicas**: copies of the DB that server read traffic. Most apps are read-heavy so this buys a lot. Caveat: **replica lag** 
- **Scaling writes -> sharding (last resort)**: split db across nodes by a shard key. Powerful but complex. Exhaust vertical + replicas + caching first
- **Vectors -> pgvector when you're already on Postgres**: one system, transactional, one backup. 

## 8. Replication & sharding
- **Replication = copies of the same data**
    - One **primary** (takes writes) + one or more **replicas** (copies)
    - **Solves**: read scaling + high availability 
    - The catch: **replica lag**
    - **Does not help with write scaling**

- **Sharding = splitting data across nodes**
    - Solves: write scaling + datasets too big for one machine
    - The cost: real complexity. Cross-shard queries are slow/awkward. Rebalancing painful. Bad shard key creates hot shards (one node overloaded)
    - Sharding should be a **last resort**

- **Deep Core**: 2-person tech team startup we will not shard. 

## 9. Consistency (CAP)
- **Cap theorem:** in a distributed system you can't have all 3: Consistency, Availability Partition-tolerance. Since network partitions *will* happen, the real choice under a partition is **Consistency OR Availability**
    - **CP** - refuse to answer rather than risk a stale/wrong answer (stay consistent, sacrifice availability)
    - **AP** - keep answering even if some nodes might be slightly stale (stay available, sacrifice strict consistency)
- **Strong vs. eventual consistency**
    - **Strong consistency** = every read returns the **latest** write, always. Costs latency/availability (nodes must coordinate)
    - **Eventual consistency** = reads might be **briefly stale**, but all copies **converge** given a little time. Fast and highly available,
    - Memory hook: **strong = always current; eventual = current eventually**
- **How to choose:**
    - **Strong** where stale data is dangerous: money, inventory, auth/permissions, anything where a wrong read causes a real-world error
    - **Eventual** where a brief lag is harmless: live/view counts, feeds, search indexes, analytics. Most of the consumer web leans AP + eventual 

## 10. Monolith vs microservices

*"My default is a modular monolith until there's a named reason to split — premature microservices are the classic early-stage mistake. The exception is splitting by workload, like a separate Python service for the geostat compute, which is justified. So I'd reach for services only when I can point at the specific bottleneck or constraint forcing it."*

## 11. Observability + reliability
- Observability = can you tell what your system is doing in prod
    - **3 pillars:**
        - **Logs** - discrete events 
        - **Metrics** - numbers over time (request rate, error rate, latency, CPU). Watch **percentiles, not averages** (**p95/p99** latency tells you the tail experience; an average hides it)
        - **Traces** - follow one request across services 
    - **LLM/agent-specific signals:** **cost-per-call, token usage, eval/faithfulness score, hallucination rate, drift over time**

- Reliability = staying up when dependencies misbehave
    - **Circuit breaker:** stop hammering a failing/slow dependency. Three states:
        - 1. **CLOSED** (normal) -> trips to 
        - 2. **OPEN** (fail fast, don't call it) -> after a cool-down,
        - 3. **HALF-OPEN** let one probe through, success = CLOSED, failure = back to OPEN
    - **Retries with backoff + jitter** - retry transient failures, but **exponentially back off** and add **jitter** so all clients don't retry in sync and create a thundering herd
    - **Graceful degredation** - when a dependency is down, serve a reduced experience instead of failing hard.

- **Caseway angle:** cost-per-call tracking and guards (token/truncation, dual-model routing) alongside Sentry alerts and logs. 

---

## Supabase / Cesium — "if it comes up" only (NOT studied)

- **Supabase** = managed Postgres + RLS → maps to JWT/tenant isolation. Q: "RLS or app-layer isolation?"
- **Cesium** = web 3D engine; hard part = perf w/ large meshes. Q: "LOD / tiling / streaming for large meshes?"
