# Load Balancing & Networking

## What a Load Balancer Does and Where It Sits

- [Scenario] - Your app is getting enough traffic that one server can't handle it. You've scaled horizontally - you now have 4 identical app servers
- [Problem] - Users send requests to a single address (your domain). Something needs to sit in front of those 4 servers and decide which one handles each request
  - This is the job of a load balancer. It is the traffic cop
- An LB makes pre-request decisions in real time with full visiblity into backend health and load (unlike DNS which just routes traffic blindly)
- **Client -> Load Balancer -> one of N backend servers**

- Where it typically sits:
  - **Between the internet and your app servers** (most common - this is the "front door" LB)
  - Can also sit between app servers and databases, or between any two tiers of your stack
  - In cloud environments, this is usually a managed service (AWS ALB/NLB, GCP Cloud Load Balancer) - you don't run your own

- Key idea: the client has no idea there are multiple servers behind the LB, it just talks to one address and hte LB handles routing

## Load Balancing Algorithms

- The LB gets a request, how does it pick one? There are 4 main strategies:
  1. **Round-Robin** -- simplest possible: go in order. Request 1 -> Server A, Request 2 -> Server B, Request 3 -> Server C and cycle through. Con: assumes all requests are equal cost and all servers equal capacity — doesn't adapt to real load.
  2. **Weighted Round-Robin** -- same rotation, but some servers get more turns. Con: weights are static — pre-configured, not reactive to real-time load. Doesn't adapt if a high-weight server gets slammed.
  3. **Least Connections** -- send the request to whichever server currently has the fewest active connections. Adapts to reality — if one server is slow or handling expensive requests, it accumulates connections and the LB routes away from it.
  4. **Consistent Hashing** -- hash something about the request (e.g. user ID) and map it to a server. Same user always hits the same server. Pro: great for stateful workloads or local caching — if Server A always handles User 123, it can cache that user's data locally. Con: when a server goes down, its users must be redistributed. Naive hashing redistributes everyone; consistent hashing (ring approach) only redistributes the dead server's users. You'll see this again in database sharding.

## Session Stickiness

- Sometimes you need the same user to keep hitting the same server across multiple requests. That's **stickey sessions**
- Why? If a server stores session state locally (e.g. shopping cart in memory or a websocket), sending the next request to a different server means the server has no idea who the user is
- **How it works:**
  - The LB tracks which server a user was assigned to (usually via a cookie or IP) and keeps routing that user to the same server
- **The trade-off:**
  - **Pro:** Simple way to handle server-local state
  - **Con:** Defeats the purpose of load balancing. Server A accumulates all the "sticky" power users, it gets overloaded while B/C/D sit idle. If server A dies, users lose all their state

- **The better answer:** Instead of sticky sessions, **externalize your state**
  - Put sessions in Redis, carts in a db
  - Now any server can handle any request
  - Stateless servers + external state store pattern is a pattern that scales
- **When sticky sessions are still OK:** legacy apps you can't refactor, or short-lived affinity where teh cost of externalizing isn't worth it

## Reverse Proxy vs. Load Balancer

- **Reverse proxy:** a server that sits between your clients and your backend, acting on behalf of the backend. The client talks to the proxy, the proxy talks to your server(s). The client never knows the backend's real address
  - What a reverse proxy can do:
    - **SSL termination** -- handles TLS so your app servers don't have to
    - **Compression** -- gzips responses before sending to client
    - **Caching** -- serves static assets without bothering the backend
    - **Security** -- hides backend IPs, blocks malicious requests
    - **Routing** -- sends /api requests to one service, /images to another

- **Load balancer:** distributes traffic across multiple servers

**The overlap:** a reverse proxy can load balance if you put multiple servers behind it. A load balancer is a type of reverse proxy. In practice, tools like **Nginx** do both - it's a reverse proxy that an also load balance

- Clean mental model:
  1. **1 backend server** --> you still might want a reverse proxy (for SSL, caching, security)
  2. **Multiple backend servers** --> you need load balancing, and your reverse proxy probably does it
  3. **At scale** --> you might have a dedicated LB (like AWS ALB) in front, plus Nginx as a reverse proxy on each server

"A reverse proxy is about what sits in front of your servers. Load balancing is about distributing across them. Most real tools do both"

## API Gateways

- An API gateway is a reverse proxy with app-level smarts bolted on. It's the single entry point for all client requests, but instead of just forwarding traffic, it handles cross-cutting concerns so your services don't have to

- **What an API Gateway does:**
  - **Authentication/authorization** -- validates JWTs or API keys before the request ever reaches your service
  - **Rate limiting** -- "this user gets 100 requests/min" enforced in one place
  - **Request routing** -- /users -> User Service, /orders -> Order Service, /search -> Search Service
  - **Protocol translation** -- client speaks REST, backend service speaks gRPC
  - **Logging/metrics** -- one place to observe all traffic

- **Where it sits:**
  - **Client -> Public LB -> API Gateway cluster -> Backend Services**
  - The gateway itself is a horizontally scaled service. It runs on N identical instances for availability and throughput. A public-facing LB distributes traffic across those instances — for self-hosted gateways (Kong, Traefik, Envoy) you provision this LB yourself. For managed gateways (AWS API Gateway) Amazon provisions it for you — the LB is still there, just abstracted away.

- **When you need one:**
  - Microservices architecture -- without a gateway, every client needs to know the address of every service. The gateway gives them one door
  - Public APIs -- rate limiting, auth, and key management in one place
  - Mobile/web BFF (backend for frontend)
  - When you need cross-cutting concerns (auth, rate limiting) in one place rather than duplicated in every service

- **When you don't:**
  - Monolith with one backend -- a reverse proxy covers you
  - Small number of services where an ALB with path-based routing to target groups is simpler and sufficient. The gateway earns its complexity when you need things like rate limiting and centralized auth, not just because you have multiple services.

- Real world tools: AWS API Gateway, Kong, Traefik

### How Gateway Instances Work

The gateway is a **shared, replicated layer** that knows about all services. Its horizontal scaling is for its own HA and throughput — not one gateway per service.

Two layers of "1 of N" selection happen on every request:
1. **Public LB → gateway instance** — doesn't matter which, they're all identical
2. **Gateway → service instance** — path determines the service, internal LB picks the instance

```
Client
  │
  ▼
Public LB  ← distributes across gateway instances
  │
  ├──► Gateway #1 ─┐
  ├──► Gateway #2 ─┤  all identical, all know about all 3 services
  └──► Gateway #3 ─┘
                   │
                   │  gateway routes by path, then picks instance
                   │
       ┌───────────┼───────────┐
       ▼           ▼           ▼
   User Svc   Restaurant   Order Svc
   [U1,U2,U3] [R1,R2]      [O1,O2,O3,O4]
```

**Key rule:** There is one gateway — one codebase, one config, one logical service. What gets horizontally scaled are **instances** of that single gateway (think: multiple Docker containers running the same image). Whether those instances are managed for you (AWS API Gateway) or provisioned manually (Kong in Docker Compose, gateway pods in Kubernetes), they are all clones of the same thing. "One gateway per service" is the anti-pattern — that would mean three separate gateway configs, each only knowing about one service, which forces the client to know which gateway to call for which operation and duplicates auth/rate limiting three times.

