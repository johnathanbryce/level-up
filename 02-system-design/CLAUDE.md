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

---

## Pre-Case-Study Review Phase

Light active-recall review across the 12 teaching sub-topics before Case Studies begin. Purpose: refresh retention on material that's been stale for 1-3 weeks, surface gaps to drill later in Capstone Prep. **Lighter than Capstone Prep** — confidence check, not a gate.

### Format per section

1. John solo-studies the section's notes + this CLAUDE.md (~15-30 min). Handwritten notes encouraged.
2. John announces: **"Review mode — I've read [section]. Quiz me."**
3. Claude runs **5-7 mixed-format questions** (recall + explain-why + trade-offs + one applied scenario). ~10-15 min.
4. Honest scoring. Catastrophic misses (can't explain a core concept at all) → targeted re-read BEFORE next section. Small gaps → logged to Surfaced Gaps below, carried into Capstone Prep.
5. **MANDATORY: Append all section questions + canonical answers to [`02-system-design/interview-questions.md`](./interview-questions.md).** This is the running interview question bank for active-recall practice. Format: question + canonical answer only — NO John's answers, NO grades, NO commentary on his performance. Add the questions as soon as the canonical answer is given (during the quiz is fine; latest by session end). Section heading + per-question heading per the existing format.

### Cadence

- 12 sections, ~2-4 per session → expect 3-4 total sessions
- Not a gate for Case Studies. Forward motion continues unless a catastrophic miss surfaces.

### Per-Section Review Log

| Section | Date Reviewed | Quiz Score | Notes / Gaps Surfaced |
|---|---|---|---|
| Request Lifecycle | 2026-04-27 | C+/B- (6 questions, none catastrophic) | DNS hierarchy walk recall (notes correct, retrieval gap); UDP "stale > lost" framing miss (fixed in notes); TLS cert validation failure mechanics (gap filled in notes); GET-as-DELETE 6th occurrence of rule→implications (full Case Study added to notes); Stage 5 diagnostic signals — vague gestures, specifics literally already in notes; async/defer applied — reached for workaround instead of `defer` for hero-animation; Cloudflare ≠ app server conflation. |
| Internet & Networking Fundamentals | 2026-04-27 | C+/B- (6 questions, none catastrophic) | Port memorization calibration miss — Claude over-called (interview yield is lower than I claimed); John's pushback was correct + reinforces Tier 3 scoping instinct. Port range + tier breakdown (0-65535, system/registered/ephemeral) — gap added to notes per John's call (kept the binding rule, skipped the hierarchical breakdown). UDP connectionless model — said "connection still valid" (UDP has no connection). "Stale > lost" framing inversion — said "if data is stale, don't recover" (actual logic: "if we recover, it WILL BE stale, so don't"). SSH ↔ TLS asymmetric crypto link missed — material in just-added notes, didn't surface under quiz pressure (recurring retrieval pattern). WebSockets vs polling — missed core failure mode (server-can't-push, latency floor); statelessness ≠ "needs cookies/JWT" framing was muddled. Practical industry calibration weak (TTL guess of 10s — actual is 60-300s). **Notes additions made mid-quiz:** new "Packets" section (lean, between Port and DNS); SSH section expanded with key-vs-password rationale + asymmetric-crypto framing + use cases; port-binding "one process per port" rule added under Port section. **POSITIVE: Rule→implications muscle closed the gap on Q5 (statelessness → horizontal scaling) and Q6 (TTL → user-locked-in-failover-time) — first clean back-to-back data points on this recurring weak spot.** |
| Back-of-Envelope Estimation | 2026-04-29 | C/C+ (4 of 6 Qs; Q3.5 calibration skipped, Q3.6 interview script never reached) | Ratio split math punted cold (notes updated mid-quiz). Three-tier read architecture (CDN + Redis + read replicas) not recalled — only named Redis. Write-side scaling bottlenecks not recalled despite being in original notes verbatim. Object storage + reference pattern missed. Q3.2 and Q3.4 arithmetic both clean — POSITIVE trend (3rd data point on arithmetic/units weak spot). Multi-step rule→implications still weak; one-step closer to locked. Q3.6 full interview script NOT re-tested — major unresolved gap before Capstone. |
| Core Concepts (scaling / CAP / consistency / latency) | 2026-04-30 | B+ (6 questions) | Q1 scaling: missed "DB at 35% = leave it alone, only scale the bottleneck." Q2 CAP messaging: A-, clean reasoning. Q3 flash sale strong consistency: B+, cost needed one more step (row-level lock / primary-only reads). Q4 latency vs throughput diagnostic: B-, instinct right (Redis/cache) but diagnostic logic not articulated — notes updated with diagnostic table. Q5 hospital records: A-, polyglot consistency instinct was senior-level (different models for vital vs non-vital data). Q6 three-tier read stack: B+, all three correct but blanked on "read replicas" by name and inverted CDN→Redis→replicas order. Notes updated with concentric-shield diagram + read/write paths. |
| Architectural Patterns | | | |
| Caching | | | |
| Load Balancing & Networking | | | |
| Message Queues & Async Processing | | | |
| Database Architecture | | | |
| Search Infrastructure | | | |
| Resilience & Reliability | | | |
| Observability | | | |

