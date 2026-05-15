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

---

## Section 6: Caching

### Q6.1 — Cache-aside: actors and steps

**Question:** Walk through cache-aside end-to-end on a cache miss, then on a cache hit. Name every actor involved.

**Answer:**

**Cache miss path:**
1. **Application** checks Redis — cache miss (key not found).
2. **Application** queries the **database** directly.
3. **Application** writes the result to **Redis** with a **TTL** (expiry time).
4. **Application** returns the result to the user.

**Cache hit path:**
1. **Application** checks Redis — cache hit.
2. **Application** returns cached value immediately. DB is never touched.

**Key characteristic:** the **application layer** is responsible for all three operations (check, query, populate). The cache itself is passive. This distinguishes cache-aside from write-through, where the cache layer handles the DB write automatically.

**Interview one-liner:** *"Cache-aside puts the application in charge: check the cache, miss → query DB → populate cache with a TTL → return. The cache has no knowledge of the DB."*

---

### Q6.2 — Write strategies: naming precision

**Question:** Name three write caching strategies and what each one does. Which do you pick for a cart service that requires no stale reads?

**Answer:**

**Write-through:** on a write, app writes to cache synchronously AND cache/app writes to DB synchronously. User waits for both. Cache and DB stay in sync on every write. Latency cost: every write blocks on two stores.

**Write-behind (write-back):** on a write, app writes to cache and immediately returns success. DB updated asynchronously in background. Lower write latency; risk of data loss if cache fails before DB sync.

**Invalidate-on-write:** on a write, app **deletes** the cache entry instead of updating it. Next read is a cache miss → fetches fresh from DB → repopulates. Simpler than write-through (no two-store sync); trades a write-time op for a one-time miss on next read.

**For cart service:** **write-through.** Cart data must be consistent — user must see what's in the DB. Synchronous DB + cache write latency is acceptable; stale cart data (wrong items, prices, quantities) is not.

**Critical distinction:** write-through pushes new data *into* the cache. Invalidate-on-write *removes* the entry. Same consistency goal, different mechanism. These are NOT the same thing.

---

### Q6.3 — Eviction policies: LRU vs LFU applied

**Question:** Redis is at 95% capacity. Active session tokens AND 3-week-old flash sale HTML fragments live in the same instance. Which eviction policy, and what's the architectural catch?

**Answer:**

**LRU (Least Recently Used):** evicts the key accessed least recently. For this scenario: flash sale fragments from 3 weeks ago haven't been accessed recently — LRU naturally evicts them first. Correct choice here.

**LFU (Least Frequently Used):** evicts the key with fewest total accesses over time. Better for burst-traffic content (accessed thousands of times during a window, then nothing). LRU would evict a flash sale item that was hot last week; LFU correctly identifies historical popularity.

**The architectural catch:** `maxmemory-policy` in Redis is **instance-wide** — you cannot set different eviction policies per key or namespace. If different data types need different eviction behaviors, you need **separate Redis instances**.

**Session token risk:** session tokens should NOT be subject to memory-pressure eviction at all. If Redis evicts a session token under load, the user gets silently logged out mid-session — no error, just a redirect to the login page. Session tokens belong in a **dedicated Redis instance with enough headroom**, managed by **explicit TTL** (idle timeout), not by memory pressure.

---

### Q6.4 — Cache stampede / thundering herd

**Question:** Redis key `homepage:featured_products` expires. 8,000 users hit the homepage simultaneously. (a) Failure mode? (b) Two specific mitigations? (c) Which one for a single hot key?

**Answer:**

**(a) Cache stampede (thundering herd):** all 8,000 requests get a cache miss simultaneously. All 8,000 hit the DB at once. DB receives 8,000 queries instead of 1. Can crash or severely degrade, causing cascading failure.

**(b) Two mitigations:**

1. **Staggered TTLs / jitter:** randomize expiry instead of a fixed TTL: `TTL = base + random(0, 60)`. Keys in a population expire at different times → stampedes spread across a window instead of all firing at once.

2. **Lock-based recomputation (mutex / distributed lock):** when a key expires, the first request acquires a Redis lock (`SET NX` — set if not exists). That one request hits the DB, recomputes, populates the cache, releases the lock. All other requests wait on the lock or return a stale value. Result: DB gets exactly **1 query** instead of 8,000.

**(c) Single hot key → lock-based recomputation.**

Jitter is the wrong tool for a single key. Randomizing the TTL of ONE key doesn't help — all threads still race for it when it expires. Jitter prevents stampedes across *populations* of keys. For one hot key, use a distributed lock.

**Mental model: single hot key → lock. Population of keys → jitter.**

---

### Q6.5 — When NOT to cache

**Question:** PM wants to cache the user notifications feed. What questions do you ask, and what conditions make this a bad idea?

