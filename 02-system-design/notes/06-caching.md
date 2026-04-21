# Caching

## Why Caching Matters
- Reading from a database is slow compared to reading from memory. Every time your app can answer a request from memory instead of hitting a database, it's faster for the user and cheaper on your infra

### When does caching make sense?
- Data is **read more often than written** (high read-to-write ratio)
- The same data is **requested repeatedly** 
- Slight staleness is **acceptable** (you can tolerate the data being a few seconds old)

### When does caching NOT make sense?
- Data changes constantly and must be fresh
- Every request is unique
- Data is highly personalized with no overlap between users

## Cache-Aside Pattern
- The most common caching pattern encountered.
- It is a **read** strategy
- The flow:
    1. Request comes in - check the cache first
    2. **Cache hit:** data is there --> return it. Done
    3. **Cache miss:** data isn't there --> query the db --> write the result into cache --> return answer
   
Request → [Check Cache] 
              ├── HIT → Return cached data
              └── MISS → Query DB → Write to Cache → Return data

- **The Tradeoff:** what happens when someone *updates* the data in the database? The cache still has the old version. This is the **cache invalidation problem** (famously one of the two hardest problems in comp sci)
    - Common strategies for handling this:
        - **TTL**: cache entry expires after N seconds. Simple, but stale for up to N seconds
        - **Invalidate on write**: when you update the DB, delete the cache entry. Next read triggers fresh cache fill

## Write-Through vs. Write-Behind
- Cache-aside is a **read** strategy
- These two patterns address what happens on **writes**

### Write-Through

1. App writes to the cache
2. Cache **immediately** writes to the database (synchronously)
3. Response returns only after both writes success

- Pros: cache and DB are always in sync - no staleness
- Cons: every write is slower - you're doing two writes before responding

### Write-Behind (Write-Back)

1. App writes to the cache
2. Cache acknowledges immediately - user gets a fast response
3. Cache writes to the databse **later** (async, batched)

- Pros: writes are fast - user doesn't wait for DB
- Cons: if the cache crashes before syncing to DB, you **lose data**. Cache had the only copy

**The trade-off in one sentence:** write-through sacrifices write speed for consistency. Write-behind sacrifices durability for write speed

## Cache Eviction Policies 
- Cache has finite memory. When it's full and a new entry needs to go in, something has to get kicked out
- **3 policies to be aware of:**
    1. **LRU (Least Recently Used)** - Evict the entry that hasn't been accessed in the longest time
        - Most common default
        - Good for: general purpose caching where recent access predicts future access
    2. **LFU (Least Frequently Used)** - Evict the entry that's been accessed the *fewest total times*
        - The logic: popular items should stick around even if they haven't been hit recently
        - Good for: workloads with stable "hot" items
        - Downside: a once-popular item that's no longer relevant can cling to the cache forever. Needs decay mechanism
    3. **TTL (Time-To-Live)** - a per-entry expiration timer
        - Good for: ensuring staleness never exceeds a known bound
        - Usually combined with LRU or LFU, not used alone 


Core Concept: **Evicition policies (LRU/LFU) manage space. Invalidation strategies (TTL, invalidate-on-write) manage freshness**

## Redis
- An in-memory data store. It holds data in RAM, which is why it's fast. It sits alongside your db as a caching layer
### Key characteristics

- **In-memory** -- all data lives on RAM. Fast reads/writes but limited memory
- **Data structures** -- not just key-value. Redis supports strings, lists, sets, hashes, and more
- **Singled-threaded** -- one operation at a time, no race conditions
- **Optional persistence** -- can snapshot to disk or log every write for durability

### Common use cases

- **Cache layer** -- the cache-aside pattern
- **Session storage** -- user sessions in Redis instead of your app server's memory (this is what makes horizontal scaling work - any server can look up any users session)
- **Rate limiting** -- track request counts per user with TTL keys 
- **Leaderboards** 

## CDN Caching
- **CDN:** a network of servers distributed geographically that cache content close to users
- What they cache:
    - Static assets (images, CSS, JS bundles, fonts, videos)
    - API responses
    - Entire HTML pages (for static or semi-static sites)

### How it works

1. User in Tokyo requests yourapp.com/logo.png
2. Request hits the nearest CDN edge node (Tokyo)
3. **Cache hit:** edge node has it -> returns immediately and origin server never touched
4. **Cache miss:** edge node forwards to origin -> origin responds -> edge node caches it + returns to user. Next Tokyo user gets a cache hit

- **Cache control:** your origin server tells the CDN what to cache and for how long via HTTP headers:
    - *Cache-Control: max-age=86400* -- cache this for 24 hrs
    - *Cache-Control: no-cache* -- always revalidate with origin before serving
    - *Cache-Control: no-store* -- never cache (sensitive data)

- **Cache invalidation on CDNs:**
  - 2 common solutions:
      - **Cache busting** -- append a hash to the filename (app.a3f3s.js). New deploy = new filename = cache miss = fresh file
      - **Purge API** -- tell the CDN to drop specific entries. Most CDN providers offer this

**The metric that matters: hit rate** - a well-configured CDN should have 90%+ cache hit rate for static assets

## Cache Stampede 
- The scenario:
    1.  You have a popular cache entry (say, homepage data) that thousands of users hit per second
    2.  The TTL expires - the entry disappears from cache
    3.  Suddenly thousands of requests simultaneously miss the cache and all hit the database
    4.  Your db gets crushed by a spike it wasn't sized for

- The above ex is a **cache stampede** 

### 3 Common Mitigations

1. **Staggered TTLs** -- add a random jitter to expiration times. Instead of every entry expiring at exactly 300 seconds, use 270 - 330 seconds. Prevents mass simultaneous expiry
2. **Lock-based recomputation** -- when a cache miss happens, the first request acquires a lock and rebuilds the cache. All other concurrent requests either wait for the lock to release or get served slightly stale version
3. **Background refresh** -- before the TTL expires, a background job proactively refreshes the cache entry. The entry never actually goes empty, it gets replaced while still valid

