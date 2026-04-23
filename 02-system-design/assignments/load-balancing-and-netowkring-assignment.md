Applied Scenario
You're designing a food delivery app (think Uber Eats). You have:

A web app and a mobile app
3 backend services: User Service, Restaurant Service, Order Service
Traffic is read-heavy (people browsing menus) with write spikes at meal times (lunch, dinner)
Questions:

1. Draw the request path from client to backend services — where does the LB sit, do you need an API gateway, and why?
2. The dinner rush just started. Order Service is getting hammered but Restaurant Service is fine. How does your LB setup help here?
3. A PM asks: "Can we add rate limiting so free-tier users can only place 5 orders per hour?" Where does that logic go and why?



# My Answer

Let's list what we know and what we will need to implement first:
- 3 backend services, so a load balancer is necessary. Nginx reverse proxy is not enough
- Because of these 3 defined services we should use an API Gateway as our reverse proxy. 
- Read heavy, so caching is necessary but out of the scope of this section

1. Request path drawing:

Client Req --> Load Balancer --> 1 of 3 API Gateway services --> 1 of the 3 services

- Load balancer routes the client request to the appropriate server which is "intercepted" by the API gateway first to authorize, apply rate limiting, etc.
- But, what is not clear in this applied scenario is if each backend service is horizontally scaled so we would need a load balancer to route traffic to, say, 1 of 4 available User Services or Restaurant Services?

2. Given that these are separate services, there is no point for an LB to route an Order service to a restaurant service. Goes back to my prior question from 1. which is I assume these services are horizontally scaled so the Load Balancer can route accordingly using Least Connections algorithm

3. Yes we absolutely can. The API Gateway can handle this for us smoothly. The request will contain the information necessary for us to determine whether a user is paid or free, and if the user is free we apply rate-limiting.

---

# Feedback & Corrected Answer

**Grade: B+.** Strong instincts, one architectural confusion, and a couple of places where you underestimated what you got right.

## What you nailed
- Correctly identified that 3 services = API gateway territory, not just a reverse proxy.
- Q3 is exactly right. Rate limiting at the gateway is the correct answer — the request has the user info, and you want this logic in one place, not duplicated in every service.
- Asked the right clarifying question about per-service horizontal scaling — that's senior-flavor instinct (ask for requirements instead of assuming).

## Q1 — Your original diagram was correct

`Client → LB → API Gateway → Services` is standard production practice. The gateway is itself a horizontally scaled service — it runs on multiple instances for availability and throughput. An LB in front of those instances is required. The only case where this LB is invisible is managed services like AWS API Gateway, where Amazon provisions it for you. For self-hosted gateways (Kong, Traefik, Envoy, Nginx) you provision it yourself. Your diagram stands.

Both LB layers exist in real systems:
- **Public-facing LB** in front of the gateway tier
- **Per-service LBs** between the gateway and each service's instances

One thing worth adding: "3 services = API gateway" is the easy answer, but the *real* justification here is the rate limiting (Q3) and centralized auth across web + mobile. An ALB with path-based routing to three target groups is a valid simpler alternative. The gateway earns its complexity because of those cross-cutting concerns, not just because you have multiple services.

## Q3 — one level deeper
Saying "the gateway handles rate limiting" is correct but incomplete. The counter must live in **Redis** (shared across all gateway instances). If you track in-memory per instance and have 4 gateways, a user gets 5 × 4 = 20 orders/hour, not 5. Shared state = shared store.

## Q2 — closer than you thought
Your answer was correct but buried. Clean version:

> "LB only helps within a service, not across services. If Order Service is hammered, you need more Order Service instances (horizontal scaling), and the LB in front of Order Service distributes across them. Restaurant Service isn't affected because it has its own LB and its own instances."

The missing piece: LB alone doesn't fix an overloaded service — **autoscaling** does. The LB distributes across whatever capacity exists; autoscaling adds capacity when load spikes. Together, the dinner rush gets absorbed.
