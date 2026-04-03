# System Design Fundamentals — Progression Tracker

## Overview

The foundational section that everything else builds on. Covers core infrastructure concepts, architecture patterns, and the ability to reason about trade-offs verbally. This section is conceptual + diagramming + verbal practice, with some hands-on exercises where they reinforce understanding.

## Definition of Done

Can whiteboard a system, explain where it breaks first, justify every component choice, and discuss trade-offs without fumbling. Can answer "why not X instead?" for any architectural decision.

---

## Sub-Topics

### Internet & Networking Fundamentals

Foundational knowledge that interviewers expect you to explain cold. "What happens when you type a URL in your browser?" is a classic interview question that touches all of these.

- [ ] How the internet works: IP addresses, TCP vs UDP, ports, packets (high-level, not networking-engineer depth)
- [ ] What is DNS — how domain name resolution works, DNS caching, TTL, recursive vs iterative lookup
- [ ] What is HTTP — request/response cycle as a protocol, headers, methods, versions (HTTP/1.1 vs HTTP/2 vs HTTP/3 awareness)
- [ ] What is HTTPS/TLS — what TLS does, how the handshake works (conceptual), certificates, why it matters
- [ ] Web request lifecycle (DNS → TCP → TLS → HTTP → server → response) and latency at each stage
- [ ] WebSockets — what they are, how they differ from HTTP, persistent connections, when to use them (real-time chat, live updates)
- [ ] SSH — what it is, how it works (conceptual), key-based auth vs password

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
- [ ] Polyglot persistence — using the right DB for each job

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
| — | — | — | — |

---

## Notes & Weak Spots

- (none yet)
