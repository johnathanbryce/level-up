# Round 3 — Paired Programming Prep

**Round 3 = collaborative paired programming.** John has never done one (only solo
live-coding). Goal over 2026-06-10 → 06-11: not-shaky on hands-on coding + comfortable
with the *pairing* format. Coding sandbox: `sandbox/interview-prep/deep-core/`.

This doubles as general muscle-memory rebuild — John has offloaded most coding to LLMs;
comprehension is intact, *production* fluency is the gap. Reps with a decreasing safety net.

---

## The format — what's actually scored

A pair round assumes you can code (R2 already proved it). It scores **how you build with
someone**. The rubric to drill:

1. **Clarifying questions first** — 2–3 before typing, always. Surfaces ambiguity, buys thinking time.
2. **Think out loud continuously** — silence is the fastest way to lose; they can't score what they can't hear.
3. **State a 2–3 beat plan before coding** — then go quiet and execute. (John's anti-ramble lever.)
4. **Communicate trade-offs concisely** — name the cost, take a position, move on.
5. **Collaborate, don't perform** — take nudges like a coworker; push back with reasons; "I don't know, here's how I'd find out" is a senior move.

Build in **vertical slices** — smallest runnable thing first, confirm, then layer. Expect
the interviewer to **add scope mid-stream** ("now add filtering") to test adaptability.

John's #1 risk (carried from R2): **rambling under pressure.** The plan-in-beats habit is the antidote.

---

## Assignment ladder (hands-off dial increases each rep)

| # | Assignment | Format drilled | Claude's mode |
|---|-----------|----------------|---------------|
| **A1** | **Samples Explorer** — full-stack CRUD: FastAPI + Pydantic + SQLite + Next.js consumer | Build an API end-to-end, wire a frontend | **Step-by-step guided** — scaffold + nudge freely |
| **A2** | **Extend & Fix** — small working-but-buggy FastAPI+React mini-app; read it cold, fix planted bugs out loud, then add a requested feature mid-stream | Reading unfamiliar code, debugging narration, adapting to scope change (the most common real pair format) | **He drives, I nudge only when stuck** |
| **A3** | **Data service** — FastAPI endpoint that ingests raw records and computes aggregations/stats (group by rock_type, avg grade, depth bucketing) | Idiomatic Python under pressure (comprehensions, `collections`, `statistics`) + data transformation | **Spec only** — he scaffolds env + writes all; I review at the end |
| **A4** | *(stretch)* **Agentic endpoint** — a route doing structured-output validation + orchestrating one deterministic "tool" (mock geostat calc) with a validate-retry loop | Mirrors Deep Core's wedge; ties to his agentic strength | **Cold, timed interview-sim** — minimal intervention |

**Woven in (not standalone):** React interview patterns — `useDebounce` debounced search,
controlled inputs, loading/error/empty states, memoization-when-it-matters — land inside
A1's frontend and A2.

**Why this mix:** A1 builds the core full-stack reflex; A2 drills the format most pair rounds
actually use (extend/debug existing code, not greenfield); A3 hammers the Python-writing weak
spot John is rebuilding; A4 connects to the role's agentic core. Not all are greenfield APIs —
that's deliberate.

---

## Progress

- **A1 — BACKEND COMPLETE (2026-06-10), committed.** `samples-app/backend/` — full CRUD FastAPI
  service, all endpoints smoke-tested green: `GET /samples` (+ `?rock_type=` filter), `GET /samples/{id}`
  (404), `POST /samples` (201, two-model design `SampleCreate` vs `Sample`), `DELETE /samples/{id}`
  (204, no body). Pydantic validation via `Literal` rock_type → 422 on bad input. Seed data in
  `app/seed_data.py`. **Concepts landed:** APIRouter `include_router` *ordering* (after routes);
  Pylance interpreter selection (the "import not resolved"/no-fastapi-colors issue = editor interpreter
  ≠ runtime venv); uvicorn CLI vs `__main__`; routes fire per-request; `return` not `print`; generators
  are lazy (print shows the object, `list()` consumes); `response_model` is a validate+serialize contract;
  **return the resource not a `{status,message}` envelope** (errors → status codes + `HTTPException`,
  never in the 200 body) — but rich domain payloads (warnings/tool-calls in agentic routes) DO belong in a
  typed response model; in-memory store = process RAM, resets on `--reload`/restart, invisible across
  workers → *why databases exist*; `**model_dump()` is Python's dict-spread; `async`/try-except only at the
  real I/O boundary. **Remaining for A1:** CORS (deferred — only matters once frontend calls it), then
  **frontend (Next.js consumer + `useDebounce`)** and **SQLite persistence** on Day 2.
- A2 — not started.
- A3 — not started.
- A4 — not started (stretch).

## Day plan

- **Day 1 (2026-06-10):** algo warm-up (done: group_tags.py, merge_bookings.ts) → A1 backend.
- **Day 2 (2026-06-11):** algo warm-up → A1 frontend (Next.js consumer + useDebounce) + A1 SQLite
  → if time, start A2.
