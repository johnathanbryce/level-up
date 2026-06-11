# Build Reps — Hands-On Coding Practice Track

## Purpose

Short, real, runnable **build reps** that rebuild production coding fluency — the muscle LLM-offload
atrophied. Comprehension is intact; *writing it cold* is the gap. This track is the antidote, and
John found it **more valuable for interview readiness than algo drills alone** (his call,
2026-06-11, after the Deep Core A1 full-stack CRUD rep).

**This is NOT a fixed curriculum.** It's a **fluid, pull-based** practice track. John invokes it on
any day he's up for it — trigger phrase: **"let's do a rep"** (or "build-rep"). Target cadence
~once a week, but it's opt-in, never scheduled. On a rep day, we pick from the Backlog menu below
*or* invent something fresh based on his mood, energy, and time.

**Priority:** reps that transfer to **live / paired-programming interviews** come first — full-stack
CRUD is the bread and butter. But a rep can be anything: frontend-only, backend-only, DB-only,
CI/CD, agentic, or a combo. Variety is fine; interview-relevance is the tiebreaker.

This is a **peer to `interviews/` and `sandbox/`** — `sandbox/` stays a pure throwaway playground
(quick react/next/fastapi boot-ups); structured reps with tracking live here.

---

## How a rep session runs (codifies what worked in Deep Core A1)

1. **Pick.** John names energy / time / category mood. Claude proposes a rep from the Backlog *or*
   invents fresh → confirms **scope + scaffold dial** in 2–3 lines before any code.
2. **Clarify + plan in beats.** 2–3 clarifying questions, then a **2–3 beat plan stated out loud**
   before coding (the anti-ramble / pairing-format habit — John's #1 interview risk is rambling).
3. **Build in vertical slices.** Smallest runnable thing first, confirm, then layer.
4. **Division of labor.** Claude scaffolds the dialed-in boilerplate (env, **frontend markup/CSS**,
   stubs, dummy data, config). **John writes the business logic** — API routes, CORS, SQL, React
   hooks/forms/state. Frontend markup is *always* Claude's job; John focuses on logic, not HTML/CSS.
5. **Review honestly, as he goes.** Point out bugs, anti-patterns, missed edge cases with the *why*.
   Watch John's recurring bug-types (inverted conditions, builtin-shadowing, boundary operators,
   expression-vs-assignment, return-inside-loop) — see `01-algorithms/CLAUDE.md`.
6. **Clean files at "done."** Enforce save hygiene — no debug prints, dead code, or stale comments
   before a rep is called complete.
7. **Log it.** Add a Completed-log row. Surface meaningful gaps back to the relevant section CLAUDE.md.

### Scaffold dial

Each rep sets an explicit knob so hands-off increases over time (like the Deep Core A1→A4 ladder):

- **Heavy** — Claude scaffolds env + markup + most boilerplate + stubs; John writes core logic only.
- **Medium** — Claude scaffolds env + frontend markup; John writes all backend + all React logic.
- **Light** — Claude scaffolds env only (or nothing); John builds end-to-end, reviewed at the end.

A1 ran ~Medium. The dial should drift toward Light as fluency returns.

---

## Backlog (the fluid menu — add / remove / reorder freely)

Not a sequence. A buffet to pull from on a rep day. Priority = interview/paired-programming transfer.

