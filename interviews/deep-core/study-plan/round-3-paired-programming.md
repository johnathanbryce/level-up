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

- **A1 — IN PROGRESS (started 2026-06-10).** `samples-app/` scaffolded. Backend: venv + FastAPI,
  working route skeleton (learned: APIRouter + `include_router` *ordering* — include must come
  AFTER routes; interpreter-selection for Pylance; uvicorn CLI vs `__main__`; routes fire
  per-request not at startup; `return` not `print`). Slice 1 (`GET /samples` returning seeded
  dicts) done. Seed data in `app/seed_data.py`. **Next: slice 2 = Pydantic models (`SampleCreate`
  vs `Sample`), then GET-by-id (404), POST (201), DELETE (204), `?rock_type=` filter, CORS.**
- A2 — not started.
- A3 — not started.
- A4 — not started (stretch).

## Day plan

- **Day 1 (2026-06-10):** algo warm-up (done: group_tags.py, merge_bookings.ts) → A1 backend.
- **Day 2 (2026-06-11):** algo warm-up → A1 frontend (Next.js consumer + useDebounce) + A1 SQLite
  → if time, start A2.
