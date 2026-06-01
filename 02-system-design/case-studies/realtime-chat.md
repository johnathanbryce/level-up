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

### HTTP Endpoints (REST)

| Method | Endpoint | Purpose |
|--------|----------|---------|
| `GET` | `/conversations` | Inbox / sidebar — list user's conversations, paginated. |
| `GET` | `/conversations/:id/messages?before=<msg_id>&limit=50` | Message history fetch (paginated, scrolling backward). Hits Redis cache first → DB on miss. |
| `POST` | `/conversations` | Create new conversation (body: member user_ids, optional name). |
| `POST` | `/conversations/:id/messages` | **HTTP fallback** for sending — used when the WebSocket isn't connected. Primary send path is the WebSocket (see below). |
| `DELETE` | `/conversations/:id` | Leave or delete conversation. (Individual message unsend = v2 — correctly flagged as too granular for first pass.) |
| `POST` | `/auth/login` | Issues JWT. |
| `GET` (upgrade) | `/ws` | WebSocket upgrade endpoint — opens the persistent connection. |

### WebSocket Events

The WebSocket is the **primary channel** for live messaging. Once the client connects, events flow bidirectionally over the open socket — no HTTP overhead per message.

**Client → Server:**
- `message.send` — `{ conversation_id, text, client_msg_id }` where `client_msg_id` is a UUID the client generates for idempotency (if the client retries on network blip, server dedupes by this key).
- `presence.update` — `{ status: "typing" | "online" }` (optional in v1; typical v2 feature).
- `ack` — acknowledges receipt of a server-pushed event (for delivery confirmations).

**Server → Client:**
- `message.received` — `{ conversation_id, message_id, sender_id, text, timestamp }` — the live-pushed new message arriving from someone else in the conversation.
- `message.sent` — `{ client_msg_id, server_msg_id, timestamp }` — confirms the client's send was persisted and echoes the server-assigned `message_id`.
- `presence.update` — `{ user_id, status }` (optional v1).

### Authentication

- **HTTP requests:** JWT bearer token in `Authorization: Bearer <token>` header (standard pattern).
- **WebSocket:** token passed during the connection upgrade — either as a query parameter (`/ws?token=...`) or as the first message after the upgrade handshake. The chat server validates the token, looks up the user_id, and binds the WebSocket connection to that user for its lifetime.
- **Refresh tokens:** short-lived JWT (15-60 min) + refresh token for renewal — standard pattern, scoped out of v1 design discussion.

### Sticky sessions — refinement on initial instinct

John's instinct in the live discussion was to add sticky sessions to HTTP requests too. Small clarification:

- **WebSocket connections are inherently sticky.** A WebSocket is a long-lived TCP connection to ONE chat server — the LB hands the client off and the connection stays pinned for its lifetime. No special "sticky session" config needed at the LB; it's a property of the protocol.
- **HTTP requests do NOT need sticky sessions.** They're stateless — any chat server can serve any HTTP request as long as it can read the DB / Redis. Round-robin or least-connections LB is fine.
- Sticky sessions as a config flag matter for OLD-style server-stores-session-on-local-disk apps. Modern chat = stateless HTTP + stateful WebSocket-on-its-own-server.

### Why messages flow over WebSocket, not HTTP POST

Mid- to senior-flavor trade-off worth knowing:

- **WebSocket bidirectional** (send + receive over WS): primary path for Slack/Discord/web chat. Lower latency, reuses the open connection, no HTTP handshake overhead per message.
- **HTTP POST + WebSocket receive** (send via POST, receive via WS): some mobile apps, and the fallback path when WS isn't connected. HTTP overhead per send but resilient to dropped WS connections.

**For our design:** WebSocket bidirectional is the primary path. HTTP POST `/conversations/:id/messages` is the fallback for clients without an active WS (e.g., reconnecting, mobile background).

---

## Phase 4 — Architecture

### Components (edge → persistence)

1. **Clients** (browser / mobile) — hold 1 persistent WebSocket + HTTP for non-real-time ops (history fetch, inbox, conversation creation).
2. **Load Balancer** (separate component from API Gateway):
   - **WebSocket connections: least-connections algorithm.** NOT round-robin — round-robin distributes new connection counts equally but ignores that WS connections are LONG-LIVED, so a server accumulates disproportionate active connections over time. Least-connections accounts for current load.
   - **HTTP requests: round-robin or least-connections both fine** (requests are short-lived, stateless).
3. **API Gateway** (separate from LB) — handles JWT auth validation, rate limiting, HTTP request routing. Sits behind the LB. WebSocket connections typically auth at the upgrade handshake and then bypass the gateway for subsequent WS frames (one less hop per message — important at chat scale).
4. **Chat Server Pool (~50-100 instances)** — the workhorse layer. Each server:
   - Holds ~20K concurrent WebSocket connections.
   - Subscribes to pub/sub channels for the conversations of its connected users.
   - Validates inbound messages, writes to DB, publishes to pub/sub, pushes outbound messages to its connected clients.
