# Back of Envelope Estimation - High Level

**QPS** -> Queries Per Second; a count of how many requests hit your system every second
- if your app gets 60 requests a minute, thats 1 QPS; 600 in a minute = 10 QPS
- QPS helps inform architecural decisions, for ex: do we need a load balancer? horizontal scaling? how many servers if we apply horizontal scaling?

**Estimating QPS from User Count**
- QPS = (daily active users x actions per user per day) / seconds in a day
- seconds in a day = ~ 100,000
- e.g. 200 daily users making 5 requests per day:
  -  200 x 5 = 1000 requests per day
  -  1000 / 100K seconds = 0.01 QPS

**Peak vs. Average Traffic**
- peak traffic is usually 2-3x above the average
- average 1,100 QPS - peak ~2,200 - 3,300 QPS

**Reads vs. Writes**
- **writes** are expensive
  - they hit the database, often need to be durable (written to disk), often update indexes, can't easily be cached
- **reads** are cheap
  - can be served from cache or read replicates and scale horizontally with ease
- this means that a system that is **read-heavy** and a system that is **write-heavy** need very different architectures
- typical ratio: most consumer systems are **read-heavy** often around 10:1 reads to writes.

**Storage Estimation**
- storage per day = items per day x size per item
- storage per year = storage per day x 365