| Category | Candidate reps | Priority |
|---|---|---|
| **Full-stack CRUD** | ✅ Rep 000 (samples-app, SQLite) · 🔜 Rep 001 (Postgres + Docker Compose, frontend-heavy) · CRUD + JWT auth + protected routes · CRUD w/ optimistic updates + error rollback | **HIGH** |
| **Frontend / React** | React Query dashboard (caching / retries — ties to A1's RQ discussion) · multi-step form wizard w/ validation · virtualized + debounced multi-filter list | **HIGH** |
| **Backend / FastAPI** | Data-aggregation service (group-by / stats — Deep Core A3 shape) · pagination+filter+sort query params done right · file-upload + processing endpoint | MED-HIGH |
| **Database / SQL** | Schema design + indexing + `EXPLAIN ANALYZE` on a slow query · multi-table JOINs · migrations | MED |
| **DevOps / CI-CD** | Dockerize a full stack (multi-service compose) · GitHub Actions pipeline (lint + test + build) · deploy-strategy demo (blue-green / rolling) | MED |
| **Agentic / AI** | Structured-output endpoint + deterministic tool + validate-retry loop (Deep Core A4 shape) · tiny RAG endpoint | HIGH (agentic roles) |
| **Combo / Read-the-code** | Extend-and-fix a planted-bug mini-app (Deep Core A2 format — reading unfamiliar code, debugging out loud) · WebSocket real-time feature | MED |

---

## In Progress

- **Rep 001 — Postgres full-stack CRUD** (queued for Fri 2026-06-12). Spec below.

### Rep 001 spec (next session)

Full-stack CRUD, same shape as A1 but: **real Postgres via Docker Compose**, **frontend-heavy**,
scaffold dial **Medium-Heavy**. Folder: `reps/001-<name>/` (name confirmed at session start).

- **Proposed domain (swappable):** drillhole records — `id`, `hole_id` (name), `status`
  (`planned` | `logging` | `complete`), `rock_type`, `grade` (≥0), `depth_m` (>0), `logged_at`.
  The status enum gives a meaningful `<select>` in the form and a filter dropdown.
- **Claude scaffolds:** Next.js app + most frontend markup (list table, create form, edit form,
  filter/sort/pagination controls — bare structure, minimal CSS); `db.py` (psycopg connection +
  a simple **connection pool** so John *sees* the Postgres-vs-SQLite difference); Pydantic model
  stubs; `requirements.txt`; dummy seed.
- **John writes:** the `docker-compose.yml` (guided — short, doubles as a DevOps rep); **all API
  routes** — GET list (pagination + filter + sort), GET by id, POST, **PUT/edit**, DELETE — using
  **raw `psycopg`** (cements the DB-API pattern from A1: same `connect → cursor → execute → fetch →
  commit → close`, just `%s` placeholders + a DSN); **CORS**; and **all React logic** — controlled
  create/edit forms, POST/PUT mutations with refetch-or-optimistic update, and list-at-scale
  (server-side pagination + sort + filter wired to query params).
- **Why:** raw psycopg over an ORM (cement the transfer; ORM is a later rep) · Docker Compose
  (local, realistic, a real DevOps skill) · forms+mutations + list-at-scale are the two big frontend
  reps A1 didn't cover · pool is scaffolded so frontend time isn't burned on it.

---

## Completed log

| # | Date | Rep | Category | Stack | Scaffold | What John wrote | Outcome / notes |
|---|------|-----|----------|-------|----------|-----------------|-----------------|
| 000 | 2026-06-10/11 | **Samples Explorer** — full-stack CRUD | Full-stack CRUD | FastAPI + Pydantic + SQLite + Next.js/TS | Medium | All backend routes (GET list+filter, GET by id/404, POST 201 two-model, DELETE 204), Pydantic validation, CORS; frontend fetch + loading/error/empty states, debounced filter, extracted `useDebounce` hook, AbortController race handling; SQLite swap (raw `sqlite3` DB-API, `lastrowid`/`rowcount`) | **Complete.** Deep Core R3 prep (A1). Code: [../sandbox/interview-prep/deep-core/samples-app/](../sandbox/interview-prep/deep-core/samples-app/). Concepts landed: CORS/SOP (browser-enforced, relaxes not protects), useEffect fetch lifecycle + cleanup, AbortController vs ignore-flag, debounce = setTimeout + clearTimeout, DB-API connection/cursor/commit, **DB-API cross-tool transfer (sqlite3 → psycopg)**, FastAPI lifespan, `Depends(get_db)` pattern, connection pooling rationale. |
