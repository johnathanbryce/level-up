# Case Study #2 — Real-time Chat System

**Date:** 2026-06-01
**Mode:** collaborative learning (NOT cold-interview). John writes initial thinking, Claude teaches/refines/corrects in place, we co-design the artifact. Cold-interview mode is reserved for the Capstone.
**Format rule:** single source of truth — edit in place. No "his answer / interviewer answer" sub-sections. Loose Notes-style content inside each phase is fine.

---

## Phase 1 — Requirements & Scope

### Questions:
1. How many users are we expecting? Do we have total averages or any indication QPS? 
2. Do we allow image or file sharing, or is this strictly text-only messages? 
3. Do we allow group chats? 
4. How long should we keep message histories? 

### Interviewer's Answers

1. **Scale.**
   - 10M DAU.
   - Avg 20 messages sent/user/day → ~200M messages/day total.
   - Read:write ≈ 10:1 (people read way more than they send — open a chat, scroll, glance at notifications).
   - Peak ~3x average.

2. **Image/file sharing.**
   - Text-only for v1.
   - Files / images explicitly out of scope. (Scopes out S3 + CDN + thumbnailing pipeline — big simplification.)

3. **Group chats.**
   - Both 1:1 AND group.
   - Max group size = 100. (Slack-channel scale, not Discord-server scale. 10K-member groups would force a completely different fanout strategy — out of scope v1.)

4. **Message history.**
   - *Punted back to candidate.* Pick a value AND defend it. ("Forever" and "7 days" have very different storage/cost profiles. Most consumer chat products land somewhere in between or use tiered storage.)

### Notes (collaborative design pass — high-level approach for Phase 2)

**Real-time delivery mechanism (the core of chat):**
- WebSockets, not webhooks. Each client holds 1 persistent WebSocket to a chat server.
- Users in the same conversation are connected to DIFFERENT chat servers (LB distributes randomly), so we need a pub/sub layer between servers to fan out messages. Full mechanism in Phase 4.

**Caching (read path):**
- 10:1 reads:writes correctly points at Redis caching ✓
- Cache recent N messages per `conversation_id` (not "the whole chat" as a blob — every new message would invalidate the whole blob).
- WebSocket = live messages only. Opening a chat / scrolling history = HTTP + Redis + DB.

**Write path (correction from initial notes):**
- Write-behind is WRONG for chat. If the cache crashes before flushing to DB, the message is lost. Messages must be durable.
- Correct pattern: write to DB first → publish to pub/sub for fanout → update cache. Closer to write-through.
- Write-behind is for things you can afford to lose a few seconds of (leaderboard scores, view counts). Not messages.

**Consistency (refinement from initial notes):**
- Within a conversation: strong ordering required (Alice 10:00 → Bob 10:01 must arrive in that order for every member). Server-assigned sequence numbers per `conversation_id` enforce this.
- Globally: eventual consistency fine (sidebar/inbox reordering 200ms late is not a bug).

**Storage:**
- Postgres sharded by `conversation_id` is defensible — and `conversation_id` is the right shard key (carry-over from DB Architecture review ✓). Distributes load AND keeps all messages in a conversation co-located on one shard (no scatter-gather on reads).
- Cassandra is the classic chat-system answer: write-optimized, time-series friendly, tunable consistency. Worth naming as the senior-flavor alternative in interviews.
- Real shard count comes from Phase 2 estimation (not "at least 3" from vibes).

**Gateway vs LB (clarification):**
- API gateway = auth + rate limiting + routing.
- Load balancer = distributes connections across server pool.
- Two separate components in production architectures. Typical flow: client → LB → gateway → chat servers. The WebSocket layer often skips the gateway (LB → chat servers directly) to avoid an extra hop on a long-lived connection.

**Message history retention (punted Q4 decision):**
- Locked at **1 year of hot storage** for Phase 2 estimation purposes. Realistic for a chat product (WhatsApp/Slack default to long history; older messages tiered to cold S3-style storage in production).

**Decision summary going into Phase 2:**
- 10M DAU, ~1-2M concurrent, ~200M messages/day, peak 3x
- Text-only, 1:1 + group chat (max 100), 1yr hot retention
- WebSockets + pub/sub fanout for live delivery
- Redis cache (recent messages per conversation_id)
- Sharded DB (Postgres or Cassandra — count from estimation)



---

## Phase 2 — Estimation

