# Core Concepts

### Four Key Concepts:

1. Vertical vs. Horizontal scaling
2. CAP theorem
3. Consistency models (strong vs. eventual)
4. Latency vs. throughput

---

## Vertical vs. Horizontal Scaling
- [Situation] - your app is slow and you need more capacity, you have two basic options:
    1. **Vertical scaling** - make your existing machine bigger: more CPU, RAM, fast disk
    2. **Horizontal scaling** - add more machines. instead of one powerful server, run 10 smaller ones behind a load balancer

**Vertical is the right move first because:**
- Zero architecture change. Upgrade the instance size, done in minutes
- No distributed systems complexity. One database, one source of truth
- Cheaper

**Horizontal becomes necessary when:**
- Single point of failure becomes an issue
- Maxed our vertical or you need fault tolerance (no downtime) or your work is stateless and parallelizes naturally 

**The key nuance:** most real systems do **both**. You scale your web servers horizontally (easy, stateless) and your database vertically as long as possible (hard to distribute state). Databases go horizontal last because distributing data introduces the hardest problems in computing.

___

## CAP THEOREM
- CAP stands for 3 properties a distributed system can have:
   1.  **Consistency**: every read gets the most recent write 
    - If you update your profile name, the very next read - from *any* server - sees the new name
   2. **Availability**: every request gets a response (not an error), even if some nodes are down
   3. **Partition tolerance**: the system keeps working even when network communication between nodes is lost (a "partition" = one server can't talk to another)

- The theorem says: **when a network partition happens, you can only guarantee 2 of the 3. You must pick C or A**
  - This is not "pick any two of the three"... Partitions *will* happen in any distributed system, so partition tolerance isn't optional, the real choice is:
  - **When the network splits, do you:**
    - Refuse to server requests until nodes are back in sync? -> **CP** (consistent but unavailable)
    - Keep serving requests even though some nodes might have stale data? -> **AP** (available but inconsistent)

- **CP examples:** banking system, inventory/stock systems, anything involving money or limited quantities where acting on stale data is a real-world loss
- **AP examples:** social feeds, DNS, analytics dashboards, user profiles

- Rule of thumb: if stale data causes someone to lose money or violate a constraint, pick CP. If stale data is mildly annoying, pick AP

## Consistency Models
- CAP gave you the binary: consistency or availability. In practice, most systems don't pick one extreme - they pick a **point on the spectrum**
- Two ends I need to know:

1. **Strong consistency:** after a write completes, eery subsequent read - from any node, any user, anywhere - sees that write. Guaranteed. No exceptions
  - Ex: you transfer $500 from checkings to savings. The moment the transfer confirms, any device you check shows the updated balances (sys blocks all reads until the nodes agree) 
  - **The cost**: slower. the system has to coordinate between nodes bfore responding 

2. **Eventual consistency:** after a write, replicates *will* converge to the same value - but theres a window where different nodes might return different (stale) data. Nothing blocks, reads are fast, but old data might be present for a bit
   - Ex: Discord - a message gets written to one one, other nodes catch up ms later

- The trade-off:
  - Strong consistency = correctness guaranteed, pay with latency
  - Eventual consistency = speed guaranteed, tolerate brief staleness

**Real-world mapping:**
- Bank balance -> strong consistency
- Instagram like count -> eventual consistency
- Shopping cart inventory -> strong consistency
- DNS propagation -> eventual consistency

## Latency vs. Throughput
- **Latency:** How long one request takes from start to finish
- **Throughput:** How many requests your system handles per unit of time