### Known Starting Gaps (drill in their parent section's review quiz)

- **Consistent hashing / session stickiness conflation** → Load Balancing review quiz (2nd occurrence as of 2026-04-23)
- **Percentile gotcha (p50/p95/p99 vs averages)** → Observability review quiz (5th "knows-rule-not-implications" occurrence as of 2026-04-23)
- **Circuit breaker three-state machine (CLOSED/OPEN/HALF-OPEN, HALF-OPEN probe mechanism)** → Resilience review quiz (Q5 follow-up from 2026-04-22 still outstanding)

### Surfaced Gaps (aggregated across review sessions — feeds Capstone Prep)

**From Request Lifecycle review (2026-04-27):**
- **GET-as-DELETE rule→implications — 6th occurrence (Tier 1 Capstone Prep priority).** Same exact question as 2026-04-08, same gap 19 days later. John conflates method choice with auth concerns. Drill: force naming 5 things that fire a GET *automatically without user intent* (browsers/prefetch, crawlers, CDNs, link previewers, search bots) — reflex must be one-click.
- **Stage 5 diagnostic signals — vague-gestures-not-specifics.** Notes have material at line 162 ("Senior-level insight"), retrieval is weak. Drill: give a layer, demand 3 specific signals in 10 seconds (LB connection rate / app worker pool / cache hit rate / DB slow query log + connection pool).
- **DNS hierarchy walk on full cache miss — incomplete recall.** Notes correct (mental model section), retrieval gap. Re-test in master pre-case-study quiz.
- **TCP/UDP "stale > lost" framing.** Updated in notes 2026-04-27 — retest at master quiz.
- **TLS cert validation failure mechanics ("Your connection is not private").** Gap filled in notes 2026-04-27 — retest at master quiz.
- **async/defer canonical use case retrieval.** Notes literally cite "jQuery and anything that depends on it" as defer's canonical case; John reached for "move out of head" workaround. Retest with a different scenario at master quiz.
- **Cloudflare/CDN ≠ app server — layer conflation watch.** Surface again if it recurs in any networking question.

