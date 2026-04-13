# Postgres / SQL Interview Questions

Curated mid-to-senior SQL and Postgres-specific questions. Focus is on query writing, indexing, EXPLAIN ANALYZE reading, and schema decisions — not Postgres administration.

---

## Tier 1 — Query writing

### 1. Top N per group
Given a `posts` table with `user_id`, `created_at`, return the **3 most recent posts per user** in a single query.
- **Demonstrate:** Window functions (`ROW_NUMBER() OVER (PARTITION BY ...)`), or `LATERAL JOIN`.
- **Discuss:** Why a naive `GROUP BY` doesn't solve this. When `LATERAL` outperforms window functions and vice versa.

### 2. Find duplicates
Given a `users` table with `email`, find all emails that appear more than once and how many times.
- **Demonstrate:** `GROUP BY ... HAVING COUNT(*) > 1`.
- **Discuss:** Why a unique constraint should have prevented this. How you'd dedupe in production safely.

### 3. Running totals
Given an `orders` table with `created_at` and `amount`, return a query showing daily revenue and a running total.
- **Demonstrate:** `SUM(...) OVER (ORDER BY date)`, `DATE_TRUNC`.
- **Discuss:** When to compute this in SQL vs the app. Why pre-aggregating into a daily summary table can be smarter.

### 4. Self-join challenge
Given an `employees` table with `id`, `name`, `manager_id`, return each employee's name alongside their manager's name.
- **Demonstrate:** Self-join, `LEFT JOIN` to handle employees without managers.
- **Discuss:** Recursive CTEs for full org-chart traversal.

---

## Tier 2 — Indexing & performance

### 5. Add the right index
Given a slow query: `SELECT * FROM orders WHERE user_id = ? AND status = 'pending' ORDER BY created_at DESC LIMIT 10`. Propose an index.
- **Demonstrate:** Composite index design, column order matters, including `created_at` for the sort.
- **Discuss:** Why column order in a composite index matters. Why `SELECT *` is bad for index-only scans. When a covering index helps.

### 6. Read an EXPLAIN ANALYZE plan
Given an EXPLAIN output showing a sequential scan on a table with 10M rows. Identify the problem and propose a fix.
- **Demonstrate:** Reading rows, cost, actual time, scan types.
- **Discuss:** Seq scan vs index scan vs bitmap heap scan. When the planner correctly chooses seq scan (small tables, low selectivity).

### 7. Why isn't my index being used?
Given a query with `WHERE LOWER(email) = 'foo@bar.com'` and an index on `email`. Index isn't used. Fix it.
- **Demonstrate:** Functional index (`CREATE INDEX ... ON users (LOWER(email))`).
- **Discuss:** Why function calls on indexed columns kill index use. Other common killers (implicit type coercion, leading wildcards in LIKE).

---

## Tier 3 — Schema design

### 8. Design a schema for a multi-tag system
Tasks can have many tags, tags can be on many tasks. Design the schema.
- **Demonstrate:** Many-to-many junction table, indexes on both FK columns.
- **Discuss:** Why you need indexes on both sides of the junction. When to denormalize tags into a JSONB column instead and why.

### 9. Soft delete vs hard delete
Design a `users` table where deletes need to be reversible for 30 days. Compare approaches.
- **Demonstrate:** `deleted_at` column, partial index for active users.
- **Discuss:** Trade-offs: data integrity, query complexity, GDPR/right-to-delete implications.

### 10. JSONB vs separate table
You're storing user preferences (variable shape, ~20 fields, occasionally queried). JSONB column or separate table?
- **Demonstrate:** Both schemas, sample queries, GIN index for JSONB.
- **Discuss:** When JSONB wins (truly variable schema, infrequent reads). When a table wins (structured queries, joins, foreign keys).

---

## Tier 4 — Senior curveballs

### 11. Optimize a slow report query
Given a multi-join query producing a daily report that takes 30 seconds. Walk through how you'd diagnose and optimize.
- **Demonstrate:** EXPLAIN ANALYZE reading, index proposals, materialized view consideration.
- **Discuss:** When to materialize. Refresh strategies (on write, scheduled, on read).

### 12. Concurrency: write skew scenario
Two users transfer money between accounts simultaneously. Show how the wrong isolation level can cause incorrect balances. Fix it.
- **Demonstrate:** `SELECT ... FOR UPDATE`, isolation levels.
- **Discuss:** Read committed vs repeatable read vs serializable. Why most apps use read committed. When you need stronger.

---

## Notes on usage

- These are best done against a real Postgres instance (Docker is fine). Set up a small schema and a few thousand rows so EXPLAIN ANALYZE actually means something.
- For Block 3 use, pair with topics from Section 4 (Backend) Postgres deep-dive.
- Always read the EXPLAIN output yourself, then explain it back. Don't just copy what the tool says.
