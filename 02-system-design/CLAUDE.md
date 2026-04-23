# System Design Fundamentals — Progression Tracker

## Overview

The foundational section that everything else builds on. Covers core infrastructure concepts, architecture patterns, and the ability to reason about trade-offs verbally. This section is conceptual + diagramming + verbal practice, with some hands-on exercises where they reinforce understanding.

## Definition of Done

Can whiteboard a system, explain where it breaks first, justify every component choice, and discuss trade-offs without fumbling. Can answer "why not X instead?" for any architectural decision.

## Assignment Convention (CRITICAL — this section's biggest learning risk)

System design is the most concept-heavy, vocabulary-heavy section in the roadmap. The risk: Claude explains a topic for 30 minutes, John says "got it," we move on, and nothing sticks. **The fix: every sub-topic ends with a "now apply it" beat. No exceptions.**

For each sub-topic, the closing assignment must be one of:
1. **Written explain-back (1 paragraph)** — John writes the concept in his own words as if onboarding a junior. Goes into the section's `notes/` folder.
2. **Diagramming exercise** — Sketch the system or component, label parts, identify failure modes. Markdown or hand-sketch saved to `notes/`.
3. **Applied scenario** — Claude poses a concrete situation requiring John to use the concept to make a design decision. Walked through verbally or in writing.
4. **Mini code exercise** — When the topic has a natural code touchpoint (rate limiter algorithm, consistent hashing, bloom filter), implement it in 30-60 min.
5. **Block 3 interview challenge** — When applicable, pull a question from `10-interview-prep/system-design-rounds/` or another sub-folder. Optional, not required.

**Pure explanation followed by "got it, next" is the anti-pattern to avoid in this section above all others.**

End-of-section warm-down quiz is mandatory before marking the section complete (5-7 mixed-format questions, log result here).

---

## Sub-Topics

### Request Lifecycle (full end-to-end walkthrough)

The classic "what happens when you type a URL" interview question, walked stage by stage. Notes in `notes/01-request-lifecycle.md`.

- [x] Stage 1: DNS Resolution (cache hierarchy, TTL semantics, absolute-time TTL clarification)
- [x] Stage 2: TCP Handshake (three-way handshake, 1 RTT cost, connection reuse, head-of-line blocking)
- [x] Stage 3: TLS Handshake (encryption + integrity + auth, certs + CAs, ~1 RTT on TLS 1.3)
- [x] Stage 4: HTTP Request (methods + idempotency, status code classes, headers, Content-Type vs Accept, GET-as-DELETE failure modes, JWT 401 debugging menu)
- [x] Stage 5: Server-Side Processing (LB → app → cache → DB diagram, walking the stack for bottlenecks, N+1 queries vocabulary)
- [x] Stage 6: HTTP Response + Browser Render (incremental parsing, render-blocking, async vs defer, "loaded is a timeline")
- [~] HTTP versions (1.1 vs 2 vs 3) — DEFERRED. Senior+ depth, not needed for mid-level. One-line takeaway only: "versions evolved to reduce round trips; HTTP/2 multiplexes, HTTP/3 uses QUIC over UDP."

### Internet & Networking Fundamentals

Foundational knowledge that interviewers expect you to explain cold. "What happens when you type a URL in your browser?" is a classic interview question that touches all of these.

- [x] How the internet works: IP addresses, TCP vs UDP, ports, packets (high-level, not networking-engineer depth)
- [x] What is DNS — how domain name resolution works, DNS caching, TTL, recursive vs iterative lookup
- [x] What is HTTP — request/response cycle as a protocol, headers, methods, versions (HTTP/1.1 vs HTTP/2 vs HTTP/3 awareness)
- [x] What is HTTPS/TLS — what TLS does, how the handshake works (conceptual), certificates, why it matters
- [x] Web request lifecycle (DNS → TCP → TLS → HTTP → server → response) and latency at each stage
- [x] WebSockets — what they are, how they differ from HTTP, persistent connections, when to use them (real-time chat, live updates)
- [x] SSH — what it is, how it works (conceptual), key-based auth vs password

### Back-of-Envelope Estimation

This comes up in every system design interview. You'll be asked to estimate scale before designing anything. The goal is quick, reasonable napkin math — not precision.

