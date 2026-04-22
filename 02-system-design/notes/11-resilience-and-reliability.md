# Resilience & Reliability

## Retries with Exponential Backoff

- Why retry at all?
  - Many failures in distributed systems are **transient** -- network blip, brief CPU spike
  - Retrying 100ms later often success. Giving up on the first failure = lost reliability for no reason

- Naive "junior level" retry:

        for attempt in range(3):
            try: return call_api()
            except: continue   # immediate retry

- Two problems with the above approach:
  1. **Thundering herd / retry storm:** 10K retries fail at once -> all retry at the same moment -> DDoS your own recovering service
  2. **Hammering a dying service:** immediate retries add load to a service that's already overloaded. Makes recovery slower, not faster

### The fix: exponential backoff + jitter

- **Exponential backoff** -- wait longer each attempt, doubling:

  Attempt 1 fails → wait 1s
  Attempt 2 fails → wait 2s
  Attempt 3 fails → wait 4s
  Attempt 4 fails → give up

      - Purpose: space retries out so recovering services aren't slammed

- **Jitter** -- add randomness to the wait. Instead of "wait 2s exactly", wait "1.5 - 2.5s random"
  - Without jitter, all clients that failed at the same moment wait the same 2s -> thunder herd just delayed by 2s
  - Jitter de-synchronizes clients so retries spread across the window
  - **Formula:** -- wait = min(base \* 2^attempt, max_delay) + random_jitter

### Bounds (always set these)

- **Max retries** -- e.g. 3 - 5 attempts (stops infinite loops)
- **Max delay** -- e.g. 30s cap (stops waits from growing unboundedly)

- **Rule of thumb:** Retry only **idempotent** operations. Retrying a non-indempotent POST can create duplicates

## Idempotency

- Operation is idempotent if running it multiple times = same result as running it once.

### Why it matters for resilience

- Retries + network uncertainty = duplicates are inevitable.
- Classic case: client POSTs, server processes, response lost, client retries.
  Without idempotency: charged twice / two orders / two emails.

### Idempotency by HTTP method

