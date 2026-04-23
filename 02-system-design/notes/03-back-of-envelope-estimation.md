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

---

## Storage Estimation

```
storage per day  = items per day × size per item
storage per year = storage per day × 365
```
