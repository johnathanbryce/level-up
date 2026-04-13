# Interview Prep — Curated Practice & Tracker

## Purpose

This directory has **two distinct uses** that run in parallel — neither one is gated behind the other:

1. **Question pool — available on demand, anytime.** John can ask Claude "hit me with a React interview question from 10-interview-prep" at any point in any session, and Claude pulls from the matching sub-folder. This is also the source for **Block 3 (Interview Mini-Challenges)** when a topic in the main roadmap has a clean interview-question fit. Use it however serves the moment: integrated with topic learning, as a session warmup variant, or as a standalone drill on a slow day.
2. **Future timed simulation rounds.** Once Sections 1-7 are mostly complete, this directory *also* becomes the home for full timed interview simulations: 45-min React rounds, 60-min FastAPI rounds, 60-min system design rounds, behavioral rounds. This is *integration practice* — combining everything you've learned under interview conditions. A separate plan will be written when that phase begins.

**Both modes are valid right now.** The only thing to wait on for #2 is timed full simulation rounds — those make more sense after the topic foundations are built. But pulling individual questions on demand is always fair game.

---

## Organization

Sub-folders are by **technology**, not by frontend/backend, because real interview rounds are bucketed that way ("React round", "FastAPI round", "system design round").

**Starting sub-folders (suggestions, not a closed list):**

- `react/` — hooks, performance, state, async patterns, custom hooks
- `fastapi/` — endpoints, async, validation, auth, ORM patterns, middleware
- `postgres-sql/` — query writing, indexing, EXPLAIN ANALYZE, schema decisions
- `system-design-rounds/` — full system design simulations (URL shortener, chat, rate limiter, feed, notifications)
- `ai-rag/` — RAG architecture questions, embedding trade-offs, hybrid search
- `behavioral/` — STAR-format prep, judgment questions

**Add sub-folders as needed.** If John picks up Django, Redis-specific drills, Elasticsearch query design, GraphQL, Kubernetes-flavored questions, or any other tech worth practicing, create a new sub-folder. The list above is a starting scaffold, not a fence. When adding a new sub-folder, mirror the structure: `README.md` with a curated question list, sourced from real interview content.

---

## Rules

1. **No grinding without context.** This is not LeetCode. Ideally questions are grounded in topics you've already studied. If a question references something unfamiliar, it's still fair to attempt — but treat the gap as a signal to revisit the topic in the main roadmap, not to brute-force pattern-match the answer.
2. **Always explain trade-offs out loud.** Every question has a "discuss" component. The code is half the answer; the reasoning is the other half. Practice narrating decisions like you would in a live round.
3. **Time-box.** Mini-challenges: 30-90 min. Timed simulations (later phase): hard 45-60 min cap with 5 min review.
4. **Track every attempt** in the Completion Log below — the global log is the source of truth for what's been worked on. Sub-folder READMEs can have their own per-tech notes if useful, but not required.
5. **Failures are signals.** If a question reveals a topic gap, log it as a weak spot in the relevant section's CLAUDE.md and revisit the topic.

---

## Completion Log

Append to this table after every interview question attempt — Block 3 challenges, on-demand pulls, or future timed simulations. This is the at-a-glance history of what's been practiced.

| Date | Tech | Question (short title) | Mode | Time | Result | Notes |
|------|------|------------------------|------|------|--------|-------|
| — | — | — | — | — | — | — |

**Mode legend:**
- **B3** — Block 3 (mini-challenge integrated with a topic session)
- **OD** — On-demand pull (John asked Claude for a question)
- **SIM** — Timed simulation round (future Mode 2)

**Result legend:**
- **✓** — Solved cleanly, reasoning solid
- **✓ (hints)** — Solved with progressive hints
- **△** — Partial — got most of the way, needs review
- **✗** — Stuck or significantly off — flag the underlying topic as weak

---

## Sources for the curated question lists

Question lists were built from web research on 2025-2026 interview content for mid-senior roles at startups. Sources:

- [GreatFrontEnd — Top React Interview Questions 2026](https://github.com/greatfrontend/top-reactjs-interview-questions)
- [Playcode — React Coding Interview Questions 2026](https://playcode.io/blog/react-coding-interview-questions-2026)
- [Index.dev — 40 Advanced FastAPI Coding Challenges 2026](https://www.index.dev/interview-questions/fastapi-coding-challenges)
- [InterviewBit — FastAPI Interview Questions 2026](https://www.interviewbit.com/fastapi-interview-questions-answers/)
- [Netalith — Python Backend Developer Interview Guide 2026](https://netalith.com/blogs/career-hiring/python-backend-developer-interview-guide-django-fastapi-flask-2026)
- [Toptal — Top Full-Stack Interview Questions 2026](https://www.toptal.com/full-stack/interview-questions)

**Refresh cadence:** Re-research and refresh sub-folder question lists every ~3 months. Interview content shifts with industry trends, and the goal is to stay current — not anchored to a snapshot from a year ago.
