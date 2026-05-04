# System Design — Interview Question Bank

Running list of quiz questions from per-section reviews, with canonical answers only. Use for active-recall practice before interviews — re-quiz yourself periodically. Recognition is not recall.

---

## Section 1: Request Lifecycle

### Q1.1 — DNS resolution path on a fresh browser session

**Question:** Walk through the DNS resolution path from keystroke to "I now have the IP." Be specific about cache order AND what happens on full cache miss.

**Answer:**

The chain has two halves: a **cache layer in front** (fast path) and a **hierarchy walk behind** (slow path).

**Cache layer (in order):**
1. Browser cache
2. OS cache
3. Router cache
4. Recursive resolver cache (typically your ISP, or a public resolver like Cloudflare 1.1.1.1)

**If all four caches miss, the resolver walks the hierarchy:**
- **Root nameservers** → "I don't know `caseway.app`, but here's who handles `.app`"
- **TLD nameservers** (`.app`, `.com`, etc.) → "Here's the authoritative nameserver for `caseway`"
- **Authoritative nameserver** → "Here's the actual IP for `caseway.app`"

The IP is returned and **cached at every layer on the way back**, respecting each layer's TTL.

---

### Q1.2 — TCP or UDP for multiplayer game position updates?

**Question:** A multiplayer browser game sends player position updates ~30 times/sec. Pick TCP or UDP, explain why, name another protocol that uses the same one for the same reason.

**Answer:**

**UDP.**

**Why:** A retransmitted position from 200ms ago is useless because the player has already moved — newer data has arrived. TCP would block the line waiting for the retransmit, making fresh data wait behind already-stale data. UDP drops the missing packet and moves on.

The mental model: **stale data is worse than missing data.** The freshness is the point, not the precision.

**Same reasoning, different protocol:** **DNS queries.** Small payload, latency-sensitive, single request/response. The cost of TCP's three-way handshake (1 RTT just to set up) is more expensive than just firing a UDP packet and retrying from the application layer if it drops.

(Also valid: live video/voice calls, WebRTC, online streaming, IoT telemetry.)

---

### Q1.3 — "Your connection is not private" warning

**Question:** A user reports "Your connection is not private — can't get past the warning page." What protocol layer is failing? Name three causes. Is traffic encrypted while the warning is shown?

**Answer:**

**Protocol layer:** **TLS** is failing — specifically **cert validation**.

**Three causes (any three of these):**
1. Cert **expired**
2. Cert issued by an **untrusted CA** (self-signed or unknown issuer)
3. **Hostname mismatch** — cert is for `example.com` but accessed `www.example.com`
4. **Clock skew** on user's device (system clock wrong → valid cert appears expired)
5. Cert **revoked**

**Encryption status during the warning:**

The handshake actually **completes** — cert is received, validation fails, browser blocks the page. **If the user proceeds anyway: traffic IS encrypted, but server identity is unverified** → vulnerable to MITM attack. The warning fires *because* validation failed, not because no encryption is happening.

**Interview one-liner:** *"The warning fires after a partial TLS handshake — cert was received but failed validation. Traffic is encrypted if the user proceeds, but the server's identity isn't trusted, which is the whole problem TLS was supposed to solve."*

**NOT triggered by:** plain HTTP (just "Not Secure" badge in URL bar, no warning page) or connection refused (different error entirely).

---

### Q1.4 — GET-as-DELETE: what specifically breaks?

**Question:** A junior dev exposes `GET /admin/users/123/delete`. Name three concrete real-world failures this design produces. Be precise — "GET shouldn't modify state" is the rule, not the consequence.

**Answer (six canonical failure modes):**

1. **Browser prefetch / link previews** — browsers proactively fetch URLs (hover prefetch, prerender hints). User mouses over the link → user deleted, no click required. Slack/Discord/iMessage previews of pasted URLs fire the delete.

2. **CDN / proxy caching** — GETs are cacheable by default. The CDN may cache the delete response — second user gets a cached "200 OK" that never reached the app server. Or the first delete result gets served from cache forever, never re-executing.

3. **Browser back / refresh / share** — URL is in history, bookmarkable, shareable. Page back → delete fires again. URL pasted in chat → recipient clicks → another user deleted.

