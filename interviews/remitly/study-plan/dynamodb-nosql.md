# DynamoDB / NoSQL — Speaking Vocabulary

Highest-leverage Phase 1 topic. Role 2 (Customer Data Platform) explicitly names DynamoDB. You have no hands-on experience — goal is **20 seconds of intelligent recognition**, not depth.

---

## What it is

DynamoDB is **AWS's managed NoSQL database.** Key-value + document model. Single-digit millisecond latency at scale. You don't manage servers, replication, or sharding — AWS handles all of that. You define your access patterns and pay per request (or provisioned capacity).

NoSQL more broadly = "not SQL" — a family of databases that drop relational features (joins, schemas, ACID across rows) in exchange for **scale, flexibility, or both.** DynamoDB is in the key-value / document subfamily, alongside Redis (in-memory) and MongoDB (document).

---

## How it works (core mechanism)

### Partition key + Sort key

Every DynamoDB item has a **primary key**. Two flavors:

- **Partition key only** (simple). A hash function maps the key to a physical partition. Fast lookup by exact key.
- **Partition key + Sort key** (composite). Items with the same partition key are stored together, sorted by sort key. Enables range queries within a partition (e.g. *"all events for user X between dates Y and Z"*).

**This is the core mental model.** All access patterns flow from the primary key shape. If you don't know your access patterns up front, you'll regret your key choice.

### Single-table design (the controversial pattern)

In relational, you'd have many tables and join them. In DynamoDB, **joins don't exist** — you can't query across tables efficiently. So practitioners often put *everything* into one table and use generic partition/sort keys to encode multiple entity types.

Example: a single table where:
- `PK=USER#123, SK=PROFILE` is a user's profile
- `PK=USER#123, SK=ORDER#456` is an order belonging to that user
- One query for `PK=USER#123` returns both, sorted by SK.

It's controversial because it's powerful at scale but cognitively heavy — the schema lives in your application code, not the database. Reading someone else's single-table design is painful.

### Eventual consistency by default

DynamoDB replicates writes across multiple AZs. By default, reads are **eventually consistent** — you might read stale data for ~1 second after a write. You can opt into **strongly consistent reads** at 2x the cost and slightly higher latency.

---

## Why Remitly cares

Role 2 (CDP) JD names DynamoDB explicitly for *"high-throughput, high-availability services that manage customer data at scale."* Customer data + identity + compliance = exactly the workload DynamoDB excels at: known access patterns, massive read throughput, predictable performance, zero ops.

---

## When DynamoDB wins vs when Postgres wins

- **DynamoDB wins:** known access patterns, massive scale, single-key lookups, no ad-hoc analytics, you want zero ops.
- **Postgres wins:** complex queries, ad-hoc analytics, ACID across many entities, relational integrity matters, you don't know your access patterns yet.

Most teams start on Postgres and move parts of the workload to DynamoDB when scale/throughput becomes the constraint. Going the other direction (DynamoDB → Postgres) is rare and painful.

---

## Must-know vocabulary

- **Partition key (PK), Sort key (SK)** — primary key components.
- **GSI** (Global Secondary Index) — alternative access pattern; like a separate index table copied from the main one.
- **LSI** (Local Secondary Index) — alternative sort key within the same partition.
- **Hot partition** — a single partition getting disproportionate traffic. The classic DynamoDB failure mode.
- **Single-table design** — pattern of storing many entity types in one table.
- **TTL** — built-in time-to-live for items; auto-deletes expired ones.
- **DynamoDB Streams** — change-data-capture feed; trigger Lambdas on item changes.

---

## Likely recruiter prompts + canonical answers

- **"Have you worked with DynamoDB?"** → "No hands-on, but I know it conceptually — key-value NoSQL, partition + sort keys, single-table design as the dominant pattern. My SQL background is Postgres."
- **"How comfortable are you stepping into NoSQL work?"** → "Comfortable conceptually. The mental flip is access-patterns-first — you design queries before you model data — and I'd want to actually ship something on it to internalize it."
- **"What's the difference between SQL and NoSQL?"** → "SQL gives you relational integrity, joins, ad-hoc queries, and ACID across rows — but you pay for it at scale. NoSQL drops most of that in exchange for horizontal scalability and predictable performance. DynamoDB is on the scale side of that trade-off."

---

## Gotchas

- **No joins, ever.** If you need joins, you're either modeling wrong for DynamoDB, or using the wrong database.
- **Schema-on-read.** DynamoDB doesn't enforce a schema beyond the primary key. Your application is responsible for data integrity.
- **Hot partition problem.** If your partition key has uneven distribution (one mega-customer dominates traffic), that partition becomes a bottleneck. Mitigations: better key design, write sharding.
- **You're querying by KEY, not by content.** If you need "find all users where email contains 'gmail'," DynamoDB is the wrong tool — that's a full table scan.