5. **Pub/Sub Broker** (Redis Pub/Sub for v1; Kafka for production-scale) — the **fanout middleware**. This is the load-bearing piece that lets servers talk to each other. Without it, every chat server would need a direct connection to every other chat server (full mesh = doesn't scale).
6. **Redis Cache Cluster (5-8 nodes)** — recent messages per `conversation_id`, user inbox lists. Sharded by `conversation_id` (consistent hashing).
7. **Persistence — polyglot (senior call):**
   - **Postgres** (1 primary + 2 read replicas): `users`, `conversations`, `conversation_members`. Relational metadata, low write volume, JOIN-friendly.
   - **Cassandra cluster (5-8 nodes, RF=3)**: `messages`. Write-heavy, time-series, sharded by `conversation_id`.

### Architecture Diagram

```
                    Clients (browser / mobile)
                              │
                              │  HTTP + WSS
                              ▼
                       ┌─────────────┐
                       │     LB      │   least-conn for WS,
                       │             │   round-robin for HTTP
                       └──────┬──────┘
                              │
                ┌─────────────┴─────────────┐
                │                           │
              (HTTP)                  (WS upgrade)
                │                           │
                ▼                           │
         ┌─────────────┐                    │
         │ API Gateway │                    │
         │ (auth, rate │                    │
         │  limit,     │                    │
         │  routing)   │                    │
         └──────┬──────┘                    │
                │                           │
                └────────────┬──────────────┘
                             ▼
                  ┌──────────────────────┐
                  │  Chat Server Pool    │ ◄──────┐
                  │  (50-100 instances)  │        │
                  │  - holds WS conns    │        │
                  │  - publishes/subs    │        │
                  │    to fanout broker  │        │
                  └──┬───┬───┬───┬───────┘        │
                     │   │   │   │                │
                     │   │   │   └──► Pub/Sub Broker ──┐
                     │   │   │       (Redis / Kafka)   │ (notifies
                     │   │   │                          │  other
                     │   │   │                          │  chat
                     │   │   └──► Redis Cache           │  servers)
                     │   │       (recent msgs,          │
                     │   │        inbox)                │
                     │   │                              │
                     │   └────► Cassandra ◄─────────────┘
                     │         (messages,
                     │          sharded by
                     │          conversation_id,
                     │          RF=3)
                     │
                     └────► Postgres
                           (users, convos,
                            members,
                            primary + 2 replicas)
```

### Data Model

**Postgres (relational metadata):**

```sql
-- users
user_id        BIGINT PRIMARY KEY
display_name   TEXT
avatar_url     TEXT
created_at     TIMESTAMP

-- conversations
conversation_id BIGINT PRIMARY KEY
type            VARCHAR(10)    -- 'direct' | 'group'
name            TEXT           -- nullable for direct chats
created_at      TIMESTAMP

-- conversation_members (composite key)
conversation_id  BIGINT
user_id          BIGINT
joined_at        TIMESTAMP
last_read_msg_id BIGINT        -- for unread counts
PRIMARY KEY (conversation_id, user_id)
INDEX ON (user_id, conversation_id)  -- supports "all my conversations" query
```

**Cassandra (messages — write-heavy, time-series):**

```cql
CREATE TABLE messages (
    conversation_id BIGINT,     -- partition (shard) key
    message_id      TIMEUUID,   -- clustering key (sort order)
    sender_id       BIGINT,
    text            TEXT,
    client_msg_id   UUID,       -- idempotency key for retry dedup
    created_at      TIMESTAMP,
    PRIMARY KEY (conversation_id, message_id)
) WITH CLUSTERING ORDER BY (message_id DESC);
```

**Key design decisions:**
- **`conversation_id` as Cassandra partition key**: all messages in a conversation land on the same shard. "Last 50 messages in conversation X" = single-shard scan, no scatter-gather.
- **`message_id` as TIMEUUID clustering key**: messages auto-sort by time within a partition. Latest-first scroll = sequential read.
- **`client_msg_id`** is the **idempotency key** — if the client retries a send (network blip), server dedupes by this UUID. Same pattern locked from Resilience review, applied to chat-specific surfaces.
- **Polyglot persistence** is a senior decision: Cassandra excels at write-heavy time-series (messages) but is overkill for low-volume relational data (users, conversations, members). Postgres handles those better with cleaner JOINs.

### Live-Message Flow — Alice sends "hello" to a group chat with Bob and Carol

The canonical end-to-end walkthrough. Memorize the steps:

1. **Alice's client** emits `message.send` over her WebSocket to **ChatServer-7** (her pinned server from connect-time).
2. **ChatServer-7** processes:
   - **(a) Validate** Alice's membership in the conversation (Redis lookup → Postgres fallback on miss).
   - **(b) Idempotency check** — query for `client_msg_id` in recent messages. If found, return the existing `message_id` without rewriting.
   - **(c) Write to Cassandra** — persist the message, get back the server-assigned `message_id` (TIMEUUID). **This must complete before fanout — messages must be durable BEFORE we tell anyone they exist.**
   - **(d) Publish to pub/sub** — emit event to channel `conversation:{conversation_id}` carrying the full message payload.
   - **(e) Update Redis cache** — append to the cached recent-messages list for this conversation.
   - **(f) Send `message.sent` ack** back to Alice's WebSocket with the assigned `message_id`.
3. **Pub/sub broker** fans out the event to ALL chat servers subscribed to that conversation's channel.
4. **ChatServer-3** (Bob's pinned server) and **ChatServer-12** (Carol's pinned server) receive the published event.
5. Each looks up the WebSockets for the conversation's members it has connected and pushes `message.received` down those sockets.
6. **Bob and Carol see "hello"** appear in their UI in real time.

**Latency budget:** WebSocket hop (~10ms) + Cassandra write (~5-20ms) + pub/sub fanout (~5ms) + WebSocket push to recipients (~10ms) ≈ **30-50ms end-to-end** under normal conditions. p99 SLA target: < 500ms.

### Consistency model (final)

- **Within a single conversation:** strong ordering required. Server-assigned TIMEUUID `message_id` enforces global per-conversation order; all members see messages in the same sequence.
- **Globally across conversations:** eventual consistency is fine. Sidebar/inbox reordering 200ms late is not a bug.
- **CAP positioning:** AP (availability + partition tolerance). For chat, sub-500ms delivery matters more than strict global consistency — the right trade-off.

---

## Phase 5 — Deep Dives (pick 2)

**OMITTED 2026-06-01** per section close restructure. Cold-case-study practice happens at the End-of-Section Capstone Part 2 with a fresh prompt — pattern repetition here would have low marginal value.

---

## Phase 6 — Trade-offs & Failure Modes

**OMITTED 2026-06-01** per section close restructure. Trade-off articulation and failure-mode analysis is part of Capstone Part 3 rapid-fire defense.

---

## Debrief

### What went well

- **Polyglot persistence + shard-key instincts.** `conversation_id` as Cassandra partition key called correctly without prompting (2nd consecutive correct shard-key call across surfaces, carrying over from DB Architecture review). Four required tables (users, conversations, conversation_members, messages) named cleanly.
- **TTL + jitter on Redis cache** reached for at the right moment for the right reason (synchronized expiration → thundering herd).
- **Honest "I don't know" on WebSocket events** (Phase 3). Senior move, named explicitly — beats confident-wrong.
- **Honest mid-session fatigue call** at the Phase 4 mark. Asked for honest mentor assessment rather than grinding, leading to the restructured section close. Pushback track record stays at ~100%.
- **Senior-flavor pruning instinct** on individual message unsend ("too granular for v1") — correctly scoped to conversation-level only.

### What fumbled (logged to Section 2 Surfaced Gaps)

1. **Webhooks vs WebSockets vocab confusion** (NEW gap). Phase 1. Corrected; retest at Capstone Part 3 rapid-fire to confirm locked.
2. **Gateway vs LB conflation — 2nd occurrence within this single case study** (Phase 1 + Phase 4 verbal). Phase 1 corrected; Phase 4 verbal still merged them. Joins the recurring "layer conflation" pattern from the section log (also: auth ≠ method, CDN ≠ app, consistent hashing ≠ session stickiness). **Tier 1 Capstone Prep.**
3. **Write-pattern drift.** Phase 1 corrected "write-behind" to "DB-first → publish → cache"; Phase 4 verbal collapsed it back to "write-through updates Redis AND DB simultaneously." The DB-first-for-durability reflex isn't locked. Same family as the 2026-04-14 + 2026-05-07 stampede/write-pattern gaps. **Tier 1 Capstone Prep.**
4. **Node counts from vibes.** "At least 3" both times for Postgres and Redis. Corrected to 5-8 derived from footprint math. **Drill at Capstone: defend every node count with the math.**
5. **Consistency framing too loose.** "Eventual everywhere" instead of "strong within a conversation + eventual globally." Refined twice in this artifact; lock at Capstone.
6. **Live-message flow walkthrough not produced under verbal pressure** (Phase 4). I asked for the end-to-end walkthrough; John talked components instead. This is the #1 chat-system interview deliverable. **Cold-retest at Capstone Part 2.**
7. **Pub/sub layer omitted in Phase 4 verbal recall** despite being taught in Phase 1. Architecture-retrieval-under-pressure pattern — same shape as Stage 5 diagnostics 2026-04-27 (material in notes, doesn't surface verbally).

### Carries to Capstone

Capstone Part 2 (cold case study) and Part 3 (rapid-fire) are where these fumbles get retested. No dedicated Capstone Prep session per restructured close — the gate IS the test.