4. **CSRF amplification** — standard CSRF tokens only protect POST/PUT/DELETE. GET sails through. Attacker embeds `<img src="https://your-site.com/admin/users/123/delete">` in any webpage; logged-in admin visits → silent delete via session cookie.

5. **Crawlers / search bots / LLM scrapers** — Googlebot, security scanners, LLM training crawlers, link checkers all auto-fire GETs on every link they discover.

6. **Logging leakage** — GET URLs are written to server access logs, proxy logs, browser history, analytics, and Referer headers. User IDs and the action itself leak into systems with looser access controls than the database.

**Critical framing:** auth and method choice are **orthogonal concerns**. POST with no auth has the same authorization problem; only GET gets prefetched, cached, embedded as `<img>`, or replayed by crawlers. The whole web ecosystem assumes GET is safe — violating it weaponizes the ecosystem against your data.

---

### Q1.5 — Page latency spike: where do you look?

**Question:** Page-load latency spiked from 200ms to 4 seconds in production. Walk diagnostic order through the request stack (LB → app → cache → DB) with one specific signal per layer.

**Answer:**

| Layer | Specific Signal | Diagnostic Question |
|---|---|---|
| **Load Balancer** | Connection rate, 5xx rate at LB layer specifically (vs at app), backend pool health checks | *Is the LB dropping/queuing requests before they reach the app?* |
| **App Server** | Worker pool exhaustion, request queue depth, CPU/memory saturation, slow downstream call duration | *Is the app CPU-bound, IO-bound, or starved (workers all blocked)?* |
| **Cache** | **Cache hit rate** (single most important metric). Hot key, eviction rate, Redis CPU. | *Did hit rate drop? If it went 95% → 40%, the DB just became the bottleneck even though the DB itself is fine.* |
| **Database** | Slow query log, connection pool utilization, query duration p95, replica lag, lock contention | *Did a query plan change, or did a previously-cached read become uncached because the cache failed?* |

**Interview one-liner:**

> "I'd walk the request path layer by layer. At the LB: connection rate and 5xx — is it the LB itself? At the app server: worker pool exhaustion and request queue — are workers blocked on a slow downstream? At the cache: hit rate — if that dropped, the DB just became the bottleneck even though the DB itself is fine. At the DB: slow query log and connection pool — what got slow and is the pool exhausted?"

---

### Q1.6 — Three scripts in `<head>`: which loading strategy?

**Question:** A landing page has these three scripts in `<head>`:
- `analytics.js` — fire-and-forget tracking pixel, no DOM dep
- `hero-animation.js` — runs on `DOMContentLoaded`
- `form-validator.js` — depends on `hero-animation.js` to init a form widget

(a) Pick `default` / `async` / `defer` for each.
(b) What breaks if all three are async?

**Answer:**

**(a) Loading strategies:**
- `analytics.js` → **`async`**. Independent, no DOM dep, fire-and-forget. Textbook async use case.
- `hero-animation.js` → **`defer`**. Downloads in parallel with parsing, executes after DOM is fully parsed but just before `DOMContentLoaded` — exactly when hero-animation needs to run.
- `form-validator.js` → **`defer`**. Order matters (depends on hero-animation), and defer guarantees scripts execute in document order.

**Pattern recognition:** `hero-animation` + `form-validator` is the canonical defer use case — a base library and something that depends on it (e.g. jQuery + a jQuery plugin).

**(b) What breaks with all-async:**
1. **No execution order guarantee.** Async scripts run as soon as they download — fastest network response wins. If `form-validator.js` downloads before `hero-animation.js` → it runs first → reference error / widget initialization fails because hero-animation isn't ready.
2. **Race against `DOMContentLoaded`.** If async loads `hero-animation.js` AFTER the event has already fired, `addEventListener('DOMContentLoaded', ...)` registers a listener for an event that already passed → animation never fires.

**Two-sentence answer:** *"async breaks the ordering guarantee — form-validator could execute before hero-animation has initialized, breaking the dependency. And async can race past DOMContentLoaded, so any listener registered after the event fires is dead."*

---

## Section 2: Internet & Networking Fundamentals

