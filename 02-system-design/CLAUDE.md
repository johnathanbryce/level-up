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

- [ ] Vertical vs horizontal scaling — when each applies, cost implications
- [ ] CAP theorem — what it actually means in practice (not just the acronym)
- [ ] Consistency models: strong vs eventual — real-world examples of each
- [ ] Latency vs throughput — how to think about performance

### Architectural Patterns

- [ ] Monolithic architecture — what it is, why it's usually the right choice for startups and small teams
- [ ] Microservices — what problems they solve, what problems they create (network complexity, data consistency, operational overhead), when to actually use them
- [ ] Monolith vs microservices trade-offs — the honest decision framework (not "microservices are always better")
- [ ] Serverless — what it means (FaaS, BaaS), trade-offs (cold starts, vendor lock-in, cost model, debugging difficulty)
- [ ] Event-driven architecture — pub/sub pattern, event sourcing (conceptual), when it makes sense

### Caching

- [ ] Why caching matters — latency numbers every engineer should know
- [ ] Cache-aside pattern (check cache → miss → query DB → populate cache)
- [ ] Write-through vs write-behind caching
- [ ] Cache eviction policies: LRU, LFU, TTL-based
- [ ] Redis: what it is, common use cases (cache, session store, rate limiting, leaderboards)
- [ ] CDN caching — what it caches, cache hierarchy, hit rates
- [ ] Cache stampede / thundering herd — what it is and how to prevent it
- [ ] When NOT to cache (dynamic/personalized content, low-read data)

### Load Balancing & Networking

- [ ] What a load balancer does and where it sits
- [ ] Algorithms: round-robin, least connections, weighted, consistent hashing
- [ ] Session stickiness — when and why
- [ ] Reverse proxy vs load balancer — overlap and differences
- [ ] API Gateway pattern — authentication, rate limiting, routing

### Message Queues & Async Processing

- [ ] Why async processing matters (decoupling, reliability, scale)
- [ ] Producer-consumer pattern
- [ ] Message queue concepts: at-least-once, at-most-once, exactly-once delivery
- [ ] Common tools: Redis Streams, RabbitMQ, SQS (conceptual, not deep-dive)
- [ ] When to use queues vs synchronous processing

### Database Architecture

- [ ] SQL vs NoSQL decision framework (when to use each, with examples)
- [ ] Database indexing — B-tree indexes, when they help, when they hurt
- [ ] Database replication — primary/replica, read replicas
- [ ] Database sharding — horizontal partitioning, shard keys, trade-offs
- [ ] Connection pooling — why it matters, how it works
- [ ] Storage types: blob/object storage (S3) vs block storage (EBS) vs file storage (EFS) — when to use each, especially for AI workloads (embeddings, documents, model artifacts)
- [ ] Polyglot persistence — using the right DB for each job

### Search Engines & Full-Text Search

Relevant to current job (Elasticsearch) and ties into hybrid search in Section 5 (AI Production). Conceptual understanding + awareness of when to reach for a search engine vs other tools.

- [ ] What full-text search is — inverted indexes (conceptual: word → list of documents containing it), tokenization, analyzers
- [ ] When to use a search engine vs database LIKE/ILIKE queries vs vector search — decision framework
- [ ] Elasticsearch/OpenSearch awareness: what it is, common use cases (search, log aggregation, analytics), basic concepts (index, document, mapping, query DSL at a high level)
- [ ] How search fits into a system: search as a read-optimized view, syncing data from primary DB to search index, eventual consistency trade-off
- [ ] Relevance scoring basics: TF-IDF / BM25 (conceptual — know what they optimize for, not the math)

### Resilience & Reliability

- [ ] Retries with exponential backoff
- [ ] Circuit breaker pattern
- [ ] Idempotency — what it is and why it matters for distributed systems
- [ ] Rate limiting — token bucket, sliding window algorithms
- [ ] Graceful degradation — serving partial results vs failing entirely

### Observability

- [ ] Structured logging (JSON logs, correlation IDs)
- [ ] Metrics: what to measure (latency, error rate, throughput, saturation)
- [ ] Distributed tracing — what it is and when you need it
- [ ] Alerting: thresholds, on-call, escalation (conceptual)

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

## Session Log

| Date | Topics Covered | Assessment | Next Focus |
|------|---------------|------------|------------|
| 2026-04-06 | Internet & Networking Fundamentals (all sub-topics) | Solid grasp. Had working knowledge of HTTP from job experience. DNS chain, TLS handshake, and request lifecycle learned fresh — passed 5/5 quiz cold. | Back-of-Envelope Estimation |
| 2026-04-07 | Back-of-Envelope Estimation (lean version). QPS, peak vs avg, read/write split, storage, full interview script. | Pushed back hard initially — had never heard of QPS. Web research confirmed it's a real but optional interview topic; agreed on lean coverage. Worked through 5 concepts with progressive examples. Strong intuition on architectural translation (cache invalidation, hot/cold storage tiering, read-heavy → cache + CDN insight unprompted). Weak spot: arithmetic accuracy under pressure — final Twitter exercise undercounted total QPS by ~10x (12K instead of 102K), which led to undersized infra recommendations. Reasoning is ahead of math execution. Graded B. | Request Lifecycle |

---

## Notes & Weak Spots

- **Arithmetic under pressure:** John's reasoning about scale is genuinely strong, but he dropped a 10x error on the final estimation exercise (computed 12K QPS instead of 102K). The fix is mechanical: write each step, sanity-check the final number against the inputs (if reads are 50x writes and writes are 2K, reads should be 100K). Reinforce on any future estimation question that comes up — he should slow down on the math, not the reasoning.
- **Strong instincts to reinforce:** Stumbled into cache invalidation pattern unprompted. Suggested CDN for image-heavy workload unprompted. Suggested hot/cold storage tiering unprompted. These are all senior-level intuitions — when they appear, name them explicitly so he learns the vocabulary that goes with the instinct.
- **Pushback culture:** John pushed back when introduced to estimation (had never heard of QPS), asked for web research to validate the topic, and we negotiated a lean version. This is good — he's not just absorbing whatever's in front of him. Honor this pattern: if he pushes back on a topic, do the research, give an honest answer, and adjust scope rather than insisting.