*(reason in order-of-magnitude. Approximate magnitudes only — interviewers don't expect exact byte-counting.)*

### DAU + activity
- 10M DAU; ~1-2M concurrent (10-20% online at any given moment) — this IS the peak concurrent figure already (not avg).
- Avg 20 messages sent/user/day → ~200M messages/day total (writes).
- Reads at 10:1 ratio → ~2B reads/day (chat opens, scrolls, glance-and-close).
- Peak message throughput = 3x average (rush hours: morning commute, lunch, evening). Peak applies to **messages/sec**, not concurrent users.

### QPS
- Use the ~100K-seconds-per-day shortcut (86,400 rounded up) — common system-design napkin math.
- **Writes:** 200M / 100K = 2,000 msg/sec avg → peak ~6,000/sec.
- **Reads:** 2B / 100K = 20,000/sec avg → peak ~60,000/sec.
- **Total:** ~22K QPS avg, ~66K QPS peak. Reads dominate — Redis cache earns its keep.

### Storage
- **Per-message size:** ~140 bytes for text payload (SMS-comparable), plus ~50-60 bytes of metadata (sender_id, conversation_id, timestamp, message_id) → ~200 bytes/message all-in.
- **Yearly:** 200B × 200M × 365 ≈ **15 TB raw**. With indexes (+30-50%) → **~20 TB hot storage / year.**

- **DB choice (refined):** Cassandra is well-suited (write-heavy, time-series, tunable consistency). BUT: Cassandra is NEVER run as a single node in production — its scale-out story IS the distribution. Typical small chat cluster = **5-8 nodes at RF=3** (replication factor 3 = each row stored on 3 nodes for fault tolerance). Sharded by `conversation_id`. Postgres-sharded is also defensible — Cassandra is the senior-flavor pick.

- **TTL good instinct ✓** — Cassandra has native per-row TTL. BUT in production chat, you don't usually DELETE old messages; you TIER them to cold S3-style storage. (Some users care about year+ history; deletion is a product call.) For v1 design: 1 year hot in Cassandra, older messages tiered to S3 (cold path, slower retrieval, rarely accessed).

- **Redis cache sizing:**
  - Cache pattern: last ~100 messages per active conversation_id (NOT the whole chat).
  - Active conversations on any day ≈ 10-30M (rough — from 10M DAU each touching multiple chats).
  - Per conversation: 100 messages × ~200 bytes = ~20 KB.
  - Total: 10M conversations × 20 KB ≈ **~200 GB cache footprint.**
  - **~5-8 Redis nodes** at 32-64 GB RAM each, sharded by `conversation_id` (consistent hashing). NOT 3 — that's pulled from vibes; the math says 5-8.
  - TTL: 12hr on inactive conversations, refresh on access. Jitter applied ✓ (good — prevents synchronized expiration storm).

### Bandwidth
*(Bandwidth = data volume per second, NOT latency. Latency is a non-functional req, moved to Phase 6.)*
- **Inbound** (clients sending messages): 200M × 200B / 100K sec ≈ **400 KB/sec avg, ~1.2 MB/sec peak.**
- **Outbound** (fanout to recipients): each message is delivered to potentially many recipients. If avg conversation has ~5 active recipients, outbound = 5x inbound → ~**6 MB/sec peak.**
- **Total:** under 10 MB/sec at peak. Trivially modest on modern infra.
- **Takeaway:** for text chat, bandwidth is NOT a constraint. The binding constraints are **connection count** (1-2M concurrent WebSockets) and **message throughput** (6K writes/sec peak). Bandwidth matters for image/video systems, not text.

### Sizing summary going into Phase 3
- **~22K QPS avg / 66K peak** (reads dominate ~9:1)
- **~50-100 chat servers** (for 1-2M concurrent WebSocket connections, ~20K connections/server)
- **5-8 Cassandra nodes** (~20 TB hot, sharded by conversation_id, RF=3)
- **5-8 Redis nodes** (~200 GB cache, sharded by conversation_id)
- **Pub/sub broker** for fanout (Redis Pub/Sub or Kafka — sized in Phase 4)
- Bandwidth is not a constraint

---

## Phase 3 — API Design

---

## Phase 4 — Architecture

### Components

### Data model

### Data flow

---

## Phase 5 — Deep Dives (pick 2)

---

## Phase 6 — Trade-offs & Failure Modes

---

## Debrief

*(populated at end of session)*
