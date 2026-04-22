# Message Queues & Async Processing

## 5 Queue Topics

1. Why Async Processing Matters
2. Producer-Consumer Pattern
3. Delivery Guarantees
4. Common Tools
5. When Queues vs. Synchronous

---

## Why Async Processing Matters
[SCENARIO] Imagine your food delivery app. User places an order. Your API needs to:

1. Save the order to the DB
2. Notify the restaurant
3. Notify a nearby driver
4. Send the user a confirmation email
5. Update analytics

If you do all of this synchronously — in a single request — the user waits for all 5 steps before getting a response. Steps 2-5 could take seconds. One of them could fail and crash the whole request.

The alternative: Save the order, immediately return 200 OK to the user, then drop a message onto a queue. Separate workers pick up that message and handle steps 2-5 independently, at their own pace, without blocking the user.

That's a message queue. A middleman buffer that decouples "I need this done" from "I'm doing it now."

- Two sentence pitch for queues: **speed** (user gets a response immediately) + **reliability** (a failure in step 4 doesn't undo steps 1 -3)

## Producer-Consumer Pattern
- The mental modal has 3 parts: **Producer -> Queue -> Consumer**
    - **Producer:** the thing that creates work and drops it on the queue (your API server after saving the order)
    - **Queue:** the buffer that holds messages until someone is ready to process them (Redis, RabbitMQ)
    - **Consumer:** the worker that picks up messages and does the actual work (notification service, email service, analytics service)
- Key properties:
    - Producer and consumer are **decoupled** -- neither knows about the other directly
    - The queue **persists** messages -- if the consumer crashes, the message isn't lost, it's still in the queue
    - You can have **multiple consumers** -- spin up 10 email workers if the queue is backed up, scale back down when it clears

## Delivery **Gaurantees**
- Production systems default to **at-least-once**: the queue holds a message until the consumer acknowledges it. If the consumer crashes before acking (acknowledging), the message gets redelivered
    - This means your consumer might process the same message twice
    - The fix: make your consumer **idempotent** -- processing the same message twice produces the same result as once.
        - For the email ex: track an email_sent flag per order ID. Before sending, check if it's already been sent. Duplicate delivery = no-op
- **Idempotent:** running an operation multiple times produces the same result as running it once
    - The operation CAN run multiple times - the point is the outcome doesn't compound

## Common Tools
- **SQS (AWS)** -- managed queue, fully serverless, default choice for AWS
- **RabbitMQ**
- **Redis Streams**
- **Kafka**

## When Queues vs. Synchronous
- Use a queue when:
    - The work doesn't need to finish before the user gets a response (email, notifications, analytics)
    - The downstream service is slow or unreliable
    - You need to absorb traffic spikes (e.g. Black Friday order burst)
- Stay synchronous when:
    - The user needs the result immediately (login, payment confirmation, search results)
    - Failure should block the operation (can't place an order if payment fails)


 
