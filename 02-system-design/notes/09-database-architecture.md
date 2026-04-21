# Database Architecture

## SQL
- Relational databases (Postgres, MySQL) give you:   
    - **Schema enforcement** -- every row conforms to a defined structure 
        - The DB rejects bad data at the boundary
    - **ACID transactions** -- Atomicity, Consistency, Isolation, Durability 
        - When you transfer $100 from account A to account B, either both happen or neither does. No partial state
    - **Joins** -- query across related tables in a single operation
        - Users -> Orders -> Products in one query
    - **Strong consistency** -- after a write commits, every subsequent read sees it

- The cost: schema changes are painful at scale, and horizontal scaling is hard
- **Reach for SQL when**: your data has relationships, you need transactions (money, inventory, bookings), or data integrity is non-negotiable

## ACID 
- **Atomicity** -- a transaction is all-or-nothing
    - e.g. if you're transferring $100 (debit A, credit B), and the server crashes after the debit but before the credit - atomicity rolls the whole thing back. you should never be in a half-done state
- **Consistency** -- a transaction can only bring the DB from one valid state to another
    - constraints, foreign keys, rules - none of them get violated
- **Isolation** -- concurrent transactions don't step on each other
    - e.g. two users buying the last concert ticket simultaneously
- **Durability** -- once a transaction is committed, it survives crashes
    - the db has written to disk before telling you "success". if the power dies after your write commits, the data is still there



- On-liner: **ACID is the gaurantee that your DB won't lie to you or leave your data in a broken state, even when things go wrong**

## NoSQL
- NoSQL is a broad category, but four main types:
    - **Document stores** (MongoDB, Firestore) -- data stored as JSON-like documents. No fixed schema. Each document can have different fields
    - **Key-value stores** (Redis, DynamoDB) -- lookup a key, get back a value. Super fast and simple
    - **Wide-column stores** (Cassandra) -- optimized for massive write throughput and time-series data
    - **Graph Databases** -- nodes and edges, optimized for relationship traversal (social graphs, fraud detection)
- The reasons you reach for NoSQL:
    1. **Schema flexibility** -- your data shape changes frequently or varies per record (user profiles with wildly different fields)
    2. **Horizontal scale** -- NoSQL databases are designed to shard across many machines from the start
    3. **Write throughput** -- Cassandra can absorb millions of writes/sec that would crush Postgres
    4. **Simple access patterns** -- if you're always looking up by one key and never joining, a key-value store is faster and cheaper

- The cost: you give up joins, transactions, and strong consistency (usually)

## Database Indexing
- An index makes lookups fast. Without one, the DB Reads every row to find a match (full table scan)
- With one, it jumps straight to the data - like a phone book jumping to the right letter
- **Trade-off:** faster reads, slower writes. Every insert/update/delete must also update the index
- **Index when:**
    - you filter on this column frequently
    - you sort on it
    - it's used in joins
    - high cardinality (lots of unique values)
- **Don't index when:**
    - Write-heavy table -- too many indexes tanks write performance
    - Low cardinality -- a status column with 3 possible values isn't worth it
    - Speculative columns -- don't index everything just in case

## Database replication
- Replication solves: a single database is a point of failure. If it goes down, everything goes down. Can also be a bottleneck when read traffic gets heavy
- **How it works**: you have one **primary** (handles all writes) and one or more **replicas** (copies that stay in sync with the primary)
    - Writes go to primary only
    - Reads can go to either

App → writes → Primary DB
App → reads  → Replica 1, Replica 2, Replica 3

- **What you get:**
    - **Read scalability** -- spread read traffic across replicas instead of hammering one DB
    - **Fault tolerance** -- if the primary dies, promote a replica to primary (failover)
    - **Geographical distribution** -- put a replica closer to users in another region for lower latency

- **The catch** -- replicates are *slightly* behind the primary
    - This means reads from replicas might return stale data
    - This is **eventual consistency** in practice (CAP theorem)

- **Read-your-own-writes consistency:** -- a pattern whereby a if a user makes a write, route their subsequent reads to the primary database for a short window (or just that request) to ensure the database is 100% accurate (remember, replicas can sometimes lag behind, especially during spikes)

## Database Sharding
- Replication solves read scale
- Sharding solves **write scale and storage scale**
- [SCENARIO] -- the problem: your primary DB is getting hammered with writes. You' can't replicated your way out - all writes go to one machine. Eventually one machine isn't enough
- **What sharding does:** -- split the data horizontally across multiple databases. Each db (shard) holds a subset of the rows:

Shard 1: users with ID 1 - 10M
Shard 2: users with ID 10M - 20M
Shard 3: users with ID 20M - 30M

- Now writes are distributed; each shard handles its own slice

- The **shard key** is the column you split on, choosing it is the most important decision:
    - **Good shard key** -- high cardinality, evenly distributed, matches your access patterns (usually *user_id*)
    - **Bad shard key** -- low cardinality or uneven - you end up with one fat shard and two empty ones

- **Rule of thumb:** sharding is a last resort. Exhaust vertical scaling, indexing, caching, and read replicas first

## Connection Pooling
- Every time your app queries the DB, it needs a connection 
- Opening a connection is expensive -- TCP handshake, auth, setup
- Under load, if every request opens and closes its own connection, you'll exhaust the DB's connection limit and crater performance
- A **connection pool** maintains a set of open connections that get reused
    - Request comes in -> grab a connection from the pool -> run the query, return the connection
    - No open/close overhead
- The key config: **pool size**
    - Too small = requests queue up waiting 
    - Too large = db gets overwhelemd
    - Typtical starting point is 10 - 20 connections per app instance

## Polyglot Persistence
- Using multiple database technologies in one system, each chosen for what it's best at
- Ex: Postgres for users/oders, MongoDB for product catalog, Redis for sessions/cache, Elasticsearch for search
- One system, 4 databases, each doing what it's designed for

## Storage Types
- 3 types that come up constantly, especially in AI work:
    - **Object/Blob storage** e.g. S3, GCS
        - files, images, documents, model artifacts
        - cheap, infinitely scalable, not for structured data
    - **Block storage** e.g. EBS (AWS)
        - Attached disk for a server
        - Like a hard drive - your DB writes here
        - Low latency, tied to one machine
    - **File storage** e.g. EFS (AWS)
        - Shared filesystem multiple servers can mount simultaneously
        - Useful for shared assets across instances

