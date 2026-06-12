# Rep 001 — Drillhole CRUD (Postgres + Docker Compose)

Full-stack CRUD, backend-heavy. Real Postgres in a Docker container, FastAPI on
your host talking to it over `localhost`, near-complete Next.js consumer.

**Your focus:** the `docker-compose.yml`, the two `db.py` TODOs, and **all** the
API routes + CORS using **raw psycopg**. The frontend is done — you just point it
at your API.

---

## Architecture

```
┌─────────────────┐      localhost:8000       ┌──────────────────┐
│  Next.js (host) │ ────────fetch───────────▶ │  FastAPI (host)  │
│   port 3000     │                           │   uvicorn        │
└─────────────────┘                           └────────┬─────────┘
                                                        │ localhost:5432
                                                        │ (raw psycopg)
                                               ┌────────▼─────────┐
                                               │ Postgres (Docker)│
                                               │  via compose     │
                                               └──────────────────┘
```

Only Postgres is containerized. FastAPI runs on your host, so it connects to the
**published** container port at `localhost:5432`.

---

## What you build

### 1. `docker-compose.yml` (you write — guided)

One service, `db`, using the official `postgres` image. It needs:

- the `postgres` image (pin a version, e.g. `postgres:16`)
- env vars: `POSTGRES_USER`, `POSTGRES_PASSWORD`, `POSTGRES_DB`
- a port mapping that publishes container `5432` to host `5432`
- a **named volume** mapped to `/var/lib/postgresql/data` (so data survives restarts)
- the `init.sql` in this folder mounted into `/docker-entrypoint-initdb.d/` (runs
  once on first init → creates the table + seeds rows)

Bring it up: `docker compose up -d`. Check it: `docker compose ps` and
`docker compose logs db`.

> Note: `init.sql` only runs on a **fresh** data volume. If you change it later,
> `docker compose down -v` (drops the volume) then `up` again.

### 2. `backend/db.py` (two TODOs)

- **DSN** — the conninfo string matching your compose env vars.
- **get_db** — the generator dependency that yields a pooled connection.

The pool object + lifespan wiring are already done for you.

### 3. `backend/main.py` (all routes + CORS)

Raw psycopg only. `db.cursor()` → `cur.execute(sql, params)` → fetch → `commit()`
for writes. Always parameterize with `%s` (never f-strings).

| Method | Path               | Behavior                                              | Success |
|--------|--------------------|-------------------------------------------------------|---------|
| GET    | `/drillholes`      | list; query params below                              | 200     |
| GET    | `/drillholes/{id}` | one record; 404 if missing                            | 200     |
| POST   | `/drillholes`      | create from `DrillholeCreate`; return the new record  | 201     |
| PUT    | `/drillholes/{id}` | update from `DrillholeCreate`; 404 if missing         | 200     |
| DELETE | `/drillholes/{id}` | delete; 404 if missing                                | 204     |

**GET `/drillholes` query params (this is the list-at-scale muscle):**

| Param    | Meaning                          | Default       | Maps to       |
|----------|----------------------------------|---------------|---------------|
| `status` | filter by status                 | none (all)    | `WHERE`       |
| `sort`   | column to sort by                | `logged_at`   | `ORDER BY`    |
| `order`  | `asc` or `desc`                  | `desc`        | `ORDER BY`    |
| `limit`  | page size                        | `20`          | `LIMIT`       |
| `offset` | rows to skip                     | `0`           | `OFFSET`      |

> ⚠️ `LIMIT`/`OFFSET`/`status` are **values** → bind with `%s`. But `sort`/`order`
> are **column/keyword identifiers** — you can't bind those with `%s`. Whitelist
> them against a set of allowed values instead (think about why: SQL injection).

The CORS middleware: the consumer runs at `http://localhost:3000`. Recall the
setup from Rep 000 cold.

---

## Acceptance criteria

- `docker compose up -d` → Postgres healthy, table seeded with 10 rows.
- All 5 routes work via the FastAPI docs (`/docs`) or `curl`.
- 404s on missing ids for GET/PUT/DELETE. POST returns 201. DELETE returns 204.
- GET list respects `status`, `sort`, `order`, `limit`, `offset`.
- Frontend (`http://localhost:3000`) lists, filters, creates, and deletes with no
  changes to the frontend code.
- Files clean at the end — no debug prints, no dead code.

---

## Run order

```bash
# 1. Infra
docker compose up -d

# 2. Backend (in backend/)
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload          # serves on http://localhost:8000

# 3. Frontend (in frontend/)
npm install
npm run dev                         # serves on http://localhost:3000
```
