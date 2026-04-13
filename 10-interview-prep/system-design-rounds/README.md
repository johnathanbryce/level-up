# System Design Rounds

Full system design simulation prompts. These are bigger than mini-challenges — each is a 45-60 minute round where John walks through a complete design end-to-end (assumptions → estimation → high-level architecture → component deep dives → trade-offs → bottlenecks).

**Use these AFTER Section 2 (System Design Fundamentals) is mostly complete.** Earlier-stage use is fine for individual sub-questions ("just do the estimation step on this prompt") but a full round needs the foundations.

---

## The Round Structure (use this for every question below)

1. **Clarify (3-5 min):** Ask about scale, key features, constraints, success metrics. Don't assume.
2. **Estimate (3-5 min):** QPS, storage, bandwidth. Translate to architectural implications.
3. **High-level diagram (5-10 min):** Major components, data flow, where state lives.
4. **Component deep-dive (15-25 min):** Pick 2-3 components and go deep on schema, API design, scaling, failure modes.
5. **Bottlenecks & trade-offs (5-10 min):** Where does this break first? What would you change at 10x scale?
6. **Wrap (2 min):** What you'd build first, what you'd defer.

---

## The Classic Five (start here)

### 1. Design a URL shortener
The "design Twitter" of warmups — shows up at almost every interview. Practice it until it's reflexive.
- **Key challenges:** ID generation strategy (random vs counter vs hash), read-heavy ratio, cache strategy, custom aliases, analytics.

### 2. Design a real-time chat system
- **Key challenges:** WebSocket connections at scale, message ordering, delivery guarantees, online presence, message history storage, group chats vs DMs.

### 3. Design a rate limiter
- **Key challenges:** Algorithm choice (token bucket, sliding window, leaky bucket), distributed coordination (Redis), per-user vs per-IP vs per-API-key, what to do when the limiter itself goes down.

### 4. Design a social media feed (Instagram-like)
- **Key challenges:** Fan-out on write vs fan-out on read (push vs pull), celebrity problem, ranking, image storage, caching strategy, infinite scroll pagination.

### 5. Design a notification system
- **Key challenges:** Multi-channel (push, email, SMS), deduplication, user preferences, delivery guarantees, scheduling, throttling.

---

## Tier 2 — Common follow-ups

### 6. Design a video streaming service (YouTube-lite)
- **Key challenges:** Storage scale (massive), CDN, transcoding pipeline, adaptive bitrate, view counts at scale.

### 7. Design a ride-sharing matching system (Uber-lite)
- **Key challenges:** Geospatial indexing (geohash, quadtree), driver location updates at scale, matching algorithm, surge pricing.

### 8. Design a search autocomplete
- **Key challenges:** Trie data structure, top-K queries, real-time updates, personalization.

### 9. Design a distributed cache
- **Key challenges:** Consistent hashing, replication, eviction policies, hot key problem.

### 10. Design a job/task queue
- **Key challenges:** At-least-once delivery, dead-letter queues, retry strategies, prioritization, worker scaling.

---

## AI-flavored rounds (for the AI engineer angle)

### 11. Design a RAG-powered customer support assistant
- **Key challenges:** Document ingestion pipeline, embedding storage and refresh, retrieval quality, citation, hallucination handling, cost per query, evaluation.

### 12. Design an LLM API gateway
- **Key challenges:** Routing across providers, fallbacks, caching, rate limiting per tenant, cost tracking, streaming responses.

### 13. Design a vector search service for 100M embeddings
- **Key challenges:** ANN index choice (HNSW), sharding strategy, query latency targets, hybrid search integration, index updates.

---

## Notes on usage

- **Don't memorize answers.** The point is the process — clarifying questions, estimation reasoning, trade-off articulation. Two correct answers can look very different.
- **Practice out loud or in writing.** System design rounds are a verbal performance, not a code-writing exercise.
- **Have Claude play interviewer.** Push back on assumptions, ask "what about X?", and grade the answer at the end. Don't accept your own first draft.
- **Web-research the actual scale numbers** for big systems before you do them. Knowing "Twitter has ~500M tweets/day" makes your estimation feel grounded.