- [~] Key latency numbers — DEFERRED. Not worth memorizing at mid-level. Skip unless prepping for senior+ rounds.
- [x] Throughput estimation: QPS from DAU × actions ÷ ~100K seconds, peak = 2-3x average
- [x] Storage estimation: items/day × size/item, then ×400 for yearly. Always convert up to GB/TB before drawing conclusions.
- [~] Bandwidth estimation — covered conceptually (QPS × response size). Skipped explicit practice; trivial enough to compute on demand.
- [x] Reads vs writes split + ratio → architectural justification (caching, replicas)
- [x] Full interview script practiced end-to-end on a Twitter-like prompt

### Core Concepts

- [x] Vertical vs horizontal scaling — when each applies, cost implications
- [x] CAP theorem — what it actually means in practice (not just the acronym)
- [x] Consistency models: strong vs eventual — real-world examples of each
- [x] Latency vs throughput — how to think about performance

### Architectural Patterns

- [x] Monolithic architecture — what it is, why it's usually the right choice for startups and small teams
- [x] Microservices — what problems they solve, what problems they create (network complexity, data consistency, operational overhead), when to actually use them
- [x] Monolith vs microservices trade-offs — the honest decision framework (not "microservices are always better")
- [x] Serverless — what it means (FaaS, BaaS), trade-offs (cold starts, vendor lock-in, cost model, debugging difficulty)
- [x] Event-driven architecture — pub/sub pattern, event sourcing (conceptual), when it makes sense

### Caching

- [x] Why caching matters — latency numbers every engineer should know
- [x] Cache-aside pattern (check cache → miss → query DB → populate cache)
- [x] Write-through vs write-behind caching
- [x] Cache eviction policies: LRU, LFU, TTL-based
- [x] Redis: what it is, common use cases (cache, session store, rate limiting, leaderboards)
- [x] CDN caching — what it caches, cache hierarchy, hit rates
- [x] Cache stampede / thundering herd — what it is and how to prevent it
- [x] When NOT to cache (dynamic/personalized content, low-read data)

### Load Balancing & Networking

- [x] What a load balancer does and where it sits
- [x] Algorithms: round-robin, least connections, weighted, consistent hashing
- [x] Session stickiness — when and why
- [x] Reverse proxy vs load balancer — overlap and differences
- [x] API Gateway pattern — authentication, rate limiting, routing

### Message Queues & Async Processing

- [x] Why async processing matters (decoupling, reliability, scale)
- [x] Producer-consumer pattern
- [x] Message queue concepts: at-least-once delivery + idempotency (at-most-once/exactly-once scoped out as overkill for mid-level)
- [x] Common tools: Redis Streams, RabbitMQ, SQS, Kafka, Celery (conceptual, not deep-dive)
- [x] When to use queues vs synchronous processing

### Database Architecture

- [x] SQL vs NoSQL decision framework (when to use each, with examples)
- [x] Database indexing — B-tree indexes, when they help, when they hurt
- [x] Database replication — primary/replica, read replicas
- [x] Database sharding — horizontal partitioning, shard keys, trade-offs
- [x] Connection pooling — why it matters, how it works
- [x] Storage types: blob/object storage (S3) vs block storage (EBS) vs file storage (EFS) — when to use each, especially for AI workloads (embeddings, documents, model artifacts)
- [x] Polyglot persistence — using the right DB for each job

### Search Infrastructure as a System Component

Trimmed from full-text search deep dive — research confirmed inverted indexes, LIKE/ILIKE, and BM25 internals are niche/Tier 3 for mid-level interviews. Lean coverage only: what Elasticsearch is, when to reach for it, how it fits into a system design answer. BM25 deferred to Section 5 (AI Production / hybrid search).

