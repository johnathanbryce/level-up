# Message Brokers — Vocabulary Pass

Role 3 (WARP) explicitly names message brokers. Roles 1 + 2 don't, but everything at Remitly's scale uses them somewhere. Goal: **nod intelligently.**

---

## What a message broker is (canonical definition)

A message broker is a middleman service that lets producers send messages without knowing who consumes them. **Decoupling** — producers and consumers don't need to be online at the same time, scale together, or know each other exist.

The three things they buy you:

1. **Decoupling** — services don't have to talk to each other synchronously.
2. **Resilience** — if a consumer goes down, messages buffer in the broker until it's back up.
3. **Replay** — you can re-read past messages to rebuild state or reprocess events.

---

## The four you should recognize

### Kafka

The dominant open-source streaming broker. **Ordered, partitioned, durable.** Producers write to topics; topics are split into partitions; consumers read in order *within a partition*. Massive throughput (millions of msgs/sec) and long retention (days, or forever if configured).

Use cases: event sourcing, audit logs, stream processing pipelines, change-data-capture.

### Kinesis

AWS's managed version of Kafka. Similar mental model: streams, shards, ordered reads, replay. Lighter than self-hosted Kafka because AWS manages the cluster. Less powerful, fewer knobs.

**Likely Remitly choice if Role 3 mentions a broker** — they're AWS-heavy.

### SQS

AWS's managed queue. **Unordered (standard) or FIFO (ordered).** No long retention by default — messages live until consumed (or hit a 14-day max). No replay.

Use cases: task queues, background jobs, simple producer/consumer decoupling.

### SNS

AWS's managed pub/sub. **One message, many subscribers.** Often pairs with SQS — SNS fans out to multiple SQS queues for different downstream consumers.

---

## Kafka vs SQS — when to reach for which

- **Kafka / Kinesis:** when you need ordering, replay, long retention, or stream processing.
- **SQS:** when you just need a simple queue with workers pulling jobs.

The mental shortcut: **Kafka is a log; SQS is a queue.** Kafka remembers everything; SQS forgets after consumption.

---

## Vocabulary worth knowing

- **Topic / Stream** — the named channel messages flow through.
- **Partition / Shard** — sub-stream within a topic. Each partition is ordered; across partitions, no ordering.
- **Consumer group** — set of consumers that share work on a topic.
- **Offset** — a consumer's position within a partition. Consumers track their own offsets.
- **At-most-once / At-least-once / Exactly-once** — delivery guarantees. Exactly-once is famously hard and usually achieved with at-least-once + idempotent consumers.
- **Consumer lag** — how far behind consumers are relative to the producer. Key operational metric.

---

## Likely recruiter prompts + canonical answers

- **"Have you worked with Kafka or Kinesis?"** → "Not hands-on, but I know the mental model — durable ordered streams, partitioned for scale, consumers read at their own pace. SQS is the simpler queue cousin in the AWS world. The broader pattern of decoupling services through async messaging is the part I'm strongest on conceptually."
- **"What's the difference between Kafka and a regular queue?"** → "Kafka is more like a durable, replayable log — messages stick around after consumption, multiple consumers can read independently, ordering is preserved within a partition. A queue like SQS is more transient — once consumed, the message is gone."
- **"Why would you reach for a message broker in the first place?"** → "To decouple services. Synchronous calls couple producers to consumers — if the consumer is down or slow, the producer is blocked. With a broker, the producer publishes and moves on; the consumer reads when it's ready. Plus you get retry, replay, and buffering for free."

---

## Gotchas

- **Ordering is per-partition, not global.** Across partitions, no order guarantee. Common interview trap.
- **Exactly-once is hard.** Most systems are at-least-once with idempotent consumers — which is *why* idempotency matters everywhere.
- **Consumer lag is a top operational metric.** If consumers can't keep up with producers, lag grows unbounded.
- **SQS standard ≠ SQS FIFO.** Standard is unordered + at-least-once + cheap. FIFO is ordered + exactly-once + slower + more expensive.
