## Scenario: You're designing the caching layer for an e-commerce product catalog. 

Here's what you know:
- 50,000 products
- 10:1 read-to-write ratio (products are browsed constantly, updated occasionally by sellers)
- The homepage shows "Top 20 trending products" — this gets hit on every single page load
- Individual product pages are viewed frequently but follow a long-tail distribution (some products get 1000x more views than others)

In your notes or here, answer these four questions:

1. What caching pattern do you use for individual product pages and why?
2. When a seller updates a product's price, how do you handle the cached version?
3. The "Top 20 trending" list is your hottest cache entry. What's the stampede risk and how do you mitigate it?
4. Where does a CDN fit (if at all) in this system?


**My Answer:**

1. For individual product pages, I would use Redis to cache products. I would not cache all 50K products, just the most viewed ones. Things like our logo, certain sections of HTML and JS bundle if necessary would be handled via a CDN. As for the items they contain, as many of the most-viewed and interacted with items I would cache, with a TTL (between 23.5 - 24.5 hours in seconds so we have it staggered so as to not overwhelm the database on a popular item when the cache expires) which is then invalidated via write-through if the seller makes a change to any of the individual product information. 
2. As mentioned in the prior answer, we use write-through. We must ensure consistency between the database and the cache when the seller owner updates their product. 
3. Stampede risk would be one or all of these items expiring at the same time and then all the mass user requests immediately hitting and crashing our database. Mentioned in answer 1 that I would have a TTL of X seconds (could be 24 hours to start or even longer if product info doesn't change often beyond updating the current count of items left in stock) that has a jitter of 23.5 hrs - 24.5 hrs in seconds.
4. A CDN would be useful for serving up the product images and any other static site data. Maybe the seller has their own company logo that rarely ever changes or other specific media data that rarely changes. If the seller changed the product details, we can implement Cache-Control: max-age=X where X could be a business decision but start with 24 hours. If the seller updates the image, we could implement a background refresh which checks all cached CDN images for all products ever X seconds and if there is a change, delete or edit the CDN image with the updated image (the image change doesn't need to be immediately reflected and uncached for all users)

---

**Corrected Answers:**

1. **Cache-aside with Redis.** Request comes in → check Redis for product data → cache hit: return it → cache miss: query DB → write result to Redis → return. TTL of ~24 hours with jitter is fine for the long-tail products. The key insight: cache-aside naturally handles the long-tail distribution because only products that are actually requested enter the cache. No need to proactively cache all 50,000 — the hot products cache themselves through usage. CDN is a separate concern (see #4) — it handles static assets, not product data.

2. **Invalidate-on-write, not write-through.** Seller updates the price in the DB → app deletes that product's Redis key → next read triggers a cache-aside miss → fresh data gets pulled from DB and re-cached. Write-through is a different pattern where the app writes to the cache first and the cache synchronously writes to the DB. What we want here is: DB is the source of truth, cache gets invalidated when the source of truth changes. TTL acts as a safety net in case invalidation fails.

3. **Lock-based recomputation, not staggered TTLs.** The Top 20 list is a single hot key — there's nothing to stagger (staggered TTLs help when many *different* keys expire simultaneously). When this one key expires, thousands of concurrent requests all miss the cache at once. Fix: the first request to miss acquires a lock and rebuilds the cache entry. All other concurrent requests either wait for the lock to release or get served a slightly stale version. Only one request hits the DB.

4. **CDN for product images + cache busting for updates.** Product images on CDN is correct — high-read, rarely-changing static assets are the ideal CDN use case. When a seller uploads a new image, use cache busting: the new image gets a new URL (e.g., `product-123-v2.jpg` or a content hash in the filename). New URL = automatic cache miss on the CDN = fresh image served. No background polling job needed — simpler, more reliable, no race conditions.