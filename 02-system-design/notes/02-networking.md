# Internet & Networking Fundamentals

## 8 Networking Topics

1. IP Address
2. Port
3. DNS
4. HTTP
5. HTTPS / TLS
6. Web Request Lifecycle
7. WebSockets
8. SSH

---

## IP Address

A unique numerical address assigned to every device on a network.

- How devices find each other.

## Port

A numbered channel on a single device.

- One computer has one IP address but thousands of ports.
- When a request arrives at a server, the port tells the OS which app should handle it.
- e.g. HTTP traffic defaults to 80, HTTPS to 443, Postgres to 5432.

**Mental model:** IP address as the building address (1189), port as the apartment number (903).

---

## DNS

DNS resolves domain names to IP addresses; it's a chain of lookups, not a simple "middleman."

- It is a chain of cache lookups (browser → OS → resolver → DNS hierarchy).
- Results are cached with a TTL:
  - **Short TTL** = faster failover, more lookups
  - **Long TTL** = fewer lookups, slower failover

### Example: user visits `google.com`

1. **Browser cache** — your browser checks if it knows the IP
2. **OS cache** — if not, your operating system checks its own cache
3. **Router cache**
4. **Recursive resolver** (usually your ISP or something like Cloudflare) — this is the server that does the heavy lifting if no cache has the answer

---

## HTTP

The rules used by web browsers and servers to communicate by sending requests and receiving responses.

- HTTP is **stateless** -- each request is independent (server doesn't remember your previous request)
  - This is why we need cookies, JWT, etc. to maintain user state
- A request has **headers** and a **body** (GET requests do NOT have a body)
  - Headers and body are the *context* and the *payload*
- A request has a **method** and a **path**, e.g. `GET /api/users/123`
  - The method (GET, POST, PUT, DELETE, PATCH) plus the path is what tells the server what you want to do

---

## HTTPS / TLS

- HTTPS is just HTTP running inside a TLS-encrypted connection (same requests, headers, bodies... just encrypted in transit)
- TLS = **Transport Layer Security**; solves 3 problems:
  1. **Encryption**
  2. **Authentication** — the server proves it's actually who it claims to be, via a certificate (prevents someone from impersonating google.com)
  3. **Integrity** — data can't be tampered with in transit without detection

### TLS handshake

1. Client says "I want a secure connection" and shares what encryption it supports
2. Server responds with its certificate
3. They agree on encryption keys
4. Now all HTTP traffic flows encrypted through this tunnel

TLS adds latency but provides much more robust security.

---

## Web Request Lifecycle

1. **DNS resolution** — browser looks up `google.com` → gets IP address (cache chain: browser → OS → resolver → DNS hierarchy)
2. **TCP connection** — browser opens a connection to that IP on port 443
3. **TLS handshake** — establishes encrypted tunnel (cert verification, key exchange)
4. **HTTP request** — browser sends `GET / HTTP/2` with headers through the encrypted tunnel
5. **Server processing** — request hits load balancer / reverse proxy (nginx), routes to app server, server processes and builds a response
6. **HTTP response** — server sends back status code (200), headers, and body (e.g. HTML in this case)
7. **Browser renders** — parses HTML, fetches additional resources (CSS, JS, images — each may trigger new requests), paints the page

**Summary:** DNS → TCP → TLS → HTTP → Server → Response

---

## WebSockets

- Normal HTTP is request-response: client asks, server answers, connection is done
- WebSockets solves this lack of real-time features: it starts as a normal HTTP request, then the connection stays open. Both client and server can send data to each other at any time — **bidirectional, persistent connection**
- Best use cases:
  - Live chat, real-time notifications, collaborative editing, gaming

---

## SSH

- A protocol for securely connecting to remote machines
- Encrypts the connection and authenticates via key pairs or passwords