### Q2.1 — Ports

**Question:** What's the valid port range? Name three well-known ports. Can two processes on the same host listen on the same port simultaneously?

**Answer:**

**Range:** **0–65535** (16-bit). Three rough tiers:
- **0–1023** — well-known / system ports (need root to bind on most OSes)
- **1024–49151** — registered ports (assigned to specific apps)
- **49152–65535** — ephemeral / dynamic (used by clients for outgoing connections)

**Three well-known ports (table-stakes):** 80 HTTP, 443 HTTPS, 22 SSH. Other commonly-tested: 53 DNS, 25 SMTP, 5432 Postgres, 3306 MySQL, 6379 Redis.

**Two processes on the same port:** **No.** Port binding is **exclusive**. The first process to `bind()` a port owns it; any second process gets `EADDRINUSE` ("address already in use") and fails. The OS doesn't time-share ports between processes.

(Caveat for senior follow-ups: Linux `SO_REUSEPORT` lets multiple processes explicitly share a port for load distribution — but that's an opt-in kernel feature, not implicit time-slicing.)

---

### Q2.2 — UDP for DNS: why?

**Question:** Articulate the "stale > lost" mental model for UDP use cases. Apply it: if a DNS query packet drops, what happens, and why is this better than TCP-from-the-start?

**Answer:**

**"Stale > lost" framing:** if we recover the lost packet, the recovered data WILL BE stale by the time it arrives — newer data has already arrived. The retransmit takes time → retry is useless before it even completes. UDP drops and moves on; TCP would block waiting for the retransmit, making fresh data wait behind already-stale data.

**DNS specifically — UDP is connectionless.** There IS no connection to keep valid; packets are independent.

**Failure flow when a DNS UDP packet drops:**
1. Resolver fires UDP query, sets a timeout (~few hundred ms).
2. No response arrives within timeout.
3. **The application layer (the resolver itself) retries** — possibly to a different DNS server, possibly with backoff.
4. If multiple retries fail, the resolver may fall back to **TCP** (DNS supports both — UDP for the common case, TCP for big responses or after UDP fails).

**Why faster than TCP-from-the-start:**
- No three-way handshake on every query (TCP setup = 1 RTT just to establish)
- Retry strategy is tunable at the application layer (try a different server, custom backoff, app-level fallback) instead of being locked into the kernel's TCP retransmit logic

**Interview one-liner:** *"DNS uses UDP because the application can manage its own retry strategy in milliseconds, while TCP would force a handshake on every query just for reliability that DNS doesn't need 99% of the time."*

---

### Q2.3 — SSH key-based auth in CI/CD

**Question:** You're setting up a CI/CD pipeline that runs `git clone git@github.com:your-org/repo.git` on a build server. (a) Why use key-based auth instead of password? Two specific reasons. (b) Where does the private key live? Where does the public key live? (c) What's the conceptual link between SSH key auth and something from Section 1?

**Answer:**

**(a) Two reasons for key-based in CI/CD:**

1. **Automation-friendly — no interactive prompt.** Password auth requires someone to type the password; CI/CD runs unattended (3am pipelines, scheduled jobs). Key-based auth is non-interactive: the runner uses the private key, no human in the loop.
2. **Easy revocation per machine.** One key per build server. If a build server is compromised, delete its public key from GitHub — that single machine loses access without affecting any other system.
3. (Honorable mention) **No shared secret on the wire.** The private key never leaves the client; only signatures cross. Immune to brute-force guessing or password leaks.

**(b) Where the keys live:**

- **Private key:** `~/.ssh/id_rsa` (or `id_ed25519`) on the **client** machine. NEVER shared, NEVER transmitted. In CI/CD specifically: lives on the build server as a secret (encrypted at rest, accessed by the pipeline runner).
- **Public key:** `~/.ssh/authorized_keys` on the **server** the user wants to access — one public key per line, each authorized to log in as that user. In CI/CD specifically: added to GitHub as a "deploy key" on the repo, or to a service account's SSH keys.

The build server is the *client* in this scenario (it initiates the SSH connection to GitHub). Private key on the build server; public key registered with GitHub.

**(c) Conceptual link to Section 1: TLS certificates.**

Both SSH key auth and TLS use the **same asymmetric-crypto pattern**:

- **TLS:** the server holds the private key for its cert. Browsers trust a list of CAs (public-key infrastructure). The server proves identity by signing TLS handshake data with its private key; the browser verifies with the cert's public key.
- **SSH:** the user holds the private key. The server has the user's public key in `authorized_keys`. The user proves identity by signing a server-issued challenge with their private key; the server verifies with the public key.

**Same mechanism, different problem.** Public/private key pairs + challenge/response = the foundation of *both* SSH auth and TLS server identity. Connecting these two as "same crypto, different problems" is a senior-flavor move that crystallizes both concepts.

---

### Q2.4 — WebSockets vs HTTP polling for live stock prices

**Question:** You're building a stock-trading dashboard with live price updates for users' watchlists. (a) WebSockets or HTTP polling? (b) What's the specific failure mode of using HTTP polling? (c) Is there any scenario in this product where polling would be the right call?

**Answer:**

**(a) WebSockets.** Real-time, server-pushed updates with persistent bidirectional connection.

**(b) Four canonical failure modes of HTTP polling for real-time data:**

1. **Latency floor = polling interval.** Poll every 5s → worst-case latency to see a price change is 5s. For stock trading, that's a financial gap (prices move in milliseconds, user could miss the trade).
2. **Server can't initiate.** The fundamental design difference. With polling, only the client can request; the server has no way to push fresh data. With WebSockets, the server pushes the moment an event happens — zero latency between event and notification.
3. **Wasted requests.** Poll every 1s but prices don't change for 30s → 30 round-trips of pure overhead. Bandwidth + server load scales as `users × polling frequency` even when nothing's happening.
4. **Forced trade-off between freshness and load.** Faster polling = lower latency but more waste; slower polling = less waste but worse freshness. WebSockets eliminates the trade-off.

**Interview one-liner:** *"Polling has a fundamental design problem — the server can't push, only the client can ask. So you're stuck choosing between latency and load, even when nothing's happening. WebSockets flips that — the server pushes the moment something changes."*

**(c) Yes — polling is fine for the slow-moving / event-triggered features in the same dashboard:**

- End-of-day portfolio summary — once a day, polling on page load is plenty
- News headlines / market commentary — 30-60s polling is fine
- Account balance — changes only on user action; refresh after the transaction completes
- Watchlist composition — changes only when the user adds/removes

**Pattern:** anything that changes slowly OR only changes in response to user action doesn't justify a persistent connection. Live prices = WebSockets. Everything else on this dashboard = HTTP.

**Auth note:** statelessness ≠ "needs cookies/JWT." Both HTTP and WebSockets need auth — WebSockets just checks it once at connection upgrade time instead of every request. Auth is orthogonal to protocol choice.

---

### Q2.5 — Stateless HTTP: implication chain

**Question:** A user logs in at 9:00 AM and clicks around for 30 minutes. (a) What concrete thing happens at the protocol level on EVERY click that wouldn't be necessary if HTTP were stateful? (b) Statelessness sounds inefficient — name one concrete benefit it gives you that compensates.

**Answer:**

**(a) Every request re-sends auth credentials.**

On every click, the browser re-transmits the auth cookie or JWT (in the `Authorization` header or `Cookie` header). The server validates it from scratch each time — there's no session state on the server saying "oh yeah, that's John, I remember." If HTTP were stateful, you'd authenticate once and the connection would "remember" you, skipping the per-request auth overhead.

**Interview one-liner:** *"Every request re-sends the JWT in the headers. The server validates it from scratch every time."*

**(b) The canonical benefit: HORIZONTAL SCALABILITY.**

With statelessness, **any app server can handle any request.** Spin up 10 more servers behind a load balancer, round-robin requests across them — no "session" pinned to a specific server. Add servers, traffic flows. Drop a server, the next request goes to a different one with the same JWT and it works.

If HTTP were stateful, you'd need:
- **Session affinity / sticky sessions** at the LB (route a user back to "their" server) — fragile, breaks if that server dies
- **Shared session store** like Redis — extra infrastructure, extra failure mode
- **Session replication** across servers — complex, expensive

**Other canonical benefits:**

- **Resilience to server failure** — if a server crashes mid-flight, the next request just goes to another server with the same auth token. No "lost session."
- **Easier caching** — responses can be cached at CDN/proxy level without per-user state. CDNs only work because of statelessness.
- **Eliminated bug class** — stateful systems risk per-user state bleeding across requests (race conditions, memory leaks, process-level variable bugs). Statelessness eliminates that entire bug class because there's no shared state to leak.
- **Easier debugging** — every request is self-contained and replayable in isolation.

---

### Q2.6 — DNS TTL trade-off and failover

**Question:** You're on-call. Production is down. You update your DNS A record to fail traffic over to a DR site. (a) Your TTL is 86400 (24h) — what does that mean for users? (b) What's the trade-off cost of setting TTL much lower (60s) by default — what infrastructure pays? (c) What TTL would you run in production for a typical web app API?

**Answer:**

**(a) Users could be locked into the dead site for up to 24 hours, even after you push the DNS update.**

TTL is enforced **per cache, from when that cache last fetched the record.** So:
- Worst case: a user whose cache fetched 1 minute before the outage waits the full 24 hours.
- Best case: a user whose cache fetched 23.5 hours ago refreshes in 30 minutes.
- Average: roughly TTL/2.

**Key principle:** DNS doesn't know about your incident. Your TTL is a *floor* on how fast you can recover via DNS changes.

**(b) Lower TTL → much higher query volume hitting your authoritative DNS servers.**

Every time a downstream cache expires, the recursive resolver walks back up the hierarchy to your authoritative nameservers. TTL=60s vs TTL=86400s = **1440x more queries** hitting your DNS infrastructure, scaled across every user of every resolver.

**Concrete cost:** most managed DNS services (Route 53, Cloudflare DNS, NS1) **bill per query.** Drop TTL by 1000x, your DNS bill goes up 1000x. For a high-traffic site, that's real money.

**Interview phrasing:** *"Lower TTL means more queries hit my authoritative DNS, which I pay for per-query. Faster failover comes at a literal dollar cost."*

**(c) Practical industry calibration:**

| TTL | Typical use |
|---|---|
| **60s** | High-availability APIs needing fast failover (Stripe, AWS APIs, active-active multi-region) |
| **300s (5 min)** | Default for managed services (Cloudflare, Route 53 default) — good balance |
| **3600s (1 hour)** | Stable, infrequently-changing services |
| **86400s (24h)** | Static records that essentially never change |

**Default for a typical web app's API endpoint: 300s.** Fast enough for acceptable failover, low enough query volume to not blow up your DNS bill. **60s if you anticipate failovers** (active-active multi-region setups, frequent IP changes).

**Senior-flavor calibration note:** "I don't know" beats confident-wrong. If you're outside your real-world experience, admit the calibration gap and give a defensible range — that's the senior move.

---

## Section 3: Back-of-Envelope Estimation

### Q3.1 — Estimation fundamentals: formula, 100K trick, and peak

**Question:** (a) What's the standard formula for estimating QPS from user count? (b) Why use 100,000 seconds/day instead of the actual 86,400? (c) Average QPS → peak QPS: what's the multiplier, and why is peak so much higher than average?

**Answer:**

**(a) Formula:**

```
QPS = (DAU × actions per user per day) / 100,000
```

All three terms: DAU (daily active users), actions/user/day, and the 100K denominator. Order of operations: multiply first, then divide.

**(b) Why 100K instead of 86,400:**

- Mental math simplicity: dividing by 100,000 = "shift the decimal 5 places left." No calculator needed.
- The difference is ~15%, well within napkin-math tolerance — this is order-of-magnitude reasoning, not precision.
- 100K > 86,400, so it slightly *under*-estimates QPS — acceptable.

**(c) Peak multiplier: 2-3x average.**

The mechanism: **diurnal cycle** — natural daily usage wave. Consumer apps peak in evenings (Twitter/Reddit at prime time vs 3am low); B2B apps peak weekday mornings (Slack/Zoom at 10am Tuesday vs weekend low). Peak = top of that wave; average = the 24h mean including valleys.

**Important distinction:** 2-3x describes the daily cycle, NOT event spikes. Ticket drops, Super Bowl, breaking news = 10-100x — different infrastructure strategy (pre-warmed capacity, queueing, surge pricing). Don't conflate these two cases.

---

### Q3.2 — QPS arithmetic: 5M DAU, 6 actions/day

**Question:** A meal-tracking app has 5M DAU, 6 actions/user/day. What's the average QPS? Peak QPS? Walk every step.

**Answer:**

- Total actions/day: `5,000,000 × 6 = 30,000,000`
- Average QPS: `30,000,000 / 100,000 = 300 QPS`
- Peak QPS: `300 × 3 = 900 QPS` (take the higher end of 2-3x for capacity planning)

**Capacity-planning default:** when the range is 600-900, size for **900**. Cost of over-provisioning < cost of an outage.

---

### Q3.3 — Read/write split → architecture (rule→implications)

**Question:** A blog platform has 10:1 reads:writes, 2,000 total QPS. (a) Split the QPS. (b) What specific architecture does the read-heavy asymmetry justify? (c) Why can't writes horizontally scale like reads?

**Answer:**

**(a) Ratio split:**

10:1 → 11 total parts. One part = 2,000 ÷ 11 ≈ 182 QPS.
- Reads: 10 × 182 ≈ **1,818 QPS**
- Writes: 1 × 182 ≈ **182 QPS**
- Napkin round: ~1,800 reads/sec, ~200 writes/sec.

**Ratio split mechanic:** total parts = X + Y → divide total QPS by parts → multiply each side by its share.

**(b) Canonical 3-tier read stack for content-heavy systems:**

1. **CDN at the edge** — caches rendered HTML, images, static assets near the user (Cloudflare, Fastly, CloudFront). Catches the bulk of traffic before it hits app servers.
2. **Redis cache layer** — for dynamic data that survives the CDN: comment threads, user profiles, trending posts.
3. **Read replicas** at the DB layer — N replicas behind a load balancer; only the primary handles writes.

**Consistency cost:** eventual consistency across all three layers. TTL trade-offs — longer TTL = more cache hits, more staleness.

**(c) Why writes can't horizontally scale like reads:**

| Reason | Mechanism |
|---|---|
| **Single source of truth** | Every write must hit the primary DB. Multiple DBs → which one has the latest row 123? Distributed consensus is expensive. Reads can hit any replica. |
| **Durability cost** | Writes must persist to disk (WAL + fsync), often replicated synchronously before acknowledging. Blocking. Reads have no fsync. |
| **Index updates** | Every write updates ALL indexes. 5 indexes = 5 extra writes per logical write. |
| **Lock contention** | Writes take row/page locks. Concurrent writes on the same row serialize. Reads use cheap shared locks or MVCC. |
| **Only escape: sharding** | Partition across N primary DBs by shard key. Hard: cross-shard transactions, hot shards, rebalancing. |

**Interview one-liner:** *"Reads scale by replication — copy the data, point readers at copies. Writes can't, because you'd lose your single source of truth. The only horizontal write path is sharding, with all its trade-offs."*

---

### Q3.4 — Storage estimation + unit conversion + architectural decision

**Question:** A photo app gets 2M uploads/day, average 1.5 MB each. (a) Storage per day? (b) Storage per year? (c) After 5 years, GB/TB/PB? (d) What storage system does this force, and why?

**Answer:**

**(a)** `2,000,000 × 1.5 MB = 3,000,000 MB = 3,000 GB = **3 TB/day**`

**(b)** `3 TB × 365 = **1,095 TB ≈ 1.1 PB/year**`

**(c)** `1.1 PB × 5 ≈ **5.5 PB** — solidly PB territory`

Unit ladder: 1,000 MB = 1 GB → 1,000 GB = 1 TB → 1,000 TB = 1 PB.

**(d) Object storage (S3 / GCS / Azure Blob).**

**Pattern:** *DB stores the reference, S3 stores the bytes, CDN serves the bytes.*

- DB: `photo_url` or `s3_key` column (~100 bytes/photo) — NOT binary blobs in the DB.
- S3: holds the actual photo bytes. Cheap per GB, durable (S3 = 11 9s durability), infinitely scalable.
- CDN: in front of S3 to cache hot photos at the edge.

**Trade-offs:** Higher latency than block storage (EBS) for random access; not transactional. Worth it: cost + durability + scale at PB.

---

---

## Section 4: Core Concepts

### Q4.1 — Scaling applied: where does the money go?

**Question:** Your web servers are at 85% CPU. Your database is at 35% CPU. You have $5K to spend. What do you scale, how, and why?

**Answer:** Scale only the web servers — they are the bottleneck. Scale them horizontally (add instances behind a load balancer): they are stateless, easy to parallelize, and don't require distributed state coordination. The database is at 35% CPU — there is no bottleneck there, so spend nothing on it now. Revisit the DB when it approaches its ceiling, and when it does, scale vertically first (larger instance, no architecture change) before considering read replicas or sharding. Key principle: identify the actual bottleneck before spending — only scale what is constrained.

---

### Q4.2 — CAP theorem: messaging system during a partition

**Question:** You're designing a Discord/Slack-style messaging system. A network partition occurs. Do you choose CP or AP? Walk through the reasoning.

**Answer:** AP — availability over consistency. During a partition, keep serving requests from the nodes that are up. The worst outcome is that some messages arrive slightly out of order or with a brief delay. The alternative — CP — means refusing all requests until nodes re-sync, which means users can't send messages at all. Brief staleness is always preferable to downtime for a messaging system. CP is for money, inventory, and anything where acting on stale data causes a real-world loss.

---

### Q4.3 — Strong consistency: flash sale

**Question:** Flash sale, 1 item left. Two users click Buy at the exact same millisecond from different servers. What consistency model and what is one concrete architectural cost?

**Answer:** Strong consistency. Every read after a write must return the updated inventory count from any node — guaranteed. This prevents both users from seeing "1 item available" simultaneously. Concrete architectural cost: the inventory write must acquire a row-level lock; all concurrent reads of that record block until the lock is released and nodes confirm the write. Reads cannot be served from read replicas for this query — they must hit the primary. This adds latency on every purchase confirmation.

---

### Q4.4 — Latency vs throughput diagnostic

**Question:** Your API handles 500 req/sec at 50ms latency. Throughput stays at 500 req/sec. Latency climbs to 800ms. What's happening and where do you investigate first?

**Answer:** Throughput holding steady means requests are getting in and completing — the system is not shedding load at the gate. The bottleneck is inside the request pipeline, not at ingress. Each individual request is taking longer to process. Investigate in order: (1) cache hit rate — a drop means more requests are falling through to the DB, slowing each one; (2) slow query log — DB queries getting heavier; (3) app worker processing time — heavier computation per request; (4) external API call latency. If throughput had also dropped, you'd suspect the LB or ingress is the bottleneck.

---

### Q4.5 — Hospital records: consistency model + architectural consequence

**Question:** A doctor updates a patient's medication at 9:00am. At 9:00:02, a nurse at a different station reads the same patient. What consistency model and one architectural consequence?

**Answer:** Strong consistency. Stale medication data could cause patient harm — this is exactly the case for strong over eventual. Architectural consequence: medication reads cannot be served from read replicas (they may lag the primary). All reads of critical fields must go to the primary node, which increases read latency. Bonus: non-critical fields (contact info, address) can use eventual consistency — different consistency contracts for different data within the same system (polyglot consistency by data type).

---

### Q4.6 — Read-heavy feed: three-tier architecture

**Question:** 95% reads, 5% writes, DB at 90% CPU. Name three things you add and what each one fixes.

**Answer:** The canonical three-tier read stack, outermost to innermost:
1. **CDN (edge layer)** — caches rendered content close to users (Cloudflare, Fastly, CloudFront). Absorbs ~80-95% of reads before they reach your infrastructure. Fixes: eliminates the bulk of DB pressure in one move.
2. **Redis cache (app-adjacent)** — caches hot dynamic data that survives the CDN (feed content, trending posts, user profiles). Fixes: absorbs the reads that fall through the CDN without hitting the DB.
3. **Read replicas (DB layer)** — additional DB instances handling reads only; primary handles writes only. Fixes: distributes the DB-level reads that fall through both cache layers across N nodes instead of hammering one primary.

Read path: User → CDN → (miss) → Redis → (miss) → Read Replica → (miss) → Primary DB. Write path: User → App Server → Primary DB → replicates out.

---

---

## Section 5: Architectural Patterns

### Q5.1 — Monolith: reject microservices at 3 engineers

**Question:** Your 3-person startup just hit its first performance issue. A junior dev says "we should split into microservices." What do you tell them?

**Answer:** Not yet. At 3 engineers, the team doesn't have the capacity to support the operational overhead — separate CI/CD pipelines, monitoring, logging, and debugging across services. The right path: build a well-structured, modular monolith first. Extract services only when you have evidence you need them: a specific component with different scaling needs, or team coordination in one codebase becoming the bottleneck. "Monolith → modular monolith → extract services one at a time" is the real-world path.

---

### Q5.2 — Three specific microservices problems

**Question:** Your company just migrated to microservices — 8 services, 3 teams. Name three specific new problems you now have.

**Answer:**
1. **Network complexity** — function calls between components are now HTTP requests that can fail, time out, or arrive out of order. You need retry logic, timeouts, and circuit breakers for operations that used to be free.
2. **Data consistency** — each service owns its own database. Keeping data in sync across services (e.g. a user deletion cascading through 4 services) is a hard distributed systems problem.
3. **Operational overhead** — instead of one deploy pipeline, you have 8. Each service needs its own monitoring, logging, alerting, and CI/CD configuration.
4. **Debugging difficulty** — a bug spanning two services means correlating logs from two different systems.

---

### Q5.3 — Serverless cost trade-off

**Question:** Your API has steady, predictable traffic: 40,000 req/hr around the clock. Your architect proposes AWS Lambda. What's the actual problem?

**Answer:** Cost. At steady, predictable volume, functions stay warm — cold starts are not the issue. The pay-per-execution model becomes more expensive than a provisioned server running continuously at that scale. Serverless is optimized for bursty or unpredictable traffic where you'd otherwise be paying for idle capacity. At 40K req/hr steady, a provisioned server is cheaper and easier to reason about.

---

### Q5.4 — Sync vs async: job application flow

**Question:** A user clicks Apply. Your system must: (1) save application to DB, (2) email the employer, (3) email the user confirmation, (4) log to analytics. Which are sync and which async?

**Answer:** Only (1) is synchronous — the user needs confirmation their application was saved before the response returns. Steps (2), (3), and (4) are all async: publish `application_submitted` event, and let the email service and analytics service consume it independently. The user doesn't need to wait for emails or analytics logging. If the email service is down, the application is still saved — resilience via decoupling.

---

### Q5.5 — Three signals to extract a service

**Question:** Give three specific triggers that tell you it's time to extract a service from your monolith.

**Answer:**
1. A specific component has meaningfully different scaling needs from the rest (e.g. image processing uses 10x more CPU than everything else) — you have evidence, not just a hunch.
2. Team size makes coordination in one codebase painful (typically >15-20 engineers stepping on each other).
3. You have clear, stable domain boundaries AND can afford the operational overhead (dedicated DevOps, per-service CI/CD, monitoring).

All three should be true before extracting. Missing clear domain boundaries means you'll be refactoring the split itself as requirements evolve.

---

### Q5.6 — Event ordering failure mode

**Question:** Events `subscription_renewed` then `subscription_cancelled` are published 10ms apart. Consumer processes them in reverse order. What's the problem and how do you fix it?

**Answer:** The consumer applies `subscription_renewed` last, leaving the user with an active subscription when they intended to cancel. Final state depends on processing order, not event intent. Fixes: (1) **Partition by customer ID** in Kafka — events for the same customer always go to the same partition, preserving order; (2) **Sequence numbers or timestamps on events** — consumer discards events older than the last processed; (3) **Idempotent consumers that check current state** — before applying `renewed`, check whether the customer is already cancelled; if so, ignore the stale event. In practice: partition keys for ordering + timestamps as a safety net.

---

*(More questions added as per-section reviews progress through Sections 6-12.)*
