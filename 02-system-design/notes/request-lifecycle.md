# Request Lifecycle

The full path has roughly 6 major stages: DNS → TCP → TLS → HTTP request → server processing → HTTP response & render.

> *"What happens when you type https://twitter.com and hit Enter?"*

**6 Lifecycle Stages:**

1. DNS Resolution
2. TCP Handshake
3. TLS Handshake
4. The HTTP Request
5. Server-Side Processing
6. HTTP Response + Browser Render

---

## Stage 1: DNS Resolution

- [TIMELINE] - DNS translates the human-friendly text into an IP address so your device can recognize and "speak" to the requested server
- DNS chain, in order:
  1. Browser cache
  2. OS cache
  3. Router / local network cache
  4. Recursive resolver
- Every DNS record has a TTL

### Mental model of DNS resolution

Two layers:

1. **Caches in front** (browser → OS → router → resolver) -- fast path, hit and done
2. **Hierarchy behind the resolver** (root nameservers → TLD nameservers → authoritative nameservers) -- slow path, only walked when nothing is cached

---

## Stage 2: TCP Handshake

- [TIMELINE] - We have an IP address now (thanks to DNS)
- TCP = **Transmission Control Protocol**
- Before any HTTP request can be sent, the browser and the server need to establish a connection
- TCP takes an unreliable network and gives the app above it a **reliable, ordered, two-way byte stream**
- **Three-way handshake** establishes the connection
  - if your server is 100ms away (cross-continent) the TCP handshake alone costs 100ms before any real work happens
  - this is why **connection reuse** matters so much in HTTP -- opening a fresh TCP connection for every request is wildly expensive, which is why HTTP/1.1 introduced keep-alive and HTTP/2 multiplexes many requests over a single connection
  - Connection reuse matters because handshakes are expensive

### TCP vs UDP

- **TCP** is reliable, ordered, connection-oriented -- when correctness matters more than latency (HTTP, email, file transfer, SSH, db connections)
- **UDP** is fast, fire-and-forget, connectionless -- when latency matters more (live video, voice calls, online games, DNS queries)

---

## Stage 3: TLS Handshake

- [TIMELINE] - TCP gives you a connection, TLS gives you a **secure** connection on top of that
- TLS provides three things:
  1. **Encryption**
  2. **Integrity**
  3. **Authentication**
- It runs on top of TCP
- HTTPS = HTTP + TLS + TCP
  - When you see `https://` that's HTTP running over a TLS-secured TCP connection
- The **server proves identity via a TLS certificate signed by a trusted authority (CA)**
  - your browser trusts a built-in list of CAs (the root certificate store)

---

## Stage 4: The HTTP Request

- [TIMELINE] - We have a secure reliable connection to the server... now the browser finally sends what it came here to send: an HTTP request
- What an HTTP request actually is: just structured text sent over the TCP connection, e.g.

```http
GET /home HTTP/1.1
Host: twitter.com
User-Agent: Mozilla/5.0 ...
Accept: text/html
Cookie: session_id=abc123
Authorization: Bearer eyJhbGc...

(optional body — empty for GET, populated for POST/PUT)
```

3 parts:

- **Request line** -- the verb (`GET`), the path (`/home`), the HTTP version (`HTTP/1.1`)
- **Headers** -- key-value pairs carrying metadata (who you are, what you want, auth, cookies)
- **Body** -- the payload, if any
  - Empty for GET
  - Populated for POST, PUT, PATCH

### HTTP method semantics

**HTTP method semantics are a contract that the rest of the web relies on.**

- **GET** — read. Should never modify state. Safe to retry. Cacheable.
- **POST** — create / submit. Modifies state. Not safe to retry blindly (might create duplicates).
- **PUT** — replace a resource entirely. Idempotent (calling it 5 times = calling it once).
- **PATCH** — partial update. Often used like PUT in practice; spec is fuzzier.
- **DELETE** — remove a resource. Idempotent (deleting something already deleted is still "deleted").

Interview concept here is **idempotency**: repeating the same operation has the same final effect as doing it once.

- An operation is idempotent if making the same request multiple times leaves the resource in the same final state as making it once
- GET, PUT, DELETE are idempotent. POST is not.
- Idempotent operations are generally safer to retry because **repeating the same request should not apply the effect twice**

### Status codes

