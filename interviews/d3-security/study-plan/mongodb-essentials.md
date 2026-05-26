# MongoDB / NoSQL — High-Level Primer

> **Status:** Heavily trimmed 2026-05-25 (John's call — not D3-test-relevant). Kept as a vocab-recognition pass only.
> Goal: be able to define NoSQL vs SQL and Mongo's core shape in one breath. Not architect-level.

---

## What NoSQL means

- **NoSQL** = "not only SQL." Umbrella term for databases that don't fit the rigid relational/tabular SQL model.
- Four broad families (recognize the names, don't memorize all):
  - **Document** — JSON-like records (MongoDB, Couchbase, DynamoDB)
  - **Key-value** — string → blob (Redis, DynamoDB)
  - **Column-family / wide-column** — Cassandra, HBase
  - **Graph** — nodes + edges (Neo4j)
- MongoDB is the most common **document database.**

## How a document DB differs from a relational DB

| | Relational (Postgres / MySQL) | Document (MongoDB) |
|---|---|---|
| **Unit of storage** | Row in a table | Document in a collection |
| **Schema** | Fixed at table-creation (ALTER required to change) | Flexible — each document can have different fields |
| **Joins** | First-class (`JOIN`) | Limited (`$lookup`); often avoided by embedding |
| **Transactions** | ACID by default across rows + tables | ACID per-document; multi-document since v4.0 (less battle-tested) |
| **Scale** | Vertical (scale up the server) | Horizontal (shard across nodes) is native |

## Mongo core vocabulary (1-line each)

- **Document** — JSON-like record. The row equivalent.
- **Collection** — group of documents. The table equivalent.
- **Embed** — nest a sub-document inside its parent (e.g. orders array inside a user doc). Fast reads; denormalized.
- **Reference** — store an ID pointing to a separate document. More normalized; needs a join (`$lookup`).
- **Aggregation pipeline** — series of stages that transform documents (`$match`, `$group`, `$project`, `$lookup`, etc.). The "query language" for non-trivial reads.

## The two "rules" worth remembering

1. **`$match` first in aggregation pipelines** — filter early so smaller data flows through later stages.
2. **ESR for compound indexes** — field order in a compound index: **E**quality first, **S**ort next, **R**ange last. Wrong order = index unused or partial.

## When NoSQL (Mongo) wins vs SQL (Postgres) wins

- **NoSQL wins:** schema changes often, deeply nested data accessed together, need horizontal sharding from day 1, write throughput at scale (logs, events, sessions).
- **SQL wins:** complex multi-entity joins, ACID across many tables, ad-hoc analytics, mature ecosystem for BI / reporting.
- **Most teams start with Postgres** and add Mongo / Redis / etc. for specific workloads — not the other way around.

## Killer interview line

*"MongoDB is a document database — flexible schema, JSON-like documents in collections, horizontal sharding native. Two rules worth knowing: `$match` first in aggregation pipelines, and ESR (Equality → Sort → Range) for compound indexes. Use Mongo when the schema is fluid or data is naturally nested; Postgres when you need joins, ACID across entities, or ad-hoc analytics."*
