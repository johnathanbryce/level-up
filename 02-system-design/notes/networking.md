# Internet & Networking Fundamentals

**IP Address** -> unique numerical addressed assigned to every device on a network

- how devices find each other

**Port** -> a numbered channel on a single device

- one computer has one IP address but thousands of ports
- when a request arrives at a server, the port tells the OS which app should handle it
- e.g. HTTP traffic defaults to 80, HTTPS to 443, Postgres to 5432

Mental model: IP address as the building address (1189), port as the apartment number (903)

**DNS** -> DNS resolves domain names to IP addresses; its a chain of lookups, not a simple "middleman"

- It is a chain of cache lookups (browser -> OS -> resolver -> DNS hierarch)
- Results are cached with a TTL:
  - short TTL = faster failover, more lookups
  - long TTL = fewer lookups, slower failover

- Ex user visits "google.com"
  - Browser cache - your browser checks if it knows the IP
  - OS cache - if not, your operating system checks its own cache
  - Router cache
  - Recursive resolver (usually your ISP or something like Cloudflare) - this is the server that does the heavy lifting if no cache has the answer

**HTTP** -> rules used by web browsers and servers to communicate by sending requests and receiving responses

- HTTP is stateless -- each request is independent (server doesn't remember your prev request)
  - This is why we need cookies, JWT, etc. to maintain user state
- Request has headers and a body (GET requests do NOT have a body)
  - header and body are the context and the payload
- Request has a method and a path; GET /api/users/123
  - The method (GET, POST, PUT, DELETE, PATCH) plus the path is what tells the server what you want t do

**HTTPS/TLS**

- HTTPS is just HTTP running inside a TLs-encrypted connection (same requests, headers, bodies... just encrypted in transit)
- TLS = Transport Layer Security; solves 3 problems:
  - 1. Encryption
  - 2. Authentication - the server proves it's actually who it claims to be, via a certificate (prevents someone from impersonating google.com)
  - 3. Integrity - data can't be tampered in transit without detection

- TLS "handshake":
  - 1. client says "I want a secure connection" and shares what encryption it supports
  - 2. server responds with its certificate
  - 3. they agree on encryption keys
  - 4. now all http traffic flows encrypted through this tunnel

- TLS adds latency but much more robust security

**Web Request Lifecycle**

1. DNS resolution - browser looks up google.com --> gets IP address (cache chain: browser -> OS -> resolver -> DNS hierarchy)
2. TCP connection - browser opens a connection to that IP on port 443
3. TLS handshake - establishes encrypted tunnel (cert verification, key exchange)
4. HTTP request - browser sends GET / HTTP/2 with headers through the encrypted tunnel
5. Server processing - request hits load balancer/reverse proxy (nginx), routes to app server, server processes and builds a response
6. HTTP response - server sends back status code (200), headers, and body (ex. HTML in this case)
7. Browser renders - pareses HTML, fetches additional resources (CSS, JS, images - each may trigger new requests), paints the page

Summary: DNS -> TCP -> TLS -> HTTP -> Server -> Response

**WebSockets**

- Normal HTTP is request-response: client asks, server answers, connection is done
- WebSockets solves this lack of real-time features: it starts as a normal HTTP request, then the connection stays open. Both client and server can send data to each other at anytime - bidirectional, persistent connection
- Best use cases:
  - live chat, real-time notifications, collaborative editing, gaming

**SSH**

- it's a protocol for securely connecting to remote machines
- encrypts the connection and auth's via key pairs or passwords
