# Back-of-Envelope Estimation

High-level napkin math for sizing systems before designing them.

## 4 Estimation Techniques

1. QPS (Queries Per Second)
2. Peak vs Average Traffic
3. Reads vs Writes
4. Storage Estimation

---

## QPS (Queries Per Second)

A count of how many requests hit your system every second.

- If your app gets 60 requests a minute, that's 1 QPS; 600 in a minute = 10 QPS
- QPS helps inform architectural decisions, for example: do we need a load balancer? Horizontal scaling? How many servers if we apply horizontal scaling?

### Estimating QPS from user count

```
QPS = (daily active users × actions per user per day) / seconds in a day
```

- Seconds in a day ≈ **100,000**
- Example: 200 daily users making 5 requests per day:
  - 200 × 5 = 1,000 requests per day
  - 1,000 / 100K seconds = **0.01 QPS**

---

## Peak vs Average Traffic

- Peak traffic is usually **2-3× above the average**
- Example: average 1,100 QPS → peak ~2,200 - 3,300 QPS

---

## Reads vs Writes

- **Writes are expensive**
  - They hit the database, often need to be durable (written to disk), often update indexes, can't easily be cached
- **Reads are cheap**
  - Can be served from cache or read replicas and scale horizontally with ease
- This means a system that is **read-heavy** and a system that is **write-heavy** need very different architectures
- **Typical ratio:** most consumer systems are read-heavy, often around 10:1 reads to writes

### Splitting a ratio

Given total QPS and a ratio (e.g. 10:1 reads:writes), how to split:

- Total parts = X + Y. For 10:1, that's **11 parts**.
- One part = total QPS ÷ parts. For 2,000 QPS ÷ 11 ≈ **182 QPS per part**.
- Reads = 10 parts ≈ 1,818 QPS. Writes = 1 part ≈ 182 QPS.
- Napkin shortcut: round to ~1,800 reads/sec, ~200 writes/sec. Order of magnitude is what matters.

### Read-heavy architecture (the canonical 3-tier stack)

For content-heavy systems (blogs, news, e-commerce catalogs):

1. **CDN at the edge** — caches rendered HTML, images, static assets close to the user (Cloudflare, Fastly, CloudFront). Catches the bulk of read traffic before it ever reaches app servers.
2. **Redis cache layer** — for dynamic data that survives the CDN: comment threads, user profile data, trending posts. App-server-adjacent.
3. **Read replicas** at the DB layer — for the reads that DO make it to the database. N read replicas behind a load balancer; only the primary handles writes.

**Consistency cost:** eventual consistency. Stale reads from CDN/Redis/replicas. TTL trade-offs — longer TTL means more cache hits but more staleness; shorter TTL means fresher data but less cache benefit.

### Why writes can't horizontally scale like reads

| Reason | Mechanism |
|---|---|
| **Single source of truth** | Every write must hit the primary DB. If you had 5 DBs, which one has the latest version of row 123? Distributed consensus is expensive. |
| **Durability cost** | Writes must persist to disk (WAL + fsync), often replicated synchronously before acknowledging. Blocking. Reads have no fsync. |
| **Index updates** | Every write updates ALL indexes. 5 indexes = 5 extra writes per logical write. |
| **Lock contention** | Writes take locks to prevent concurrent corruption. Concurrent writes on the same row serialize. Reads use shared locks or MVCC (cheap). |
| **Only true escape: sharding** | Partition across N primary DBs by a shard key. Hard problem — cross-shard transactions, hot shards, rebalancing, picking the right shard key. |

**Interview one-liner:** *"Reads scale by replication — copy the data, point readers at copies. Writes can't replicate that way because you'd lose your single source of truth. The only horizontal scale path for writes is sharding, which has its own pile of trade-offs."*

---

## Storage Estimation

```
storage per day  = items per day × size per item
storage per year = storage per day × 365
```

### Unit ladder

Always convert UP to GB / TB / PB before drawing conclusions. Magnitude matters more than the raw MB number.

- 1,000 MB = 1 GB
- 1,000 GB = 1 TB
- 1,000 TB = 1 PB

**Worked example:** 2M photos/day × 1.5 MB each
- per day: `2M × 1.5 MB = 3,000,000 MB = 3,000 GB = 3 TB`
- per year: `3 TB × 365 = 1,095 TB ≈ 1.1 PB`
- 5 years: `1.1 PB × 5 ≈ 5.5 PB`

### Where this storage actually lives

For massive blob data (photos, videos, model artifacts) at TB+/PB+ scale, the canonical answer is **object storage** (S3, GCS, Azure Blob), NOT a relational database.

- The DB stores **metadata + a reference key** (e.g. `photo_url` or `s3_key` ≈ 100 bytes/photo). NOT the binary data itself.
- Object storage handles the blobs.
- CDN sits IN FRONT of object storage to cache hot blobs at the edge.

**Why object storage:**

- Cheap per GB at massive scale
- Durable (S3: 11 9s of durability)
- Infinitely scalable
- Integrates with CDNs natively

**Trade-offs:**

- Higher latency than block storage (EBS) for random access
- Not transactional — no ACID across multiple blobs

**Pattern:** *DB stores the reference, S3 stores the bytes, CDN serves the bytes.*
