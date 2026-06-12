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
| **Full-stack CRUD** | ✅ Rep 000 (samples-app, SQLite) · ✅ Rep 001 (drillhole-crud, Postgres + Docker Compose, backend-heavy) · CRUD + JWT auth + protected routes · CRUD w/ optimistic updates + error rollback | **HIGH** |
| **Frontend / React** | **Frontend-heavy full-stack (rich UI over a ready-made API — the counterpart to Rep 001; forms+mutations + list-at-scale on the client)** · React Query dashboard (caching / retries — ties to A1's RQ discussion) · multi-step form wizard w/ validation · virtualized + debounced multi-filter list | **HIGH** |
| **Backend / FastAPI** | Data-aggregation service (group-by / stats — Deep Core A3 shape) · pagination+filter+sort query params done right · file-upload + processing endpoint | MED-HIGH |
| **Database / SQL** | Schema design + indexing + `EXPLAIN ANALYZE` on a slow query · multi-table JOINs · migrations | MED |
| **DevOps / CI-CD** | Dockerize a full stack (multi-service compose) · GitHub Actions pipeline (lint + test + build) · deploy-strategy demo (blue-green / rolling) | MED |
| **Agentic / AI** | Structured-output endpoint + deterministic tool + validate-retry loop (Deep Core A4 shape) · tiny RAG endpoint | HIGH (agentic roles) |
| **Combo / Read-the-code** | Extend-and-fix a planted-bug mini-app (Deep Core A2 format — reading unfamiliar code, debugging out loud) · WebSocket real-time feature | MED |

---

## In Progress

- *(none — Rep 001 complete 2026-06-12, see Completed log. Next candidate: the queued
  **frontend-heavy** rep in the Backlog — rich UI over a ready-made API, the counterpart to 001.)*

---

## Completed log

| # | Date | Rep | Category | Stack | Scaffold | What John wrote | Outcome / notes |
|---|------|-----|----------|-------|----------|-----------------|-----------------|
| 000 | 2026-06-10/11 | **Samples Explorer** — full-stack CRUD | Full-stack CRUD | FastAPI + Pydantic + SQLite + Next.js/TS | Medium | All backend routes (GET list+filter, GET by id/404, POST 201 two-model, DELETE 204), Pydantic validation, CORS; frontend fetch + loading/error/empty states, debounced filter, extracted `useDebounce` hook, AbortController race handling; SQLite swap (raw `sqlite3` DB-API, `lastrowid`/`rowcount`) | **Complete.** Deep Core R3 prep (A1). Code: [../interviews/deep-core/samples-app/](../interviews/deep-core/samples-app/). Concepts landed: CORS/SOP (browser-enforced, relaxes not protects), useEffect fetch lifecycle + cleanup, AbortController vs ignore-flag, debounce = setTimeout + clearTimeout, DB-API connection/cursor/commit, **DB-API cross-tool transfer (sqlite3 → psycopg)**, FastAPI lifespan, `Depends(get_db)` pattern, connection pooling rationale. |
| 001 | 2026-06-12 | **Drillhole CRUD** — full-stack CRUD, backend-heavy | Full-stack CRUD + DevOps | FastAPI + raw psycopg + Postgres (Docker Compose) + Next.js/TS | Heavy FE / Medium-Light BE | `docker-compose.yml` (guided); `db.py` DSN + `get_db` pool dependency (the two load-bearing bits); **all 5 routes raw psycopg** — GET list (filter `WHERE` + whitelisted `ORDER BY` + `LIMIT`/`OFFSET` pagination), GET-by-id (404), POST (`RETURNING *`, 201), PUT (UPDATE … SET … RETURNING, 404), DELETE (`rowcount`, 204); CORS | **Complete.** Code: [001-drillhole-crud/](001-drillhole-crud/). Full loop verified (list/filter/create/delete green in browser). **Concepts landed:** Dockerfile-vs-compose (don't Dockerfile an off-the-shelf image), named volume + `/var/lib/postgresql` mount, **PG18 mount-path convention change** (hit + fixed live), `/docker-entrypoint-initdb.d/` auto-seed on fresh-volume-only, host→container networking (`localhost:5432` via published port), venv/pip workflow (`install -r` ← file→env vs `freeze` env→file), connection (line) vs cursor (query session), `%s` placeholder vs `LIKE %` wildcard, `dict_row` factory, `RETURNING *`, SQL-injection whitelist for *identifiers* (sort/order) vs `%s` for *values*, conditional query building (only `WHERE` is conditional; sort/pagination always apply). **Recurring gaps surfaced** → [../01-algorithms/CLAUDE.md] watchlist: (1) **FastAPI `:` vs `=`** — annotation (parse/inject) vs default — bit him **3×** in one session (query model, response_model param, POST body → "no body in Swagger"); (2) **`id` (int PK) vs `hole_id` (text name)** confusion — 2× (wrong column + wrong test value); (3) **indentation/scoping** of conditional SQL (ORDER BY/LIMIT nested under `if status`); (4) leftover dup `execute` + stub returns. **Wins:** DELETE `rowcount` transferred cleanly from Rep 000; reached for the injection whitelist correctly; debugged confidently off psycopg's error messages (read the `^` + hint). Heavy env-setup detour (VSCode interpreter / nested-venv auto-detect / PG18) ate ~40% of session — all real-world, but note for pacing. Also cleaned John's VSCode user settings: added `python.terminal.activateEnvironment`, removed the `/usr/bin/python3` `defaultInterpreterPath` hardcode that was forcing system Python. |
