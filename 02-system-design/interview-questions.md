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

*(More questions added as per-section reviews progress through Sections 3-12.)*