**Answer:**

**Three questions to ask:**
1. **Is it personalized?** Each user has a unique feed → N users = N cache entries, each served to exactly one person. Cache hit rate ≈ 1. Near-zero ROI.
2. **Read frequency vs write frequency?** Notifications are high-write (arrive constantly) and often read-once (user sees it, dismisses it). If writes ≥ reads, cache invalidates as fast as you populate it.
3. **How stale is acceptable?** Notifications are time-sensitive. A cache TTL introduces staleness users will notice ("why didn't I see that message?").

**Bad idea when all three conditions hold:**
- Highly personalized → low hit rate
- High-write / read-once → entries stale immediately
- Freshness required → TTL can't be long enough to amortize the miss cost

**What you CAN cache:** global/shared notifications — site-wide announcements, promotional banners, system status messages. One cache entry, all users.

**The clean rule:** cache is valuable when data is **read many times, changes infrequently, and is shared across users**. Notifications fail all three.

---

### Q6.6 — CDN caching + cache busting

**Question:** New JS bundle deployed. Two hours later, users still load the old version. (a) What's happening? (b) Correct fix? (c) Naive fix and why it's worse?

**Answer:**

**(a) What's happening:** CDN cached `bundle.js` with a long TTL. New version deployed to origin; CDN doesn't check — it serves its cached copy until TTL expires. Same URL = same CDN response.

**(b) Correct fix — content-addressed filenames:**

```
bundle.js           ← same URL, CDN caches forever
bundle.a1b2c3.js    ← filename includes a hash of file content
```

