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

- **The fix: exponential backoff + jitter**
    - **Exponential backoff** -- wait longer each attempt, doubling:

        Attempt 1 fails → wait 1s
        Attempt 2 fails → wait 2s
        Attempt 3 fails → wait 4s
        Attempt 4 fails → give up

          - Purpose: space retries out so recovering services aren't slammed

  - **Jitter** -- add randomness to the wait. Instead of "wait 2s exactly", wait "1.5 - 2.5s random"
      - Without jitter, all clients that failed at the same moment wait the same 2s -> thunder herd just delayed by 2s
      - Jitter de-synchronizes clients so retries spread across the window
  
      - **Formula:** -- wait = min(base * 2^attempt, max_delay) + random_jitter

- **Bounds (always set these)**
    - **Max retries** -- e.g. 3 - 5 attempts (stops infinite loops)
    - **Max delay** -- e.g. 30s cap (stops waits from growing unboundedly)

- **Rule of thumb:** Retry only **idempotent** operations. Retrying a non-indempotent POST can create duplicates

## Chunk 2: Idempotency

### Definition
Operation is idempotent if running it multiple times = same result as running it once.

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
