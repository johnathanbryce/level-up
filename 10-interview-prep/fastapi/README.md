# FastAPI Interview Questions

Curated mid-to-senior FastAPI / Python backend questions, sourced from real 2025-2026 interview content. Focus is on async correctness, validation, auth, ORM patterns, and middleware — the things that actually come up in live coding rounds and take-homes.

Each question has: a short prompt, what to demonstrate, and the discussion points an interviewer would expect.

---

## Tier 1 — Endpoint design & validation (most common live-coding)

### 1. Build a paginated list endpoint
`GET /items?page=1&size=20` returns paginated items from a fake in-memory store. Include total count, page, size, and items in the response.
- **Demonstrate:** Pydantic response model, query parameter validation (positive integers, max page size), proper status codes.
- **Discuss:** Offset-based vs cursor-based pagination. Why cursor-based is better for large datasets and infinite-scroll UIs. Link header vs body metadata for pagination info.

### 2. Build a CRUD endpoint set with proper status codes
`POST /users`, `GET /users/{id}`, `PUT /users/{id}`, `DELETE /users/{id}`. Validate inputs with Pydantic. Return correct status codes for each scenario (201, 200, 204, 404, 422, 409).
- **Demonstrate:** Pydantic models for create/update/response (separation matters), `HTTPException` patterns, idempotency.
- **Discuss:** Why PUT vs PATCH. Why DELETE returns 204. When 409 (conflict) is correct over 400. What "idempotent" means and which methods should be.

### 3. Request validation with custom Pydantic validators
Build a `User` model with: email (validated), password (min length, must contain digit), age (must be 18+). Reject invalid input with structured error messages.
- **Demonstrate:** Pydantic v2 validators (`@field_validator`, `@model_validator`), custom error messages.
- **Discuss:** Why validation belongs in the model, not the route handler. How FastAPI's automatic 422 responses work.

---

## Tier 2 — Async, dependencies, middleware

### 4. Async endpoint that calls two services concurrently
Build an endpoint that fetches user data and user posts from two separate (mocked) services *in parallel*, then returns a combined response.
- **Demonstrate:** `asyncio.gather`, proper async/await, timeout handling.
- **Discuss:** Why sequential `await` calls are slow. When `gather` is wrong (when calls depend on each other). Difference between async I/O and CPU-bound parallelism.

### 5. Implement a dependency-injected database session
Build a `get_db()` dependency that yields a session and closes it on cleanup. Use it in an endpoint.
- **Demonstrate:** `Depends`, generator-based dependencies, proper resource cleanup.
- **Discuss:** Why FastAPI's DI is better than passing globals. How dependencies compose. Why scope matters (request-scoped vs app-scoped).

### 6. Write custom middleware that logs request duration
Middleware that measures time to handle each request and logs `method path status duration_ms`.
- **Demonstrate:** ASGI middleware, request timing, structured logging.
- **Discuss:** Difference between FastAPI middleware and Starlette middleware. When to use middleware vs dependencies vs background tasks.

---

## Tier 3 — Auth & security

### 7. Implement JWT auth middleware
`POST /login` returns a JWT. `GET /me` requires the JWT in the `Authorization: Bearer <token>` header and returns the current user.
- **Demonstrate:** JWT signing/verification, password hashing (bcrypt), `HTTPBearer` dependency, 401 vs 403 distinction.
- **Discuss:** Why bcrypt over SHA. Token expiration. Refresh token rotation. Why JWTs are hard to revoke and what that means in practice.

### 8. Build a rate limiter middleware
Limit each IP to 60 requests per minute. Return 429 when exceeded with a `Retry-After` header.
- **Demonstrate:** Token bucket or sliding window implementation, in-memory store (with note that production needs Redis).
- **Discuss:** Why rate limiting in middleware vs at the load balancer. Token bucket vs leaky bucket vs sliding window trade-offs.

### 9. Role-based access control with dependencies
Add a `require_role("admin")` dependency that 403s if the current user lacks the role. Use it on a protected endpoint.
- **Demonstrate:** Composing dependencies (auth → role check), proper error responses.
- **Discuss:** RBAC vs ABAC. Why centralized authorization is safer than scattered if-checks.

---

## Tier 4 — ORM & database patterns

### 10. Solve an N+1 query problem
Given an endpoint that returns users with their posts. The naive implementation does 1 query for users + N queries for posts. Fix it.
- **Demonstrate:** SQLAlchemy `selectinload` / `joinedload` (or equivalent in asyncpg), query inspection.
- **Discuss:** Why N+1 happens, how to spot it (query logs, EXPLAIN), when joins vs separate queries are better.

### 11. Implement transactional write across two tables
Endpoint that creates a user and a default settings row in one atomic operation. If either fails, both roll back.
- **Demonstrate:** Async session, transaction context, error handling.
- **Discuss:** Isolation levels (high level), what "atomic" means. Why partial writes are dangerous.

### 12. Add a Redis cache layer to a slow endpoint
Endpoint that does an expensive computation. Add cache-aside: check Redis, miss → compute → store with TTL → return.
- **Demonstrate:** Async Redis client, key naming, TTL choice, cache invalidation on writes.
- **Discuss:** Cache stampede / thundering herd. When NOT to cache (highly dynamic data, low read rate). How to invalidate intelligently.

---

## Tier 5 — Senior-flavor curveballs

### 13. Background task vs queue
You need to send a welcome email after user signup. Implement it two ways: with FastAPI `BackgroundTasks` and conceptually with a queue (Celery / Redis Streams).
- **Demonstrate:** `BackgroundTasks` usage, plus a verbal walkthrough of the queue version.
- **Discuss:** When `BackgroundTasks` is fine (best-effort, fast, can lose). When you need a real queue (retries, durability, scale).

### 14. Streaming response endpoint
`GET /stream` returns a `StreamingResponse` that yields data over time (e.g., chunks of an LLM response or a large CSV).
- **Demonstrate:** Generators/async generators, `StreamingResponse`, proper content type.
- **Discuss:** Why streaming matters for UX (perceived latency). Difference between SSE and WebSockets. When to use each.

### 15. Design a small API end-to-end (take-home style)
Spec: build a notes API with users, notes (title, body, tags), and sharing (a user can share a note with another user). Include auth, validation, tests for at least one endpoint, and a README explaining design decisions.
- **Demonstrate:** Full project structure, schema design, layered architecture (routes / services / models), testing.
- **Discuss:** Defend three design decisions out loud as if reviewing with a senior engineer.

---

## Notes on usage

- For Block 3 use, pick a question that aligns with a sub-topic just covered in Section 4. For on-demand use, pick whatever John asks for.
- Time-box: 30-90 min for individual questions. #15 is a take-home and can sprawl; treat it as a multi-session capstone if attempted.
- Always discuss trade-offs. Code without reasoning is half an answer.
