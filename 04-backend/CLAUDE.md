# Backend Deep-Dive — Progression Tracker

## Overview

Hands-on backend development in two tracks: Python/FastAPI (~60%) and Node/Express (~40%). Covers API design, database work (Postgres + Redis), authentication, and real project building. This is where concepts from System Design become tangible code.

## Definition of Done

Can build a clean, well-structured REST API in both Python/FastAPI and Node/Express. Can write efficient SQL queries, explain indexing decisions, implement Redis caching with measurable performance improvement, and design proper auth flows.

---

## Sub-Topics

### API Design Fundamentals

- [ ] REST resource naming conventions
- [ ] HTTP methods and when to use each (GET, POST, PUT, PATCH, DELETE)
- [ ] Status codes: know the important ones (200, 201, 204, 400, 401, 403, 404, 409, 422, 500)
- [ ] Error response patterns (consistent error format)
- [ ] Pagination patterns (cursor-based vs offset)
- [ ] API versioning strategies
- [ ] Request validation and data sanitization
- [ ] GraphQL — what it is, how it differs from REST (client specifies what data it wants), when you'd choose it vs REST (not a deep dive, conversational awareness only)

### Python/FastAPI Track (~60%)

- [ ] FastAPI project structure and best practices
- [ ] Pydantic models for request/response validation
- [ ] Dependency injection in FastAPI
- [ ] Async endpoints — when async matters and when it doesn't
- [ ] Middleware (CORS, logging, error handling)
- [ ] Build a complete API project: multiple related resources, proper error handling, auth
- [ ] Connect to Postgres with SQLAlchemy or asyncpg
- [ ] Implement Redis caching layer
- [ ] Write tests (pytest)

### Node/Express Track (~40%)

- [ ] Express project structure and middleware patterns
- [ ] Route organization and controller patterns
- [ ] Error handling middleware
- [ ] Request validation (zod or joi)
- [ ] Build equivalent API with same patterns as FastAPI project
- [ ] Connect to Postgres (pg or Prisma)
- [ ] Implement Redis caching layer
- [ ] Write tests (jest or vitest)

### Postgres Deep-Dive

- [ ] Schema design: normalization, relationships, constraints
- [ ] Core SQL: JOINs (INNER, LEFT, RIGHT, FULL), GROUP BY, HAVING
- [ ] Subqueries and CTEs (Common Table Expressions)
- [ ] Indexing: B-tree, when to index, when not to, composite indexes
- [ ] EXPLAIN ANALYZE: reading query plans, identifying slow queries
- [ ] Connection pooling (pgBouncer concepts)
- [ ] Migrations: strategy and tooling (Alembic for Python, Prisma/knex for Node)
- [ ] Transactions and isolation levels (conceptual)

### Redis

- [ ] Redis data structures: strings, hashes, lists, sets, sorted sets
- [ ] Cache-aside implementation: check Redis → miss → query DB → store in Redis → return
- [ ] TTL strategies: when to expire, how long
- [ ] Session storage with Redis
- [ ] Rate limiting with Redis (token bucket implementation)
- [ ] Measure: query with cache vs without cache (prove it helps)

### Testing

- [ ] Unit tests vs integration tests vs end-to-end tests — what each tests, when to use which
- [ ] Test structure: arrange-act-assert (AAA) / given-when-then
- [ ] What to test and what NOT to test (test behavior, not implementation details)
- [ ] Mocking — what it is, when it's appropriate, when it's harmful (over-mocking hides real bugs)
- [ ] Test coverage — what it means, why 100% coverage is a trap, what "good enough" looks like
- [ ] Python: pytest basics (fixtures, parametrize, assert patterns)
- [ ] Node: jest or vitest basics (describe, it, expect, mocking)
- [ ] Write meaningful tests for both API projects (not just "it runs without crashing")

### Authentication & Authorization (Implementation)

- [ ] JWT implementation: signing, verification, refresh tokens
- [ ] Password hashing (bcrypt)
- [ ] Middleware for protecting routes
- [ ] Role-based access control (basic)

---

## Projects

### FastAPI Project: [Name TBD]

**Description:** TBD — a realistic API with 3-4 related resources, auth, caching, proper error handling.
**Status:** NOT STARTED
**Notes:**

### Express Project: [Name TBD]

**Description:** TBD — equivalent patterns to FastAPI project, different stack.
**Status:** NOT STARTED
**Notes:**

---

## Session Log

| Date | Topics Covered | Track (Py/Node) | Assessment | Next Focus |
|------|---------------|-----------------|------------|------------|
| — | — | — | — | — |

---

## Notes & Weak Spots

- (none yet)