When content changes, hash changes, filename changes. CDN sees a **new URL** and fetches from origin automatically. You can set TTL of **1 year** on JS/CSS assets — stale content is literally unreachable (old filename doesn't exist in the new deploy). Webpack/Vite/Rollup do this automatically.

**Pattern:** long TTL on static assets + content-addressed names + short TTL on the HTML file (so users get the new bundle filename quickly).

**(c) Naive fix — CDN purge API:** manually invalidate the cached object after every deploy. Works, but: reactive (must remember to do it), slow to propagate across all edge nodes, brittle (miss one deploy = users see old version), expensive (many CDNs charge per-purge). Content-addressed filenames make purging unnecessary entirely.

---

---

## Section 7: Load Balancing & Networking

### Q7.1 — Four LB algorithms: mechanisms + use cases

**Question:** Walk through the four main load balancing algorithms. For each one, name the use case where it's the right choice.

**Answer:**

1. **Round-robin** — rotate through servers in order. Request 1 → Server A, Request 2 → Server B, etc. Use when: stateless requests on **homogeneous** servers (identical CPU/RAM) with roughly equal request cost.

2. **Weighted round-robin** — same rotation, but servers with higher capacity get more turns (Server A gets 2 requests for every 1 Server B gets). Use when: servers are **heterogeneous** — different CPU/RAM across instances. Weights are static and pre-configured, not reactive.

3. **Least connections** — send to whichever server has the fewest active connections right now. Use when: requests have **wildly different durations** — video uploads, WebSocket connections, streaming. Round-robin treats a 7-minute upload the same as a 20ms API call; least connections sees the actual load.

4. **Consistent hashing** — hash the request key (cache key, shard key) and map it to a node. Same key always routes to the same node. Use when: you need **cache key locality** — the same cache key always hitting the same cache node keeps that node's cache warm. When a node dies, only its keys redistribute (ring minimizes churn).

**Critical distinction:** consistent hashing routes *keys to nodes* for cache locality. Session stickiness routes *users to servers* for stateful session reasons. Different problem, different tool.

---

### Q7.2 — Session stickiness vs consistent hashing

**Question:** A multiplayer game stores each game room's state in memory on the app server managing it. A player disconnects and reconnects. What mechanism do you use, and what's the better long-term architecture?

**Answer:**

**Immediate mechanism: session stickiness.** The LB tracks which server that user was pinned to (via cookie or IP) and routes them back. The game room state is still there; reconnect is seamless.

**Better architecture: externalize state to Redis.** Don't rely on stickiness at all. If state is stored in Redis instead of app-server memory, any server can handle any player — reconnecting to a different server doesn't matter. Stateless app servers + external state store is the architecture that scales and survives server failures.

**The consistent hashing distinction:** if you have a distributed cache layer (N Redis nodes) and want the same cache key to always hit the same Redis node (for cache locality), that's consistent hashing — routing by key. Stickiness routes by user identity. Not the same problem.

---

### Q7.3 — Reverse proxy vs load balancer

**Question:** What's the difference between a reverse proxy and a load balancer? Are they the same thing?

**Answer:**

**Not the same, but overlapping.** A load balancer is a *type* of reverse proxy — a reverse proxy that specializes in distributing traffic. A reverse proxy is the broader category.

**Reverse proxy** sits between clients and backend, acting on the backend's behalf. Can do: SSL termination, compression, caching, security (hide backend IPs), routing (`/api` → Service A, `/images` → Service B).

**Load balancer** distributes requests across multiple backend servers. Its core job is traffic distribution — algorithm-based routing across N instances.

**The overlap:** tools like Nginx do both. AWS ALB is primarily a load balancer but also terminates TLS.

**Three-tier mental model:**
1. One backend server → still want a reverse proxy (SSL, caching, security)
2. Multiple backend servers → need load balancing; reverse proxy often handles it
3. At scale → dedicated managed LB (AWS ALB) out front + Nginx as reverse proxy per server

*"A reverse proxy is about what sits in front of your servers. Load balancing is about distributing across them. Most real tools do both."*

---

### Q7.4 — API gateway: what it buys you and the critical don't

**Question:** You have 8 microservices. A senior engineer says "put an API gateway in front of everything." What does it buy you, and what's the one thing you must NOT do with it?

**Answer:**

**What it buys you (cross-cutting concerns in one place):**
- **Authentication/authorization** — validate JWTs or API keys before requests reach your services
- **Rate limiting** — per-user or per-endpoint limits enforced once, not duplicated in every service
- **Request routing** — `/users` → User Service, `/orders` → Order Service
- **Logging and metrics** — one place to observe all traffic
- **Protocol translation** — client speaks REST, backend speaks gRPC

**Architecture:** Client → Public LB → API Gateway cluster (N identical instances) → backend services. The gateway is one logical service, horizontally scaled as identical instances. Never one gateway per service — that duplicates the auth/rate-limiting logic N times and forces the client to know which gateway to call.

**The one critical don't: do not put business logic in the gateway.**

The gateway handles cross-cutting concerns only. The moment you add data transformation, service orchestration, or service-specific logic, you've created a God service — hard to test, hard to deploy, and every team has to touch it when their service changes. The gateway becomes the bottleneck instead of infrastructure.

**Rule:** gateway handles cross-cutting concerns, services handle business logic. Never cross the streams.

---

### Q7.5 — Session stickiness failure mode

**Question:** Your LB uses session stickiness across three app servers. Server B goes down. What happens to the users pinned to Server B, and what does this reveal about the trade-off?

**Answer:**

**What happens:** the LB can no longer route to Server B. Users pinned to it get redistributed to Server A or C — but Server B's in-memory state is gone. Those users start from a clean slate: lost session, lost in-progress work, likely forced back to login.

**What this reveals:** stickiness undermines the core benefit of load balancing, which is fault tolerance. The whole point of multiple servers is that if one fails, others absorb the traffic seamlessly. Stickiness breaks that — a chunk of users can't be absorbed cleanly because their state lived only on the dead machine.

**Trade-off one-liner:** *Stickiness trades fault tolerance for stateful convenience. When a server dies, sticky users feel it. With externalized state (Redis), server death is invisible to users.*

---

### Q7.6 — Least connections vs round-robin for long-lived uploads

**Question:** A file upload service handles videos that take 3–8 minutes to upload. Your LB uses round-robin. An engineer argues for switching to least connections. Are they right? Make the case.

**Answer:**

**They're right.** Round-robin assumes all requests cost roughly the same — it doesn't adapt. A server handling 10 active 8-minute uploads looks identical to one handling 10 idle connections from the LB's perspective; round-robin sends the next upload to whichever server is "next in line" regardless.

Least connections sees the actual open connection count. If Server A has 12 active uploads and Server C has 2, least connections routes to C. It naturally distributes the actual load, not the theoretical equal load.

**When round-robin is fine:** stateless API calls where each request takes ~20ms and cost is roughly equal. When to reach for least connections: long-lived connections — video uploads, WebSocket sessions, streaming, large file processing — where duration variance is high and "equal turns" doesn't mean "equal load."

---

## Section 8: Message Queues & Async Processing

### Q8.1 — When to queue vs. stay synchronous

**Question:** A user uploads a profile photo. Your API needs to: (1) save the raw image, (2) resize to 3 thumbnail sizes, (3) update the user's profile record with the new image URL, (4) send a push notification. Which steps are synchronous? Which go on a queue?

**Answer:**

- **Step 1 — Synchronous.** User must know immediately if the save failed so they can retry. This is the critical path.
- **Step 2 — Queue.** Resize is CPU-intensive and not needed before the user gets a response. Drop it on the queue; a worker handles it in the background.
- **Step 3 — Synchronous, but with a nuance.** Update the profile record immediately with the **raw image URL** from step 1 — the user expects to see their new photo right away. The thumbnail URLs don't exist yet (step 2 is still queued), so a second consumer updates the profile record again once thumbnails are ready. Two updates, not one.
- **Step 4 — Queue.** Not user-blocking, not critical path.

### Q8.2 — At-least-once delivery and idempotency

**Question:** A consumer picks up an order notification, successfully notifies the restaurant, then crashes before acking. What happens next, what problem does it create, and how do you prevent it?

**Answer:**

**What happens:** the queue never received the ack, so it treats the message as unprocessed and redelivers it to the next available consumer.

**The problem:** the restaurant gets notified twice — double processing. At scale this means duplicate emails, duplicate charges, duplicate order entries.

**The fix — idempotency.** Before processing, check whether this message has already been handled. For the restaurant notification: before notifying, check if `order_id` already has a `restaurant_notified` flag set. If yes → skip (no-op). If no → notify and set the flag. The key property: processing the same message twice produces the same outcome as once — the second run is a no-op, not a second action.

---

## Section 9: Database Architecture

### Q9.1 — ACID and when ACID requirements rule out NoSQL

**Question:** Walk through ACID. Then: when would you reject MongoDB (or any document store) for a use case purely on ACID grounds?

**Answer:**

**ACID:**

- **Atomicity** — a transaction is all-or-nothing. If part of it fails partway through, the DB **rolls back** to the pre-transaction state at the DB layer (not the app layer). Classic example: transferring $100 between accounts — debit A succeeds, credit B fails → both reverted. You never end up in a half-done state.
- **Consistency** — a transaction can only move the DB from one valid state to another. Constraints, foreign keys, and unique-checks hold across the transaction.
- **Isolation** — concurrent transactions don't step on each other. Two users buying the last concert ticket can't both succeed.
- **Durability** — once a transaction commits, it survives a crash. The DB writes to disk before returning "success."

**One-liner:** ACID is the guarantee that the DB won't lie to you or leave your data in a broken state, even when things go wrong.

**When to reject MongoDB on ACID grounds:**

1. **Multi-document transactions.** When a single logical operation spans multiple records (money transfer touching two accounts; order creation touching `orders` + `inventory` + `payment_log`) and you need all-or-nothing semantics. MongoDB has multi-document transaction support now but it's a more recent feature and has performance trade-offs; Postgres has had it for decades and it's a first-class citizen.
2. **Schema flexibility as liability.** Document stores let any document have any shape — great when data shape varies legitimately (CMS content, user-defined fields). **Liability** when data integrity matters: there's no schema enforcement at the boundary, so a buggy service can write malformed records and the DB happily accepts them. For financial / regulatory / inventory data, you want the DB to reject bad data at the door.

**Heuristic:** if the requirements mention "money, inventory, bookings, or audit," default to SQL.

---

### Q9.2 — Composite index, when and how to order

**Question:** When do you reach for a composite index, and how do you order the columns?

**Answer:**

**When:** the query filters on one column AND sorts on another (or filters on multiple columns together).

**Column order:** filter column first, sort column second. The DB walks the index from the filter value, then reads rows in sort order without a separate sort step.

```sql
-- query: WHERE user_id = ? ORDER BY created_at DESC
-- index: (user_id, created_at)
```

Get the order wrong and the index either doesn't get used or only helps with half the query.

---

### Q9.3 — User refreshes after updating profile photo and sees the old photo

**Question:** A user updates their profile photo. They refresh and see the OLD photo. What's happening, and how do you fix it without breaking the read-scaling architecture?

**Answer:**

**What's happening: replica lag — normal asynchronous behavior, not a crash or failover.**

The write went to the primary DB. Reads (including this user's refresh) get routed to a replica for read scalability. **Replicas catch up asynchronously** — usually milliseconds, sometimes seconds under heavy write load. The user's refresh hit a replica that hadn't applied the photo update yet, so they saw stale data. This happens every day under normal operating conditions. **No outage required.**

This is eventual consistency in practice (CAP theorem) — the cost of read-replica scaling.

**Fix: Read-Your-Own-Writes (RYO-W) consistency.** After a user writes, route **that user's** subsequent reads to the primary for a short window (e.g., 5-10 seconds), or just for the response to that specific write request. Other users' reads continue hitting replicas — only the write originator pays the consistency cost.

**Important framing:** RYO-W is scoped to the user who just wrote, NOT "send all reads to the primary." Sending all reads to the primary defeats the entire point of having replicas.

---

### Q9.4 — Shard key for a messaging app

**Question:** You're sharding a messaging app's `messages` table. Pick a shard key. Defend it. Name what you'd avoid and what failure mode to avoid.

**Answer:**

**Shard key: `conversation_id`.**

Two properties make it the right choice:

1. **High cardinality, even distribution** — many conversations across the user base; no single conversation dominates the total message volume.
2. **Query locality** — all messages in a conversation live on one shard. Fetching "show me this conversation" is a single-shard lookup. No fan-out.

**Avoid `message_id`** — distributes uniformly but **destroys query locality**. Every "fetch this conversation" becomes a **scatter-gather** query: hit every shard, merge results. Latency explodes, especially as the shard count grows.

**Avoid `user_id`** — looks reasonable, but a heavy-traffic user (a celebrity, a service account) creates a **hot shard**. One shard gets disproportionate write/read load while others sit idle.

**Hot shard** = a shard receiving disproportionate traffic due to uneven key distribution or access pattern. Term to know cold for senior interviews — describing the problem without naming it costs vocabulary points.

---

### Q9.5 — Postgres is choking, 20 app instances, no connection pool

**Question:** You have 20 app instances making DB queries directly with no connection pool — each request opens a fresh connection, runs its query, closes the connection. Postgres is failing under load. (a) What's the root cause? (b) What's the math when you add a pool? (c) What's the canonical fix in production?

**Answer:**

**(a) Root cause: no pool at all.** Every single request pays the cost of a fresh connection: TCP handshake, auth, session setup. Under load, this overhead is brutal — Postgres connection slots are finite (default `max_connections = 100`), and you exhaust them faster than the OS can clean up the closed ones.

The fix in concept: a **connection pool** maintains a set of open connections that get **reused** across requests. Request comes in → grab an idle connection from the pool → run the query → return it to the pool. No handshake overhead per request.

**(b) Math with a typical pool size of 15 per instance:** 20 instances × 15 connections = **300 connections**. Postgres default `max_connections = 100`. **You're 3x over the default.** Even with a pool, you'd saturate Postgres unless you raise the limit or reduce per-instance pool size — and raising `max_connections` has its own memory costs.

This is why the math matters: a pool isn't free, it just shifts the bottleneck.

**(c) Canonical production fix: PgBouncer.**

A connection pooler that sits **between the app and Postgres**. Apps connect to PgBouncer; PgBouncer multiplexes thousands of app-side connections down to a much smaller pool of actual Postgres connections. The standard tool for this exact problem in production.

**Standard architecture:** App instances → PgBouncer → Postgres. Per-instance pool size goes down because PgBouncer is the real pool.

---

### Q9.6 — Storage strategy for a legal doc analysis tool

**Question:** Building a legal document analysis tool. Users upload PDF contracts. Product needs to: (a) store raw PDFs, (b) let users search by keyword within document text, (c) let users find contracts semantically similar to a query like "non-compete clause for sales reps." What storage do you use for each, and what mistake should you avoid?

**Answer:**

**(a) Raw PDFs → S3 (object/blob storage).**

Cheap, infinitely scalable, designed for files. The DB stores a reference (the S3 key), files don't bloat the DB. Never store raw blobs in Postgres rows — it kills query performance and inflates backup size.

**(b) Keyword search within document text → Elasticsearch (BM25).**

ES indexes the extracted text and scores results by keyword relevance using BM25 (term frequency + rarity). Handles typos, partial matches, stemming, phrase matching. SQL `LIKE '%foo%'` works for one document but can't rank or scale. SQL can't rank.

**(c) Semantic similarity → vector embeddings + vector store.**

Convert each document chunk to a vector (embedding), convert the query to a vector, find nearest neighbors by cosine similarity. **pgvector** (Postgres extension) is fine for moderate scale; dedicated vector DBs (Pinecone, Weaviate, Qdrant) for large scale.

**The mistake to avoid: reaching for Elasticsearch for semantic search.** ES added vector capabilities later but it is a **search engine first**, not a purpose-built vector DB. The conflation is:

- **BM25 (Elasticsearch native)** = keyword relevance scoring. Term frequency × rarity. Matches exact words and variations.
- **Semantic similarity (vector DBs)** = vector math. Finds conceptually similar content even if no words overlap.

Different problems, different tools. "Non-compete clause for sales reps" matching a document that talks about "restrictive covenants for account executives" is **semantic**, not keyword — BM25 misses it because the words don't overlap.

**Hybrid search** = BM25 (ES) + semantic (vector store) running in **parallel**, results merged with weighted scoring. Not sequential — neither pipeline feeds the other.

---

## Section 10: Search Infrastructure

### Q10.1 — Postgres or Elasticsearch for natural-language job search

**Question:** Your startup has a Postgres table with 5M job listings. Users type queries like "senior react engineer remote NYC." Do you query Postgres or add Elasticsearch? Why?

**Answer:**

**Add Elasticsearch.**

Postgres can do exact filters and `LIKE '%query%'` matches, but it cannot **rank by relevance**. ES scores results using BM25 — term frequency × rarity. A listing that contains all 5 keywords from the query ranks above one that contains 2. ES also handles typos ("reactt" → "react"), stemming ("engineers" matches "engineer"), and phrase matching.

**The cue for adding a search layer:** the requirement says "search by keyword" / "free-form query with ranked results." SQL is for **filtered lookups** (`WHERE` clauses with structured fields). ES is for **relevance-ranked search** over freeform text.

**For semantic intent too (user types "remote react job" and wants results that mention "WFH front-end engineer"):**

BM25 (Elasticsearch) and vector embeddings (pgvector / Pinecone) run **in parallel** — each retrieves its top-N independently, a merge step combines them with weighted scoring (e.g., 60% BM25 + 40% semantic). **Not sequential** — BM25 doesn't filter the semantic results, and semantic doesn't rerank BM25 output. They are two independent retrievers feeding one merge step.

---

### Q10.2 — "New listings don't appear in search for 30 seconds" — bug or feature?

**Question:** A product manager files a bug: *"When sellers add a new listing, it doesn't appear in search results for ~30 seconds."* (a) What's the architecture causing this? (b) Is this a bug? How do you frame the answer for the PM?

**Answer:**

**(a) Architecture:**

1. Write goes to Postgres (source of truth).
2. A sync process — typically a queue consumer or event stream (CDC, Kafka, Redis pub/sub) — copies the new record to Elasticsearch.
3. Search queries hit Elasticsearch, not Postgres.

The 30-second delay is the **propagation lag** between the Postgres commit and the ES index update.

**(b) Not a bug — it's the trade-off.**

Elasticsearch is a **read-optimized view** of the primary data, never the source of truth. The propagation delay is the cost of having a search layer at all. **This is eventual consistency working as designed.**

**Framing for the PM:**

> *"Elasticsearch isn't real-time — it's seconds behind Postgres by design. That's the trade-off we accepted when we added the search layer in exchange for ranked relevance search, partial matches, and the ability to handle freeform queries Postgres can't. If 30 seconds is consistently too long for the product, we can tune the sync interval — but that has cost implications (more frequent syncs = more load). It's a knob, not a defect."*

The framing matters in real product conversations: **"trade-off we accepted"** beats **"this is how it works"** every time — the first invites a product conversation about whether the trade-off is still right; the second sounds dismissive.

---

### Q10.3 — Customer success wants Elasticsearch for invoice filtering

**Question:** Customer success asks you to add Elasticsearch to power a new feature: *"Let users find all invoices from Q3 2024 marked as overdue, sorted by amount."* Should you add ES?

**Answer:**

**No. This is not a search problem — it's a structured filter query.**

The query is a SQL `WHERE` clause:

```sql
SELECT * FROM invoices
WHERE quarter = 'Q3 2024' AND status = 'overdue'
ORDER BY amount DESC;
```

There's no freeform text, no relevance ranking needed, no fuzzy matching, no partial matches. Just exact matches on structured fields and a sort. Postgres with appropriate indexes (composite on `(status, quarter, amount)` or similar) handles this fast at any reasonable scale.

**The diagnostic question to ask before recommending ES:**

> *"Is this relevance-ranked freeform search, or structured filtered lookups?"*

- **Search** = "find me anything matching 'react engineer NYC'" → freeform, no exact field-value pairs, results need relevance ranking → **ES.**
- **Filter** = "give me records where field X = Y and Z > N, sorted by W" → exact field-value matching, structured → **SQL `WHERE` + index.**

**The trap:** reaching for ES anytime the word "search" appears in a feature request. UI labels say "search" for everything — search invoices, search users, search settings. Most B2B record-finding features are filter problems, not search problems.

**Test it on every "add ES" request:** would `WHERE` clauses + indexes solve this on Postgres? If yes, don't add ES. You'd be paying the cost of an additional system (sync pipeline, eventual consistency, ops overhead) for zero benefit.

---

## Section 11: Resilience & Reliability

### Q11.1 — Circuit breaker state machine

**Question:** A payment gateway you depend on starts failing. Your service has a circuit breaker wrapping every call. Walk through all three states by name, what each one does, and what triggers each transition. Then explain which state is load-bearing and why.

**Answer:**

**Three states:**

- **CLOSED** — Normal operation. Requests flow through to the downstream. The breaker counts failures in the background.
- **OPEN** — Tripped. Requests fail immediately without attempting the downstream call. Gives the downstream breathing room. Cooldown is a timer (e.g. 30s), not a condition on traffic.
- **HALF-OPEN** — Cooldown elapsed, testing recovery. One probe request is allowed through.
  - Probe **succeeds** → transition to CLOSED, normal traffic resumes.
  - Probe **fails** → back to OPEN, another cooldown window, try again next probe.

**Transitions:**
- CLOSED → OPEN: failure threshold crossed (rate-over-window or consecutive failures)
- OPEN → HALF-OPEN: cooldown timer elapsed
- HALF-OPEN → CLOSED: probe succeeds
- HALF-OPEN → OPEN: probe fails

**HALF-OPEN is load-bearing.** Without it, you'd be stuck in OPEN forever — or need a human to manually flip the switch back to CLOSED. HALF-OPEN is the self-healing automation: it re-tests the downstream by itself with a single probe and decides whether to resume traffic. Just ONE probe — not a flood — because 1000 requests hitting a still-broken downstream re-triggers cascading failure.

**Trip conditions:** Failure-rate-over-window (e.g., "50 failures in 30 seconds") is more robust than consecutive-failures because it accounts for mixed success/failure traffic. Consecutive-failures is simpler but noisy — one slow minute can trip you unnecessarily.

---

### Q11.2 — Why exponential backoff alone isn't enough

**Question:** 10K clients had requests in flight when a downstream gateway went down for 30s. Walk through (a) the failure mode of naive immediate retry, (b) whether exponential backoff fully solves it and what the residual problem is, (c) what jitter does mechanistically, and (d) the one operation type where retries are unsafe even with backoff + jitter.

**Answer:**

**(a) Naive immediate retry — thundering herd / retry storm.** All 10K clients retry the moment they fail. When the gateway recovers, 10K requests slam it simultaneously and re-crash it. Plus while the gateway is dying, immediate retries hammer it and slow recovery.

**(b) Exponential backoff alone doesn't fully solve it.** If 10K clients all failed at the same moment, they all wait *exactly* 1s, then *exactly* 2s, then *exactly* 4s. They're **synchronized.** Backoff spaces the synchronized stampedes further apart in time but doesn't de-synchronize the clients. Same cohort, same shape, just stretched.

**(c) Jitter de-synchronizes the cohort.** Instead of "wait 2s exactly," wait "a random value in 1.5–2.5s." Different clients pick different waits → arrivals spread across a window → no single moment when 10K hit at once. Formula: `wait = min(base * 2^attempt, max_delay) + random_jitter`. The mechanism is *randomized de-synchronization*, not just delay.

**(d) Non-idempotent operations.** Retrying a POST that creates state (charge a card, place an order, send an email) can create duplicates — the first POST succeeded but the response was lost in transit; retry processes a second charge. Backoff + jitter don't save you. **The fix: idempotency keys.** Client sends `Idempotency-Key: <uuid>` header; server caches `(key → response)` for ~24h; duplicate retry returns the cached response without re-executing. **Retry + idempotency is a package deal — you can't safely have one without the other.**

---

### Q11.3 — Token bucket vs sliding window applied

**Question:** Pick the algorithm and give concrete numbers (capacity/refill or window/limit) for three endpoints: (a) dashboard page that fires ~15 parallel API requests on load then idles 30-60s, (b) password-reset email endpoint ($0.0001/email, abuse risk), (c) AI summarize endpoint ($0.05/call, 3-8s response time, abuse can cost hundreds/hour).

**Answer:**

**(a) Token bucket.** Bursts are expected and benign (page load fires N parallel requests, then quiet). **Capacity: 35 tokens, refill: 1/sec sustained.** Capacity covers the page-load burst plus a refresh; refill rate covers steady idle-and-click usage. **Always state both capacity AND refill rate** — capacity defines the burst, refill defines the sustained rate.

**(b) Sliding window. 3 requests per 5 minutes.** No legitimate burst use case (no one needs to send themselves 3 reset emails in 10 seconds), and a hard cap is exactly the right shape. Layer with per-IP fallback for unauthed traffic.

**(c) Sliding window, layered.** Short: **5/min** (allows accidental double-clicks and legitimate retries). Long: **50/hr** (caps abuse at $2.50/hr/user — bounded cost). 429 + Retry-After response pattern. Per-IP fallback. **Key calibration discipline:** for any expensive endpoint, anchor the rate-limit to the worst-case $/hour per abusive user. "What's the max cost this limit allows?" is the senior framing.

**Response pattern:** Return `HTTP 429 Too Many Requests` with a `Retry-After` header telling the client when they can retry.

---

### Q11.4 — Idempotency mechanism applied (flaky network)

**Question:** User on hotel wifi clicks "Place Order" → POST to /api/orders/checkout charging $189. Server processes and charges the card, but the response packet is lost in transit. Client auto-retries. Walk the full mechanism: (a) what client generates and where it goes, (b) server logic on first POST, (c) server logic on retry — and critically, how many times is the card charged, (d) cache TTL strategy.

**Answer:**

**(a) Client side.** Client generates a **UUID** at the moment of the logical action (when the user clicks "Place Order" — NOT regenerated per retry). The SAME value is reused across all retries of that logical operation. Sent in the HTTP header named **`Idempotency-Key`**. The persistence-across-retries is what makes the entire mechanism work — if the client regenerated a fresh UUID per retry, dedup is defeated.

**(b) First POST — server logic in order:**

1. Read `Idempotency-Key` header.
2. Check cache: is this key already stored?
3. If MISS → process the request normally (charge card, save order), then cache `(key → full HTTP response payload + status code)`, then return response.
4. If HIT → see (c).

**Cache the response, not the request.** The cached value should be the full response body + status code, so the client experience on retry is byte-identical to the original.

**(c) Retry POST — same logic, cache hit branch:**

1. Read `Idempotency-Key` header (same UUID as first attempt).
2. Cache check: HIT.
3. Return the cached response immediately — no card charge, no DB writes, no side effects.

**The card is charged ONCE.** The user sees one successful order confirmation, one charge on their statement, one shipped item. From the user's perspective, the network blip and the retry are *completely invisible.* That invisibility is the whole point of the pattern.

**(d) TTL: ~24 hours (Stripe convention).**

- **Why 24h works:** any retry happening more than 24h after the original is, by definition, an intentional re-action by the user (not a network-layer retry). Returning a cached response after 24h would actually be a bug.
- **Why 30s is too short:** real flaky-network retries can stack over minutes (TCP timeouts + client backoff + user manually refreshing). Evict at 30s, a slow retry slips through → card charged twice.
- **Why cache-forever is bad:** (i) unbounded storage growth, (ii) bigger UX bug — user legitimately re-purchases the same item 6 months later, server returns the cached 6-month-old response with the old order ID, user never sees their new order go through. Worse than the duplicate charge it was meant to prevent.

**Calibration rule:** TTL must outlast all realistic retry windows but be short enough that intentional re-actions are treated as fresh.

---

### Q11.5 — Graceful degradation in a partial-failure scenario

**Question:** B2B SaaS analytics dashboard has 7 components: auth, core metrics, real-time event stream, AI insights panel (Anthropic API), saved-segment dropdown, team activity sidebar (presence Redis), recent exports widget (S3 listings). At 9:42 AM: Anthropic returns 503s, presence Redis crashed, S3 listings p99 went from 200ms to 8s. Dashboard timing out at 12+ seconds. (a) Identify critical path. (b) Specific degradation for each of the 3 failing dependencies. (c) Rebut the "just show a banner" argument. (d) Which failure causes cascading failure if treated naively?

**Answer:**

**(a) Critical path: Auth + Core Metrics + Saved Segments.** These are the components the user must have for the page to be worth loading at all — the user's core goal is "view my product's analytics." Everything else degrades. Test for critical-path: "Can the user complete their core goal without this component?" If yes, it's not critical.

**(b) Degradation for each failing dependency:**

- **Anthropic API (AI insights panel) → Disable feature** (hide the panel with a small inline note: "Insights temporarily unavailable") OR **cached data** — serve last-known-good insight from cache. Yesterday's retention summary is fine; most senior teams cache LLM responses for cost reasons anyway.
- **Presence Redis (Team activity sidebar) → Disable feature.** Hide the sidebar entirely or show "Team activity unavailable." Cheapest degradation — no one loses sleep over a missing sidebar.
- **S3 listings slow (Recent exports widget) → Partial response + aggressive timeout.** Load the dashboard *without* this widget; render it async with a 500ms-1s timeout; on timeout show "Loading exports..." or fall back to "Exports temporarily unavailable." **Do not block the page load on this 8-second call.**

**(c) Senior rebuttal to "just show a banner":**

1. **Different failures have different lifespans.** Anthropic might be down for hours, Redis reboots in 15 min, S3 is just slow. One banner forces the longest-lived failure to set the user experience for everyone.
2. **The user's primary job — viewing analytics — is fully operational.** Forcing a refresh when the core product is healthy makes outages bigger than they have to be.
3. **Partial failure is the normal state of distributed systems.** All-or-nothing thinking is the junior-engineer trap — designing for it turns every dependency outage into a full outage.

**(d) S3 listings slow → cascading failure via thread/connection pool exhaustion.**

If your app calls S3 synchronously during dashboard load and S3 is taking 8s per call, every dashboard request holds an app server thread for 8s. App servers have finite thread pools (say, 100). At ~13 req/sec the pool is exhausted; new requests queue; queue overflows; **dashboard returns 503 even for users who don't care about the exports widget.**

**Slow-but-not-failing is more dangerous than outright failure.** Anthropic's 503 fails in ~50ms — thread frees up. Redis crash fails in ~10ms — thread frees up. S3 holds the thread for 8 seconds.

**The fix is the circuit breaker.** When S3 latency crosses a threshold, trip the breaker, fail fast for S3 calls, threads stay free. Or: aggressive timeout (1s max) + treat the widget as partial-response. **Slow dependencies are the canonical use case for circuit breakers, not just down dependencies.**

---

*(More questions added as per-section reviews progress through Sections 9-12.)*