- **1xx** — Informational. Rare in app code. Skip.
- **2xx** — Success. The request worked.
- **3xx** — Redirection. The thing you wanted is somewhere else (or hasn't changed).
- **4xx** — Client error. *You* (the requester) did something wrong.
- **5xx** — Server error. *The server* did something wrong.

### Headers worth knowing

- **Content negotiation:** `Content-Type`, `Accept` -- what format the body is/should be
- **Auth:** `Authorization`, `Cookie`
- **Caching:** `Cache-Control`, `ETag`
- **CORS:** `Origin`, `Access-Control-Allow-Origin`
- **Routing/identity:** `Host` (which virtual host on the server), `User-Agent` (who is calling)

---

## Stage 5: Server-Side Processing

- [TIMELINE] - the browser's request has now arrived at the server

### Path inside the data centre

```
Internet
   ↓
[ Load Balancer ]    ← receives request, picks an app server
   ↓
[ Reverse Proxy ]    ← (often combined with LB) — TLS termination, routing, header manipulation
   ↓
[ App Server ]       ← your actual code runs here (Node, FastAPI, Rails, etc.)
   ↓        ↓
[ Cache ]  [ Database ]
(Redis)    (Postgres/etc)
```

### What each layer does

- **Load Balancer** -- sits in front of app servers, distributes incoming requests across them
  - also where **TLS termination** typically happens
- **App Server** -- runs your actual app code. Receives the request, parses it, routes it to the right handler, executes business logic, returns a response
  - the box you write code in every day
- **Cache (Redis/Memcached)** -- checked *before* the database for hot data. If it's in the cache, app server returns it immediately and skips the db
  - caching exists because db's are generally slow and expensive compared to in-memory key-value stores
- **Database (Postgres/MySQL/etc.)** -- the source of truth
  - slow compared to cache, but durable, queryable, and consistent

### Senior-level insight

Every box in the above diagram is a potential bottleneck and potential point of failure, for example:

- **LB:** can it handle the incoming connection rate? Does it itself become a single point of failure?
- **App server:** are workers exhausted? CPU-bound? Waiting on slow downstream calls?
- **Cache:** hit rate dropping? Hot key? Stampede?
- **Database:** query time growing? Connection pool exhausted? Replica lag?

### TLDR Stage 5 Summary

- **Modern web requests pass through Load Balancer → App Server → Cache → Database**, with the LB typically also handling TLS termination.
- **Cache is checked before the database** — that's the whole point of having a cache layer.
- **Each box is a potential bottleneck**, and "where does this break first?" is the senior-flavor question that walks this diagram.

---

## Stage 6: HTTP Response + Browser Render

- [TIMELINE] - the server has done its work. It now sends an HTTP response back through the same TCP+TLS connection the client opened
- The response has the **same structure as the request**: a status line, headers, blank line, body

Example:

```http
HTTP/1.1 200 OK
Content-Type: text/html; charset=utf-8
Content-Length: 4827
Cache-Control: max-age=3600
Set-Cookie: session_id=xyz789; HttpOnly; Secure
ETag: "a1b2c3d4"

<!DOCTYPE html>
<html>
  <head>...</head>
  <body>...</body>
</html>
```

### What the browser does with the HTML

- The moment bytes arrive, the browser begins **parsing the HTML** -- it doesn't wait for the whole file
- As it parses, it builds the **DOM** -- the tree representation of the HTML structure
- While parsing, it encounters references to other resources, e.g.:

```html
<link rel="stylesheet" href="style.css">   <!-- fetch CSS -->
<script src="app.js"></script>             <!-- fetch JavaScript -->
<img src="hero.jpg">                       <!-- fetch image -->
<link rel="preconnect" href="...">         <!-- establish a connection to a domain we'll need soon -->
```

- **Each of these triggers another HTTP request** -- which means Stages 1-5 happen again for each resource
  - why a "single page load" might have 50-100 requests in practice

### Render-blocking resources

Two kinds of resources **block rendering**:

1. **CSS in `<head>`** -- the browser can't paint until it knows what it's supposed to look like
2. **Synchronous `<script>` in `<head>`**
   - by default, when the parser hits a script tag, it **stops parsing**, fetches the script, executes, then resumes
   - fix is to use `<script async>` or `<script defer>`

### "Page load complete" is a timeline, not an event

When you hear "the page is slow" the right first question is *"slow at which milestone?"*

### async vs defer

| Tag | Behavior |
|---|---|
| `<script>` (default) | Parser stops. Download. Execute. Resume parsing. **Blocks rendering.** |
| `<script async>` | Download in parallel with parsing. Execute as soon as it's downloaded — interrupts parsing whenever that happens. Order **not** guaranteed if multiple async scripts. |
| `<script defer>` | Download in parallel with parsing. Execute after the DOM is fully parsed, just before `DOMContentLoaded`. Order **guaranteed** — defer scripts run in document order. |

**When to use which:**

- **`async`** -- for fully independent scripts that don't depend on the DOM or other scripts. Canonical use case: analytics, ad pixels (fire-and-forget).
- **`defer`** -- for scripts that need the DOM ready and/or need to run in a specific order. Canonical use case: jQuery and anything that depends on it.
- **Safe default if unsure: `defer`.** Almost never wrong.

### TLDR Stage 6 Summary

1. **HTTP responses mirror requests**
2. **HTML parsing is incremental** -- browser works on bytes as they arrive
3. **Sub-resources trigger more HTTP requests**
4. **CSS and sync script block rendering** -- use `async`/`defer` or move to end of `<body>`
5. **"Loaded" is a timeline, not an event**