- [x] What Elasticsearch is and is not (search engine primarily; CAN function as a vector DB but that's not its primary identity)
- [x] When to add a search layer vs. querying the primary DB directly
- [x] How search fits into a system: read-optimized view, sync from primary DB, eventual consistency trade-off
- [x] Interview usage: how to drop a search layer into a system design answer confidently
- [x] BM25 vs embeddings distinction (CRITICAL — BM25 = keyword relevance scoring via term frequency + rarity; embeddings = vector/semantic similarity; hybrid search = combining both). Conflated in John's summary, corrected mid-session.

### Resilience & Reliability

- [x] Retries with exponential backoff (+ jitter, bounds, retry-eligible errors 5xx/network)
- [x] Circuit breaker pattern (three-state machine: CLOSED/OPEN/HALF-OPEN; HALF-OPEN probe is the self-heal mechanism — covered 2026-04-22; Q5 follow-up rep skipped per John's call 2026-04-22 late session, vocabulary stands as-documented in notes)
- [x] Idempotency — what it is and why it matters for distributed systems (mechanism locked: Idempotency-Key → server caches (key → result) → duplicate returns cached response)
- [x] Rate limiting — token bucket, sliding window algorithms (layered per-user + per-endpoint + Retry-After response pattern)
- [x] Graceful degradation — serving partial results vs failing entirely (critical path framing, per-component fallback strategies)

### Observability (Tier 3 — scoped lean)

Single deliverable: memorized 50-second interview paragraph covering the whole topic. No deep dive — buzzwords only. See `notes/12-observability.md`.

- [x] Three pillars vocabulary (logs / metrics / traces)
- [x] Key buzzwords: correlation IDs, Four Golden Signals, percentiles (p50/p95/p99), OpenTelemetry, PagerDuty
- [x] Memorized interview paragraph

### Case Studies (Practice Exercises)

Design each system. Sketch architecture. Claude pokes holes. Revise. Practice explaining out loud.

- [ ] Design a URL shortener
- [ ] Design a real-time chat system
- [ ] Design a rate limiter
- [ ] Design a social media feed (Instagram-like)
- [ ] Design a notification system

### Failure Analysis

Read and analyze real post-mortems. Identify what failed, why, and how to prevent it.

- [ ] Analyze 2-3 real post-mortems (Cloudflare, GitLab, GitHub, etc.)
- [ ] Document lessons learned

---

## End-of-Section Capstone

Run in its own dedicated session after all sub-topics and warm-down quizzes are complete. Three parts, all required.

### Part 1 — Written Quiz (20-30 min)
15 questions, mixed format: recall, "explain why," trade-off reasoning, and 2-3 applied scenarios spanning the full section. Scored. Any topic scoring below 70% triggers a targeted re-teach before the section closes — not "we'll revisit it later."

### Part 2 — System Design Challenge (45-60 min)
Fresh prompt John hasn't seen — not one of the practiced case studies. Design the full system cold: components, data flow, trade-offs, failure modes, scaling decisions. Claude pokes holes with "why not X?" and "what breaks first?" follow-ups. John must defend decisions or revise and explain why.

### Part 3 — Rapid-Fire Defense (10-15 min)
5-7 follow-up questions on the Part 2 design, interview-style. No notes. Tests whether understanding is real or pattern-matched to the prompt.

**Pass criteria:** Part 1 ≥ 70% with no catastrophic misses on core topics (CAP, caching, DB scaling), Part 2 design has no major conceptual errors and trade-offs are articulated, Part 3 ≥ 4/7 answered confidently. Section only closes when all three pass. Log result in Session Log below.

**Capstone result:** NOT YET RUN

---

## Session Log

| Date | Topics Covered | Assessment | Next Focus |
|------|---------------|------------|------------|
| 2026-04-06 | Internet & Networking Fundamentals (all sub-topics) | Solid grasp. Had working knowledge of HTTP from job experience. DNS chain, TLS handshake, and request lifecycle learned fresh — passed 5/5 quiz cold. | Back-of-Envelope Estimation |
| 2026-04-07 | Back-of-Envelope Estimation (lean version). QPS, peak vs avg, read/write split, storage, full interview script. | Pushed back hard initially — had never heard of QPS. Web research confirmed it's a real but optional interview topic; agreed on lean coverage. Worked through 5 concepts with progressive examples. Strong intuition on architectural translation (cache invalidation, hot/cold storage tiering, read-heavy → cache + CDN insight unprompted). Weak spot: arithmetic accuracy under pressure — final Twitter exercise undercounted total QPS by ~10x (12K instead of 102K), which led to undersized infra recommendations. Reasoning is ahead of math execution. Graded B. | Request Lifecycle |
| 2026-04-08 | Request Lifecycle — full 6-stage walkthrough end-to-end. DNS, TCP, TLS, HTTP request, server processing, HTTP response + browser render. HTTP/3 versions deferred (out of scope for mid-level). | Strong session, A-/B+ across the board. Stage 1 (DNS): missed the recursive resolver hierarchy on first try, picked it up cleanly + asked a senior-flavor question on whether cache hits reset TTL (they don't — absolute time-from-fetch). Stage 2 (TCP): blanked on TCP recall from networking sub-topic, conflated it with TLS (encryption guess). Re-taught cleanly, locked in head-of-line blocking vocabulary on the multiplayer game UDP question. Pushed back appropriately on SYN/ACK depth — correctly calibrated for mid-level scope. Stage 3 (TLS): nailed the layering one-liner; B+ on the cert error scenario (correctly identified cert validation failure but conflated "no TLS" with "broken TLS"). Stage 4 (HTTP): C+ on the GET-as-DELETE failure modes question — knew the rule but didn't push through to predict consequences (browser prefetch, CDN caching, history). Important gap to track: "knows the rule, hasn't internalized implications." Stage 5: A- walking the diagram for latency bottlenecks; introduced N+1 queries vocab. Stage 6: B+ on async/defer fix — right instinct, didn't commit to one answer. Latency math under-counted (parallel to yesterday's QPS arithmetic miss) — pattern is "reasoning ahead of arithmetic execution." Sub-topic locked. Session also included extensive notes hygiene work — converted bold-as-section to proper `##` header hierarchy across all 3 system-design notes for VSCode outline + GitHub TOC compatibility. | Core Concepts (vertical/horizontal scaling, CAP, consistency models, latency vs throughput) |
| 2026-04-09 | Core Concepts — all 4 chunks: vertical vs horizontal scaling, CAP theorem, consistency models (strong vs eventual), latency vs throughput. | B+ overall. Scaling: immediately reached for horizontal but initially framed it as "always better" — corrected to understand vertical-first for DBs, horizontal for stateless web servers, most systems do both. CAP: initially picked chat apps (Discord) as CP — corrected; chat is AP since brief staleness is fine, CP is for money/inventory. After correction, nailed the flash-sale ticket scenario with correct reasoning across all 4 concepts (CP, strong consistency, throughput as primary concern, horizontal for API servers). Consistency models: clean explanation of eventual consistency from the name alone. Latency vs throughput: swapped the chef/cafeteria analogy initially, corrected quickly, then correctly identified the 10K-user API degradation as a throughput problem. Applied wrap-up on ticket-selling system was strong — one minor correction on "DB scales horizontal too" when the pattern is DB stays vertical as long as possible. | Architectural Patterns (monolith vs microservices, serverless, event-driven) |
| 2026-04-13/14 | Architectural Patterns — all 5 chunks: monolith, microservices, monolith vs micro decision framework, serverless, event-driven architecture. Applied scenario: healthtech patient portal. | B+ overall. Strong instincts throughout: correctly chose monolith for 3-engineer MVP, identified SMS reminders and file uploads as event-driven, knew appointment booking must be synchronous. Recall question nailed the "don't over-engineer early" argument but initially stopped at "don't do it" without countering the advisor's specific argument — pushed to articulate *why* the operational tax kills a small team. Serverless scenario: correctly rejected Lambda for steady 50K req/hr but attributed it to cold starts (wrong — functions stay warm at that volume) instead of cost (right answer). Applied assignment: went on an on-prem/vector DB tangent (rabbit hole in an interview context), missed file upload processing as the key async candidate, missed audit logging as a compliance-critical synchronous requirement, wrote "50,000K" (units error). Good security instinct for healthtech but needs to learn HIPAA-compliant cloud is standard. Corrected monorepo vs monolith vocabulary confusion. | Caching |
| 2026-04-14 | Caching — all 7 chunks: why caching matters, cache-aside, write-through vs write-behind, eviction policies (LRU/LFU/TTL), Redis, CDN caching, cache stampede. Applied assignment: e-commerce product catalog caching design. | B overall. Conceptual understanding solid throughout — correctly explained why cache-aside degrades gracefully, picked write-behind for leaderboard scenario, good instinct on CDN for product images. Applied assignment exposed key gaps: (1) called invalidate-on-write "write-through" twice — knows the right behavior but used the wrong name, critical to fix for interviews; (2) applied staggered TTLs to the single-hot-key stampede problem when lock-based recomputation is the correct tool (had been told this 10 min prior); (3) proposed background polling for CDN image updates instead of simpler cache busting. Pushed back appropriately on needing all 3 stampede mitigations — agreed to drop background refresh, keep staggered TTLs + lock-based. Recall question (microservices): strong answer on engineer capacity bottleneck and 500 req/sec not needing microservices; correctly identified CI/CD pipeline proliferation and inter-service communication as specific operational costs. | Load Balancing & Networking |
| 2026-04-16 | Load Balancing & Networking — all 5 chunks: what LB does + placement, algorithms (round-robin, weighted, least connections, consistent hashing), session stickiness, reverse proxy vs LB, API gateway pattern. Applied assignment: food delivery app. Quiz: B-. | B- on quiz. Strong conceptual understanding. Key gaps: (1) initially placed LB after gateway instead of before — corrected to Public LB → Gateway cluster → per-service LBs → instances; (2) missed consistent hashing in Q1 — added to notes; (3) reverse proxy mental model inverted (said it sits between LB and servers, correct is between clients and servers); (4) rate limiting counter in Redis — nailed the bug (4 instances × 5 = 20 orders) and fix. Consistent hashing: knows session/state use case but missed cache key locality angle (same key always routes to same server = cache stays warm). Gateway architecture clarification: one gateway codebase, N identical instances — never one-per-service. Justified gateway with cross-cutting concerns (auth, rate limiting), not just service count. | Message Queues & Async Processing |
| 2026-04-17 | Message Queues & Async Processing — all 5 chunks (scoped lean): why async matters, producer-consumer, at-least-once + idempotency, common tools, when to use queues. | B+. Strong conceptual grasp — correctly explained why 200 consumer-crash messages aren't lost, nailed the async photo upload scenario with correct reasoning (202 Accepted introduced as new vocab). Idempotency definition was slightly off first attempt ("only fires once" vs "same result regardless of how many runs") — corrected but didn't re-articulate. Good scope instinct: pushed back on memorizing 3 delivery modes, we trimmed to just at-least-once. Celery flagged correctly as a real tool — noted as Python worker framework for Section 4. | Database Architecture |
| 2026-04-18 | Database Architecture — all 7 chunks: SQL vs NoSQL, ACID, indexing, replication, sharding, connection pooling, storage types + polyglot persistence. | B+ overall. Strong conceptual grasp throughout. Key gaps: called Elasticsearch a vector DB (it's a search engine — corrected); missed composite index hint on (user_id, created_at); initially conflated ACID durability with consistency. Good instincts: correctly chose document store for variable-schema catalog, flagged inventory as transactional, nailed read-your-own-writes, pivoted to conversation_id as shard key for messaging. Healthy pushback on connection pooling depth — scoped it lean, which was correct. Interview tangent on AI pipelines when asked about PDF storage — redirected to core answer (S3 + reference in DB). | Search Engines & Full-Text Search |
| 2026-04-21 | Search Infrastructure as a System Component — trimmed sub-topic. What ES is, when to add a search layer, sync/eventual consistency pattern, BM25 vs embeddings distinction. Stack Overflow applied scenario. | B/B+ overall. John pushed back on scope — correctly identified the original version as niche/extraneous. Web research confirmed search engines / BM25 / full-text search are Tier 3 for mid-level interviews. Trimmed to a 20-min survey. John was also right to push back on my "ES is not a vector database" oversimplification — ES CAN function as a vector database (his company Caseway uses it that way). Correct framing: ES is primarily a search engine that ADDED vector capabilities. Big correction mid-session: John conflated BM25 and embeddings in his summary — clarified that BM25 = keyword relevance scoring, embeddings = semantic/vector similarity, hybrid = both. This distinction is load-bearing for Section 5. Applied scenario (Stack Overflow): B/B+ — overbuilt by adding pgvector without justification (SO is classic keyword search, ES alone is the typical answer); minor imprecision on sync terminology ("ES read-only from DB") but eventual consistency reasoning was solid. Also covered real-world tangent on John's Caseway RAG stack (Postgres + pgvector + optional ES for legal research chat) — bookmarked for Section 5. | Resilience & Reliability |
| 2026-04-22 | Resilience & Reliability — all 5 chunks: retries + exponential backoff + jitter, idempotency + idempotency keys, circuit breaker + three-state machine, rate limiting (token bucket vs sliding window + layered limits + 429/Retry-After), graceful degradation (critical path + per-component fallback). Warm-down quiz 6 questions. Also large side-quest: markdown audit on all 11 notes files (34 bold-as-section-marker conversions to `###` across 9 files). | **B / B+ overall.** Chunks 1-5 covered cleanly with one-chunk-at-a-time pacing. Idempotency applied check (ride-share): initial answer C+ — missed that server RETURNS cached response (not just "discards" duplicate); corrected and mechanism now locked. Circuit breaker applied check (payment outage): C+ — didn't walk thread pool exhaustion → cascading failure mechanism for Q1; skipped HALF-OPEN recovery for Q2; both generic rather than scenario-specific. Rate limiting applied check: right algorithms both scenarios, overbudgeted refill rate on dashboard (10 tokens/sec = 600/min sustained for page-load-every-few-minutes traffic — same miss as the later quiz Q4a). Graceful degradation assignment (news aggregator): Grade C — didn't engage with the specific failing services in the scenario (trending-analytics + image CDN timeouts); thumbnails got zero treatment despite being 50% of failure; karma/notifications incorrectly placed in critical path. Wrote Claude's Review in the assignment file with better answer. **Quiz results:** Q1 recall A-, Q2 jitter A-, Q3 idempotency mechanism B+, Q4a token bucket B+ (overbudgeted numbers), Q4b sliding window A (layered 2/min + 5/day strong judgment), **Q5 circuit breaker state machine FAILED** (John removed three-state section from notes earlier deeming it "too in the weeds" — re-taught, re-added to notes, follow-up rep pending), Q6 arithmetic A ($600/hr calc unprompted — first positive data point on the recurring arithmetic gap). **Recurring pattern surfaced 4th+ time: "knows the rule, hasn't internalized implications"** — mid→senior gap. Drill locked: force naming of each scenario component and walking its specific failure path. Notes markdown audit added to Session End protocol auto-run going forward. | **Resilience & Reliability CLOSE-PENDING (Q5 follow-up first)**, then **Observability** |

---

## Notes & Weak Spots

- **Arithmetic under pressure:** John's reasoning about scale is genuinely strong, but he dropped a 10x error on the final estimation exercise (computed 12K QPS instead of 102K). The fix is mechanical: write each step, sanity-check the final number against the inputs (if reads are 50x writes and writes are 2K, reads should be 100K). Reinforce on any future estimation question that comes up — he should slow down on the math, not the reasoning.
- **Strong instincts to reinforce:** Stumbled into cache invalidation pattern unprompted. Suggested CDN for image-heavy workload unprompted. Suggested hot/cold storage tiering unprompted. These are all senior-level intuitions — when they appear, name them explicitly so he learns the vocabulary that goes with the instinct.
- **Pushback culture:** John pushed back when introduced to estimation (had never heard of QPS), asked for web research to validate the topic, and we negotiated a lean version. This is good — he's not just absorbing whatever's in front of him. Honor this pattern: if he pushes back on a topic, do the research, give an honest answer, and adjust scope rather than insisting.
- **"Knows the rule, hasn't internalized implications":** Surfaced 2026-04-08 on the GET-as-DELETE failure modes question. John knew the principle ("GET should never modify state") cold but couldn't predict the *concrete consequences* (browser prefetch, CDN caching, history replay, log leakage). This is the mid→senior gap. When asking applied questions on principles he claims to know, push past the rule-statement and force prediction of failure modes. The rule is the easy part; the consequences are where understanding lives.
- **Arithmetic execution lags reasoning (recurring):** Confirmed pattern across two sessions now. 2026-04-07: undercounted Twitter QPS by ~10x. 2026-04-08: undersized "20 fresh TCP connections at 200ms RTT" answer ("saves a round trip" — singular) when the actual answer was 4 seconds. Reasoning is consistently ahead of math execution under pressure. Reinforce on every numeric question: write each step, give the actual number, sanity-check magnitude.
- **Notes formatting standard (locked in 2026-04-08):** All section notes now follow `#` for file title, `##` for major sections, `###` for sub-sections, **bold** reserved for vocabulary/emphasis only — never for section markers. Code blocks always fenced with language tag. Apply same standard going forward when creating or editing notes in any section.