- GET — idempotent (reads don't mutate).
- PUT — idempotent ("set to value" → same final state).
- DELETE — idempotent (second call is a no-op).
- POST — NOT idempotent. Creates a new resource each call.

### Making POST safe: idempotency keys

- Client generates a UUID, sends as `Idempotency-Key` header.
- Server caches (key → result) for ~24h.
- Duplicate request returns cached response instead of re-executing.
- Canonical example: Stripe payment API.

### Key takeaway

Retry + idempotency is a package deal — you can't safely have one without the other.
At-least-once message queues (SQS, Kafka) REQUIRE idempotent consumers.

### Example of Idempotency Implementation
- [SCENARIO]: You're building a ride-share app. Rider taps "Book Ride" → mobile app sends POST to your backend → backend charges the card and dispatches a driver.
    - The app has flaky cell service. Sometimes the POST succeeds on the server but the response gets lost on the way back. The app auto-retries.

- **Implementation Strategy:**
    - Use Idempotency-Key for each client request
    - First time the key is seen: process the request normally, **cache the result keyed idempotency-key**, return response
    - **If a duplicate arrives:** cache hit, return cached response without re-executing

## Circuit Breaker 

### The problem retries don't solve
- Retries handle **transient** failures... but what if the downstream service is genuinely **down** - not a blip or a spike, but actually broken?
    - Your retries keep slamming it and your service's threads/connections pile up waiting on timeouts
    - This is **cascading failure**: one broken dependency takes down everything that depends on it

### The fix: fail fast when the downstream is known-**broken**
- Circuit breaker acts like an electrical fuse: when failures exceed a threshold, it **trips** -- subsequent requests fail immediately *without even attempthing* the downstream call
    - Your threads aren't stuck waiting on timeouts
    - The downstream service isn't getting hammered while it recovers
    - Your users get a fast failure or a degraded response, not a 30s-second hang

### Three states (the core mechanism)

- **CLOSED** -- normal operation. Requests flow through to the downstream. Breaker counts failures in the background. If failure rate crosses threshold -> trip to OPEN.
- **OPEN** -- tripped. Requests fail **immediately** without attempting the downstream. Gives the downstream breathing room to recover. Stays open for a cooldown period (e.g. 30s timer -- not a condition on traffic).
- **HALF-OPEN** -- cooldown elapsed, testing recovery. Let **ONE** probe request through.
    - Probe **succeeds** -> close the breaker. Normal traffic resumes. No human in the loop.
    - Probe **fails** -> back to OPEN. Another cooldown. Try again next window.

**Why HALF-OPEN is load-bearing:** without it, you'd need a human to manually decide when the downstream is healthy. Self-healing via automatic probing is the whole point. And just ONE probe -- not a flood -- because 1000 requests hitting a still-broken downstream = cascading failure all over again.

### What trips the breaker
- 2 common strategies:
        1. **Failure rate over a window** -- e.g. ">50 failures in the last 30 seconds" 
                - More robust, accounts for mixed success/failure traffic
        2. **Consecutive failures** -- e.g. "5 failures in a row"
                - Simple but noisy. One slow minute can trip you unnecessarily 

### Retries + Circuit Breaker together
- They're generally layered:
    - **Retries:** handle transient failures within a single request
    - **Circuit breaker:** handles systemic failures across many requests

[SUMMARY] - You retry each individual request (with backoff + jitter). You trip the breaker when aggregate fail rate tells you retrying isn't going to help

## Rate Limiting
- Any service exposed to the internet will see abuse: intentional attacks, buggy clients stu
- **Goal:** cap request volume per client, per endpoint, or globally

### Algorithm 1: Token Bucket (most common)
- Mental model: a bucket that holds **N tokens**. tokens refill at a steady rate (e.g. 10/sec = 10 req/sec sustained). Each incoming request consumes 1 token. Bucket empty -> request rejected
  
        Capacity: 20 tokens, refill 10/sec

        Second 0: bucket full (20 tokens). User sends 20 requests in 1 second — all succeed. Bucket: 0.
        Second 1: 10 tokens refilled. Bucket: 10.
        Second 2: 10 more refilled. Bucket: 20 (capped).

- **Key property:** **allows bursts up to bucket size, then smooths to refill rate**. Perfect for real-world traffic -- users load a page that fires 10 requests at once, then quiet for a minute

### Algorithm 2: Sliding Window
- Count requests in a moving time window (e.g. "<100 requests per 60s"). If count exceeds limit -> reject
    - **Simpler than token bucket**. No burst allowance - hit the limit, you're done for the window
    - Two variants: **log** (store every timestamp; precise but memory-heavy) and **counter** (approximation using fixed windows + math; cheaper, prod standard)

### Token bucket vs. sliding window - which to pick
- **Token bucket** -- when bursts are expected and OK. Real user traffic, API clients that batch requests
- **Sliding window** -- when you want a **hard cap** with no burst allowance. Expensive operations (LLM API calls, password resent emails, SMS re-sends)

### Where rate limiting thrives
- **API GAteway** -- most common. Centralizes limits across all service. One config, one place to enforce
- **CDN / edge** -- (Cloudflare) first line of defense against bots/DDoS before requests hit your infra
- **In-app** -- Redis as the counter store, since it's fast + atomic + shared across instances 

### What to rate limit on
- **Per-IP** -- simplest, but breaks behind NAT/corporate networks (500 office employees share 1 IP)
- **Per-user / API key** -- accurate, requires auth
- **Per-endpoint** -- login endpoint may need stricter limits (5/min) than public catalog (1000/min)
- Most real systems combine: per-user primary, per-IP fallback for unauthed traffic, per-endpoint overrides for sensitive routes

### Response **Pattern**
- Return a **HTTP 429 Too Many Requests** with a *Retry-After* header telling the client when they can try again:
  
            HTTP/1.1 429 Too Many Requests
            Retry-After: 30

            {"error": "rate_limit_exceeded", "retry_in_seconds": 30}

## Graceful Degradation
- Junior mindset: "service is up" or "service is down"
- Senior mindset: **real systems are partially functional most of the time**
    - A dependency is failing, a cache is cold, a feature is mibehaving - but most of the product still works
    - Your job is to **design for partial failure** so users can still accomplish their main goal
- **Graceful degradation** = server a reduced-but-functional experience when full functionality isn't available, instead of failing completely 

### Common degradation stratgies:
- **Fall back to cached data** -- primary source is down -> serve last-known-good from cache (slight stale data, page loads)
- **Fall back to defaults** -- can't compute personalized recommendations? show the popular/default list
- **Disable non-critical features** 
- **Read-only mode** -- primary db down, only replicas available? server reads, block writes
- **Partial response** -- user sends 3 API requests, 1 fails? return the 2 that worked and mark the one that failed as unavailable

### Anti-pattern to **avoid**
- "All-or-nothing" failure: one non-critical dep fails -> entire page fails

### Real world examples worth knowing
- Amazon checkout: if recommendations fail, checkout still works
- Twitter: feed personalization down -> fall back to chronological feed

### Interview usage
- When you're asked to design a system, name the critical path and explicitly identify what degrades gracefully. This is a senior signal:

*"The critical path here is search → product → cart → checkout. Recommendations, reviews, and related-items sections are non-critical — if those services fail or hit rate limits, we hide the widgets, cache the last-known-good result, and keep the funnel working. We don't want a recommendations outage to break checkout."*