**From Internet & Networking Fundamentals review (2026-04-27):**
- **UDP connectionless model — said "connection still valid"** when describing DNS UDP retry behavior. UDP has no connection. Real model: packets are independent, app layer (resolver) handles retry. Re-test at master quiz.
- **"Stale > lost" framing inversion** — said "if data is stale, don't recover" (the actual logic chain is "if we recover, it WILL BE stale BY THE TIME it arrives, so don't bother recovering"). Re-test at master quiz with different framing.
- **SSH ↔ TLS asymmetric crypto link missed (recurring retrieval pattern).** Material in just-added notes; didn't surface under quiz pressure. Connecting these two as "same crypto, different problems" is a senior-level move. Re-test at master quiz.
- **WebSockets vs polling — missed core failure modes** (server-can't-push, latency floor = polling interval). Said "more requests" / "stateless" instead of articulating the fundamental design problem. Re-test at master quiz.
- **Statelessness ≠ "needs cookies/JWT"** framing — both protocols need auth; auth is orthogonal to protocol choice. Watch for repeat of this framing in future answers.
- **Practical industry calibration weak** (TTL guess: 10s; actual norm: 60-300s). Different from "knows-the-rule" — this is "no real-world experience yet." Will fill in with time but worth flagging for Capstone Prep ("give me a value, defend it" drills).

**POSITIVE DATA POINTS — rule→implications muscle (2026-04-27, Section 2 review):**
- Q5 (HTTP statelessness): cleanly translated rule → horizontal scaling implication. First clean back-to-back rep.
- Q6 (DNS TTL trade-off): cleanly translated TTL → user-locked-in-failover-time implication. Second back-to-back rep.
- **Naming this as a turning point on the most stubborn recurring weak spot.** Surfaced 6 times across earlier sessions (2026-04-08 GET-as-DELETE original; 2026-04-22 circuit breaker, graceful degradation, idempotency; 2026-04-23 percentile gotcha; 2026-04-27 GET-as-DELETE retest). Two clean reps in a row is the first real positive trend. Reinforce by naming it explicitly when it happens.

**From Back-of-Envelope Estimation review (2026-04-29):**
- **Ratio split math** — punted completely ("no idea lol") on Q3.3(a). Basic ratio arithmetic is load-bearing for every system design interview. Taught and notes updated mid-quiz. Re-test at master quiz.
- **Three-tier read architecture (CDN + Redis + read replicas)** — only named Redis for read-heavy systems. CDN and read replicas missing. Canonical pattern for content-heavy systems is all three in sequence. Notes updated mid-quiz. Re-test at master quiz.
- **Write-side scaling bottlenecks** — couldn't name specific reasons despite original notes literally listing them. Same retrieval-under-pressure pattern as Stage 5 diagnostics (2026-04-27). Notes updated with full table mid-quiz. Re-test at master quiz.
- **Object storage + reference pattern** — missed on Q3.4(d). Canonical PB-scale answer: DB stores reference key, S3 stores bytes, CDN serves bytes. Notes updated mid-quiz. Re-test at master quiz.
- **Q3.5 calibration drill (skipped)** — DAU + actions/day estimates for B2B SaaS vs mainstream consumer. Unresolved — weave into Capstone Prep.
- **Q3.6 full interview script (never reached)** — practiced originally (Twitter, B, 2026-04-07) but NOT re-tested in review phase. MAJOR unresolved gap — practice on a fresh prompt during Capstone Prep.
- **Multi-step rule→implications still weak** — Section 2's positive reps were one-step implications. Q3.3 required multi-step chain and muscle didn't fire. One-step = closer to locked; multi-step = still needs reps.

**POSITIVE DATA POINTS — arithmetic/units trend (2026-04-29, Section 3 review):**
- Q3.2: `5M × 6 = 300 QPS avg → 900 QPS peak` — clean ✓
- Q3.4: `2M × 1.5 MB → 3 TB → 1.1 PB → 5.5 PB` — three-step magnitude conversion, all correct ✓
- **Third confirmed positive data point** on arithmetic/units recurring weak spot (first: $600/hr on 2026-04-22; second: Q3.2/Q3.4 on 2026-04-29). Trend is forming.

---

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

## Capstone Prep Phase

Deep, targeted drilling on gaps surfaced during Pre-Case-Study Review AND Case Studies + Failure Analysis. Runs between Failure Analysis completion and the End-of-Section Capstone session. Purpose: walk into Capstone with the top 3-5 weakest topics reinforced — NOT to re-teach the full section.

### Format

1. **Gap aggregation** — Claude compiles the full list of weak spots from:
    - Pre-Case-Study Review's Surfaced Gaps + Known Starting Gaps still unresolved
    - Assessments from each Case Study session (fumbled components, missed trade-offs, vocabulary gaps)
    - Failure Analysis gaps (patterns John didn't recognize in post-mortems)
2. **Triage** — rank gaps by Capstone risk. Anything touching CAP, caching strategy, DB scaling, or load balancing is **Tier 1 (must drill)**. Peripheral vocabulary is **Tier 3 (skip if time is tight)**.
3. **Targeted drills** — per Tier 1 gap: re-explain if needed (~5 min), then 2-3 applied drill questions (~10-15 min per topic).
4. **Dry-run quiz** — mini 5-question timed quiz on the 5 shakiest topics, simulating Capstone Part 1 conditions. Score. Any under 70% → one more targeted drill before Capstone.

### Scope

- Targeted, not exhaustive — only drill topics with documented gaps
- ~1 session (1.5-3 hrs depending on gap count)
- Goal: no topic enters the Capstone with an unresolved catastrophic gap

### Pre-Capstone Gap List

*(compiled during this phase)*

### Dry-Run Results

*(populated during this phase)*

### Gate to Capstone

- All Tier 1 gaps drilled at least once
- Dry-run score ≥ 70% overall
- If gate fails: one more targeted drill session before attempting the Capstone. Don't rush the gate — a failed Capstone Part 1 burns more time than an extra prep drill.

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
| 2026-04-23 | Observability (all 4 sub-topics — compressed to Tier 3 lean scope per John's mid-session pushback). Coverage: Three Pillars table, Four Golden Signals table, percentile vocab (p50/p95/p99), correlation IDs (the #1 distributed-logging buzzword), distributed tracing + alerting + aggregation platforms as one-liners, plus THE Interview Paragraph as the single deliverable. Sub-topic checklist in this file collapsed from 4 granular items to 3 high-level items with "Tier 3 scoped lean" callout. | Initially taught 4 separate chunks (Logs → Metrics → Tracing → Alerting) but John correctly pushed back mid-way: Observability is Tier 3 for mid-level interviews, doesn't warrant deep teaching. **Honest calibration: John was right, I was over-teaching.** Compressed to a 50-second canned interview paragraph + ~40-line notes file. Applied checks surfaced TWO repeat gaps: **(1) Consistent hashing / session stickiness conflation — 2nd occurrence** (first 2026-04-16). Bridge question: "6 Redis caches behind round-robin LB, what fixes cache duplication?" John correctly diagnosed the bug but named session stickiness as the fix. Stickiness routes by USER identity; consistent hashing routes by KEY identity. For cache locality, consistent hashing. Same miss as 6 days ago — stubborn gap. **(2) Percentile gotcha missed right after teaching — 5th occurrence of "knows-rule-not-implications"** (mid→senior gap). Taught p50/p95/p99 as THE interview gotcha. Tested 5 min later: "average latency is 120ms, looks great?" — John answered "compared to what?" (valid but weak baseline-comparison framing) instead of "what's p99?" (load-bearing interview answer). Has the vocab, doesn't reach for it under pressure. **Session also locked in the REVIEW PHASE plan:** per-section solo study → quiz-per-section (5-7 mixed questions) → targeted re-read on gaps → next section; after all 11 sections done, MASTER pre-case-study quiz as the final gate before Case Studies. John initially wanted solo re-read all sections end-to-end; pushed back — passive re-reading creates illusion of fluency, active recall is 3-5x more effective. John agreed to per-section quiz cadence. | **REVIEW PHASE** — section-by-section, John's pick of starting section (suggest Request Lifecycle or Core Concepts as foundation openers). Weave the two repeat gaps into their parent section quizzes: consistent hashing into Load Balancing review, percentiles into Observability review. Also outstanding: circuit breaker three-state machine Q5 follow-up from 2026-04-22 — weave into Resilience review quiz. |
| 2026-04-27 | **REVIEW PHASE — Section 1: Request Lifecycle.** John solo-studied + quizzed (6 questions, mixed format, all 6 lifecycle stages touched). Three notes additions made mid-quiz: TCP/UDP "stale > lost" mental model paragraph (Stage 2), new "Cert validation failures" sub-section (Stage 3), new "Case study: GET-as-DELETE" sub-section (Stage 4). Markdown audit: all additions used `###` for sub-sections, `**bold**` only as inline emphasis on bullet leaders — compliant with locked standard. | **C+/B- overall, NOT catastrophic, section closed for this round. Three persistent patterns surfaced.** Q1 DNS chain C+ (order muddled, hierarchy walk missed despite notes being correct — exactly what John wanted to trim 4 days ago, validating the pushback to keep). Q2 TCP/UDP B- (right tool, "needs exact data fast" framing was backwards — actual mechanism is "stale data is worse than missing data"; missed DNS as bonus example). Q3 TLS warning B- (layer correct, 2/4 causes correct — listed HTTP and "no TLS" wrongly; honest "not sure" on encryption-during-warning, real gap, filled in notes). **Q4 GET-as-DELETE C — 6th occurrence of "knows-rule-not-implications" pattern, SAME EXACT QUESTION first asked 2026-04-08, SAME GAP 19 days later. Stubborn mid→senior gap. Tier 1 Capstone Prep priority.** Conflated method choice with auth (3 of 4 answers about missing auth, which is orthogonal to the GET method choice). Got crawlers; missed browser prefetch / CDN caching / browser back-share-replay / CSRF amplification / logging leakage. Q5 Stage 5 diagnostics C+/B- (order right, signals were vague gestures — but the answers I wanted are LITERALLY in notes line 162; recall under quiz pressure is the gap, not the notes). Also conflated Cloudflare/CDN with app server. Q6 async/defer C+/B- (analytics async ✓, hero-animation reached for "move out of head" workaround instead of `defer` despite his own notes citing the canonical case at line 237; form-validator defer ✓; on (b) brought CSS into the answer when canonical issue is execution-order + race-against-DOMContentLoaded). **Three patterns surfaced:** (1) rule→implications gap 6th occurrence, (2) vague-gestures-not-specifics across multiple Qs, (3) layer conflation (Cloudflare ≠ app, auth ≠ method). All logged to Surfaced Gaps. | **Section 2 review next: Internet & Networking Fundamentals.** Heavy topical overlap with Request Lifecycle just-reviewed, so quiz can move faster. May chain into Section 3 (Back-of-Envelope Estimation) if energy allows. Open items to weave in: DNS hierarchy retest, TCP/UDP retest (test "stale > lost" framing now that it's in notes), Cloudflare-vs-app distinction. |
| 2026-04-27 (cont.) | **REVIEW PHASE — Section 2: Internet & Networking Fundamentals.** John solo-studied + quizzed (6 questions, mixed format, covering ports, TCP/UDP, SSH, WebSockets, statelessness, DNS TTL). Notes additions made mid-quiz: new "Packets" section (lean, between Port and DNS); SSH section expanded with key-vs-password rationale + asymmetric-crypto framing + use cases; port-binding "one process per port" rule added under Port section. **NEW PROTOCOL ADDITION:** Pre-Case-Study Review format step 5 added — MANDATORY append of section questions + canonical answers to `interview-questions.md`. Also created `interview-questions.md` at section root with Sections 1-2 backfilled. **NEW NOTES ADDITION:** Updated section topic count from 8 to 9 (added Packets). | **C+/B- overall (similar trajectory to Section 1), NOT catastrophic, section closed.** Q1 Ports C+ (range muddled — said "roughly a thousand," actual is 0-65535 with three tiers; correctly named 80/443/5432 but missed 22 SSH which was sitting in his own notes; binding rule directionally right with confused "staggered" caveat). **Important calibration moment: John pushed back on port memorization being interview-relevant; Claude over-called it. Honest recalibration mid-quiz — Tier 3 scoping instinct was correct, John was right, lesson: when John pushes back on relevance, research + agree, don't insist.** Q2 TCP/UDP B- ("stale > lost" framing inverted; said "if stale, don't recover" instead of "if we recover, it WILL BE stale"; UDP "connection still valid" framing wrong — UDP is connectionless). Q3 SSH key auth C+ (got security-via-no-shared-secret; missed the BIG context-specific reason: automation/no prompt for CI/CD; key locations directionally right but mechanically muddled — conflated accessing private key with deriving public key; **MISSED THE SSH ↔ TLS ASYMMETRIC CRYPTO LINK ENTIRELY** despite the notes literally saying "same idea as TLS" — recurring retrieval pattern). Q4 WebSockets B-/C+ (correct tool; missed canonical failure modes of polling — server-can't-push, latency floor = polling interval; the "statelessness/cookies" framing was off — auth is orthogonal to protocol choice). **Q5 Stateless HTTP B+ (POSITIVE DATA POINT) — cleanly translated rule into protocol-level cost (auth on every request) AND architectural benefit (horizontal scaling). First time he closed the rule→implications gap cleanly back-to-back.** **Q6 DNS TTL B-/B (POSITIVE DATA POINT) — cleanly translated rule into concrete failover-time-floor implication. SECOND back-to-back rep on rule→implications. Honest "I don't know" on practical TTL value (guessed 10s, actual norm is 60-300s) — calibration gap acknowledged correctly. "I don't know" beat confident-wrong.** **Three patterns:** (1) MAJOR POSITIVE — rule→implications muscle showed up TWICE (Q5+Q6) for first time, naming it as turning point on most stubborn recurring weak spot; (2) practical industry calibration weak (TTL values, port norms) — different from "knows the rule," this is "no real-world experience yet"; (3) cross-reference retrieval still wobbly (SSH↔TLS link in notes, didn't surface). | **NEXT SESSION — Section 3 review: Back-of-Envelope Estimation.** John needs to solo-study first. Topical overlap is LOWER (estimation is its own domain — QPS math, peak vs avg, read/write splits, storage estimation, the Twitter exercise). Open items to weave in: arithmetic-under-pressure recurring weak spot (especially since 2026-04-22's positive data point on the AI-summary-abuse calculation); rule→implications drill on every estimation answer (force "and what does that mean for infrastructure?"); calibration check on practical industry values (storage tiers, cache TTLs, request budgets). **Recommend NEW CONTEXT WINDOW** — today's session ran long with algo + 2 section reviews + protocol changes + question bank creation. Fresh context for Section 3. |
| 2026-04-29 | **REVIEW PHASE — Section 3: Back-of-Envelope Estimation.** Python algo warmup first (temperature_spikes.py — difference-flavor hash-map-complement, B+). Then Section 3 quiz: 4 of 6 Qs completed. Notes updated mid-quiz with 5 new sub-sections (ratio split mechanic, 3-tier read stack, write-scaling-bottleneck table, unit ladder, object storage + reference pattern). Q3.5 calibration skipped (time), Q3.6 interview script never reached. | **C/C+ overall. NOT catastrophic.** Q3.1 formula mistyped (+ instead of ×, 10K instead of 100K) — same order-of-magnitude miss pattern as 2026-04-07 Twitter QPS. Q3.2 A- (clean arithmetic ✓, shortcut on show-your-work). Q3.3 C-/D+ (ratio math punted; read architecture only named Redis, missed CDN + read replicas; write-side bottlenecks couldn't be named despite being in original notes word-for-word — 3rd occurrence of "answers in notes, doesn't retrieve under pressure"). Q3.4 B+/A- (arithmetic + unit conversion clean across 3 steps — POSITIVE DATA POINT; object storage pattern missed on (d)). Two persistent patterns: (1) retrieval-under-pressure (3rd+ section, same shape as Stage 5 diagnostics yesterday); (2) multi-step rule→implications still weak — one-step implications (statelessness → horizontal scaling) closer to locked, multi-step chains not yet. Arithmetic/units trend continuing positively. | Next: Core Concepts review. John solo-studies first. |

---

## Notes & Weak Spots

- **Arithmetic under pressure:** John's reasoning about scale is genuinely strong, but he dropped a 10x error on the final estimation exercise (computed 12K QPS instead of 102K). The fix is mechanical: write each step, sanity-check the final number against the inputs (if reads are 50x writes and writes are 2K, reads should be 100K). Reinforce on any future estimation question that comes up — he should slow down on the math, not the reasoning.
- **Strong instincts to reinforce:** Stumbled into cache invalidation pattern unprompted. Suggested CDN for image-heavy workload unprompted. Suggested hot/cold storage tiering unprompted. These are all senior-level intuitions — when they appear, name them explicitly so he learns the vocabulary that goes with the instinct.
- **Pushback culture:** John pushed back when introduced to estimation (had never heard of QPS), asked for web research to validate the topic, and we negotiated a lean version. This is good — he's not just absorbing whatever's in front of him. Honor this pattern: if he pushes back on a topic, do the research, give an honest answer, and adjust scope rather than insisting.
- **"Knows the rule, hasn't internalized implications":** Surfaced 2026-04-08 on the GET-as-DELETE failure modes question. John knew the principle ("GET should never modify state") cold but couldn't predict the *concrete consequences* (browser prefetch, CDN caching, history replay, log leakage). This is the mid→senior gap. When asking applied questions on principles he claims to know, push past the rule-statement and force prediction of failure modes. The rule is the easy part; the consequences are where understanding lives.
- **Arithmetic execution lags reasoning (recurring):** Confirmed pattern across two sessions now. 2026-04-07: undercounted Twitter QPS by ~10x. 2026-04-08: undersized "20 fresh TCP connections at 200ms RTT" answer ("saves a round trip" — singular) when the actual answer was 4 seconds. Reasoning is consistently ahead of math execution under pressure. Reinforce on every numeric question: write each step, give the actual number, sanity-check magnitude.
- **Notes formatting standard (locked in 2026-04-08):** All section notes now follow `#` for file title, `##` for major sections, `###` for sub-sections, **bold** reserved for vocabulary/emphasis only — never for section markers. Code blocks always fenced with language tag. Apply same standard going forward when creating or editing notes in any section.
