# Deep Core Technology — Interview Prep

## Status

**ACTIVE** — Round 2 (technical discussion/opinions) **DONE 2026-06-10**, went well (~70% est. to advance). **Now prepping Round 3 = PAIRED PROGRAMMING** (hands-on coding). John has never done a paired-programming round before — prep format + reps. Coding rep: `interviews/deep-core/samples-app/` (A1, complete). Stack: Next.js / TS / Python / FastAPI (NOT Cesium; Supabase only if quick to spin up). See [interview-log.md](interview-log.md) Round 3 block + the R3 master prompt handoff.

## Interview Info

- **Date:** Wednesday 2026-06-10, 8:15 AM PT (remote)
- **Format:** 45-min technical discussion + opinions questions. NO live coding this round.
- **Interviewer:** Jeff Thorslund — CTO + co-founder
- **Role:** Founding Engineer (employee #1). $105-125K CAD + 1% equity. Remote, Canada-eligible. HQ Squamish BC.
- **Round 1:** Casual intro chat with Jeff — PASSED (advanced to this round).

---

## What This Round Actually Tests (read before teaching)

No live coding = they already believe John can code. A 45-min "discussion/opinions" round for a **founding engineer** answers three questions:

1. **Does he reason clearly about hard engineering trade-offs out loud?** (the "opinions" part — they'll poke)
2. **Does he actually understand agentic systems deeply, or just use them?** (Jeff's explicit screen; the thing that separates John from a generic full-stack dev)
3. **Will he be a good co-builder?** (ownership, communication, how he handles "I don't know," how he disagrees)

NOT on the list: Supabase trivia, Cesium API surface, geology facts. Those are table stakes / informed-curiosity only. **Do not burn prep time memorizing their stack — judgment + agentic depth win a founding role.**

**John's #1 failure mode this round is NOT under-knowing — it's overclaiming or rambling.** He has strong material; the risk is burying it. Drill: tight answers, name the trade-off, give the honest gap. A founding CTO prefers "I haven't hit that at scale, here's how I'd reason about it" over a confident-wrong answer.

---

## Honesty Guardrails (enforce in every mock answer)

- "**Lead engineer**," never "sole." History if asked: founding team built v1; John took over as the only engineer ~a year ago and owns everything since.
- Bespoke **LangChain/LangGraph v2 rewrite is in-progress/unmerged** → "leading the rewrite," NEVER "shipped."
- Per-user ES index isolation on Bespoke: John **contributed**, design isn't his. His isolation story is **Casey's upload isolation** (user_uploads ES index scoped by user_id, 24h TTL, Redis keys scoped per user/chat/file).
- The **$150→$60/day** number is real but from the **billing dashboard**, not the repo. "Measured in production."
- **Don't fake geology or Cesium.** Curiosity + fast-ramp evidence beats bluffing.

---

## Current Position — READ THIS FIRST

> **SCOPE RESHAPED 2026-06-08 (Mon) mid-session.** This is NOT a concept-learning cram — John builds agentic systems daily. It's an **articulation + opinion-readiness cram**: drill tight, honest, spoken answers to what Jeff will actually ask. Kill lecturing on self-evident concepts; deliverable = crisp spoken line + honest anchor. Full reshape detail (5 areas, cuts, backend inference) lives in the [lesson-tracker.md](lesson-tracker.md) Current Position block — read it.
>
> **Two-day split (locked):**
> - **Mon PM/eve (today): NOTE-TAKING + quizzes mixed in** across 5 areas: (1) Agentic must-knows [screen], (2) AI foundations refresh, (3) System design framed to their product, (4) Database/backend, (5) React/Next high-level.
> - **Tue:** depth + mock drilling — Caseway stories tightened, opinions rapid-fire, full mock Q&A.
> - **Wed AM:** light reflex pass + re-read questions-for-Jeff. No new content.
>
> **CI/CD + monitoring = LIGHT PASS** (explicitly in JD). **Supabase = "managed Postgres + RLS" one-liner; Cesium = "web 3D engine, large-mesh perf is the hard part"; geology = product context only.** Stack focus = Next.js / TypeScript / Python.
>
> **Likely backend (peer-level inference, confirm w/ Jeff):** Next.js (Node) app layer via route handlers/server actions (NOT separate Express) + standalone **Python** geostat/agent services + Supabase Postgres.
>
> **ALL 5 notes areas DONE (Mon eve):** Area 1 (agentic + Claude Code internals — tool-calling mechanism, MCP/hooks w/ code+diagrams), Area 2 (`ai-foundations.md` — RAG/hybrid/embeddings-vs-response caching nuance), Area 3 (`system-design.md` — all 11 concepts), Area 4 (`backend-databases.md` — architecture, Supabase/RLS, long-job persistence), Area 5 (`react-nextjs.md` — MEDIUM level, all 8 chunks). Notes audited (heading consistency fixed).
>
> **3 accuracy flags John still needs to patch in `react-nextjs.md`:** (1) ch.7 — **ISR is missing** from the rendering-strategies list (he listed SSG/SSR/CSR only; add ISR = SSG + revalidate timer); (2) ch.4 controlled/uncontrolled one-liner overweights re-renders — better framing: "controlled when I need to validate/react to every keystroke; uncontrolled when I just need the value on submit"; (3) ch.7 Server Actions directive typo "user server" → **"use server"**.
>
> **ALL quizzes + interview-style Qs deferred to Tue** (John's call — Mon = notes-building, Tue = drill/mock at home).
>
> **TUE PLAN (rebalanced — John's read: this is a conversational/experience round, likely lighter than prepped; Round 3 = paired programming):**
> - **HIGH:** Caseway stories (tight/honest/spoken) + agentic talking points reflexive + **Caseway-mapping reflex** (the one real weak spot — designs well abstractly, doesn't anchor to his own work).
> - **MEDIUM:** opinions/trade-off rapid-fire + questions for Jeff.
> - **THEN, if time permits → pivot to HANDS-ON CODING PRACTICE** to get ahead for Round 3 (paired programming). See R3 prep note below.
> - **Throughout:** tighten spoken delivery — rambling is the #1 risk.
>
> **ROUND 3 PREP (paired programming) — flesh out together, noted 2026-06-08:** John has NEVER done a paired-programming interview (only live-coding assessments) — so prep BOTH (a) the **format** (collaborative, think-out-loud, ask clarifying Qs, communicate trade-offs; it's about how you work *with* someone, not just landing the answer) AND (b) **real-world reps** on their stack (Next.js/TS/Python), NOT LeetCode. Candidate exercises to detail later: (i) build a small backend API + wire it up + consume it on a pre-built Next.js frontend; (ii) find-and-fix bugs in a faux mini-codebase. May need a small scaffolded repo to practice in.
>
> **Grading bar (spoken round):** fluency, honesty, brevity. #1 risk = overclaiming/rambling. Every answer ~15-25 sec: name trade-off, take a position, honest caveat, STOP.
>
> **Teaching source of truth:** [lesson-tracker.md](lesson-tracker.md). John takes notes in `study-plan/<topic>.md`; quiz at end of each area.

**If a fresh window is asked to "continue Deep Core":** read this block + the Current Position in [lesson-tracker.md](lesson-tracker.md). Confirm which lesson to resume; do NOT re-teach completed lessons.

---

## Teaching Brevity Rules (carried from D3, they worked)

- **Default to bullets, not prose.** John takes hand-notes; give him the bullets he'd actually write.
- **Teach what WORKS, not what doesn't.** Opinions questions ask "what would you use / how would you reason" — not "what to avoid." One sentence on the naive baseline is fine; no comparison tables that exist to dunk on bad options. (See [[feedback-teach-what-works]] memory.)
- **Tier markers:** T1 = speak fluently + unprompted; T2 = reason about if asked; T3 = recognize / one-line only. John's Tier-3 scoping pushback has been right 5+ times across crams — honor it.
- **When in doubt, trim.** This is a 45-min chat, not a written exam. Depth where it's screened (agentic, Claude Code), breadth-only elsewhere.
- **Chunk teaching** — never dump a whole lesson at once; one chunk → check question → confirm → next. (See [[feedback-teaching-pace]].)

---

## Company Quick Facts

- **Deep Core Technology** (deepcoretech.com), Squamish BC. **"The subsurface thinking partner."**
- **Product:** agentic 3D geologic modeling platform for mining / mineral exploration. Geologist describes geology in natural terms → system reasons through data integration, model construction, iteration, validation. **"Turn drill results into interactive 3D models in minutes."** Turns geologists from software *operators* back into *interpreters*.
- **Founders:** Neil Seifert, CEO (structural geologist, MSc, 10+ yrs exploration/mining/civil) + Jeff Thorslund, CTO (10+ yrs software for the resource sector). John = employee #1.
- **Stack:** TypeScript, Python, Next.js, Supabase, Cesium. Work "rooted in agentic systems" — they explicitly want Claude Code internals + orchestrating agents for complex discrete tasks.
- **Data types:** drillhole data, geologic maps, 2D/3D geophysics, block models, historical reports, 3D models. **Security:** customer data private, not trained on.
- **Stage:** actively fundraising. Salary funded $105-125K + 1% equity. Yearly month abroad (last: Oaxaca).
- **Incumbents:** Seequent Leapfrog, Datamine, Micromine, Maptek Vulcan. **Wedge:** agentic reasoning + zero learning curve + web-based.
- **Target users:** junior mining companies, exploration/evaluation teams. Future markets: geothermal, carbon storage, water, civil.

---

## Files in This Folder

- **[study-plan/round-3-paired-programming.md](study-plan/round-3-paired-programming.md)** — **ROUND 3 PREP (CURRENT FOCUS).** Format rubric + assignment ladder (A1–A4, hands-off dial increases each rep) + progress. Read first for R3.
- **[lesson-tracker.md](lesson-tracker.md)** — TEACHING CONTENT + PROGRESS (Round 2). Read first when resuming R2 content.
- [role.md](role.md) — role analysis, stack table, gap inventory, must-knows, why-fit
- [talking-points.md](talking-points.md) — company research + intro + STAR anchors
- [interview-log.md](interview-log.md) — per-round debriefs
- [study-plan/README.md](study-plan/README.md) — day-by-day plan + file index
- `study-plan/agentic-orchestration.md` — John's notes (Lesson 1)
- `study-plan/claude-code-internals.md` — John's notes (Lesson 2)
- `study-plan/caseway-stories.md` — John's notes (Lesson 3)
- `study-plan/system-design.md` — John's notes (Lesson 4)
- `study-plan/opinions-tradeoffs.md` — John's notes (Lesson 5)
- `study-plan/questions-and-close.md` — John's notes (Lesson 6)
- `study-plan/ai-foundations.md` — John's notes (Area 2 — AI foundations refresh / RAG; created 2026-06-08)
- `study-plan/backend-databases.md` — John's notes (Area 4 — DB/backend; created 2026-06-08)
- `study-plan/react-nextjs.md` — John's notes (Area 5 — React/Next high-level; created 2026-06-08)

---

## Session Log

| Date | Focus | Outcome / Notes |
|------|-------|-----------------|
| 2026-06-08 | Intake + scaffolding | Folder + 4 base files + study-plan README + 7 topic-note scaffolds + lesson-tracker (7 lessons) created. Round 1 already passed (casual intro). Round 2 = 45-min technical discussion/opinions, no coding, Wed 2026-06-10 8:15 AM. Day plan: Mon (L1 Agentic + L2 Claude Code), Tue (L3-L7 + mock), Wed AM light review. |
| 2026-06-08 PM | SCOPE RESHAPE + Area 1 start | John (correctly) flagged plan over-indexed on teaching concepts he already owns → reshaped to articulation/opinion-readiness cram. Mon = notes+quizzes across 5 areas; Tue = depth+mock. Backend inferred (Next.js + Python geostat services + Supabase). Area 1 started: ReAct vs planner-executor (B-, rambled), trust stack taught. 2 new note scaffolds created + agentic notes realigned. |
| 2026-06-10 | R2 done + **R3 paired-programming prep kickoff** | R2 (technical/opinions) went well (~70% to advance). Pivoted to **Round 3 = paired programming** (John's first ever). Built [study-plan/round-3-paired-programming.md](study-plan/round-3-paired-programming.md): format rubric + **A1–A4 assignment ladder** (hands-off dial increases each rep, per John's ask). Web-searched pairing format. **Algo warm-up:** group_tags.py (Python, anagram grouping — defaultdict/setdefault, builtin-shadowing gotcha) + merge_bookings.ts (JS, merge intervals — both PASS; recurring inverted-condition + boundary-operator bugs). **A1 (Samples Explorer) started:** `sandbox/interview-prep/deep-core/samples-app/` — isolated per-project env strategy locked (venv-per-project, not shared; cache makes reinstall cheap). Backend venv + FastAPI working route skeleton. Lessons landed: APIRouter `include_router` ordering, Pylance interpreter selection (the "import could not be resolved" / no-colors-on-fastapi issue = editor interpreter ≠ runtime venv), uvicorn CLI vs `__main__`, routes fire per-request, `return` not `print`. Slice 1 (GET /samples) done. **Next:** A1 slice 2 = Pydantic models → GET-by-id/POST/DELETE/filter/CORS, then frontend + SQLite Day 2. Morale note: John re-engaged + having fun; flagged LLM-offload atrophy of production muscle (comprehension intact) — the rep ladder targets exactly this. |
| 2026-06-11 | **R3 prep Day 2 — A1 COMPLETE** + Build Reps track created | **A1 (Samples Explorer) DONE end-to-end.** Backend: CORS added (taught SOP vs CORS — browser-enforced, *relaxes* not protects; origin = scheme+host+port; curl ignores it; `*` + credentials forbidden). Frontend (Next.js 16 / React 19, App Router): John wrote the client — `useEffect` fetch w/ **AbortController** (taught as a generic cancellation token; vs the `ignore`-flag race fix — discard vs cancel), loading/error/empty states, debounced `rock_type` filter, **extracted `useDebounce` hook** (taught setTimeout + clearTimeout = the debounce mechanism; generic `<T>` + delay param as the canonical shape). Reviewed + fixed: fetch-fired-on-`input`-not-`debounced` (debounce was inert), inverted loading condition (his recurring bug-type), loading-never-reset, error-on-abort, non-mutually-exclusive render states. SQLite (Part 3): swapped in-memory for `sqlite3` behind same routes — taught the **DB-API (connect→cursor→execute→fetch→commit→close), parameterized `?` placeholders (injection), `lastrowid` (POST), `rowcount` (DELETE 404), `sqlite3.Row`→dict, FastAPI lifespan, and the cross-tool transfer (sqlite3 → psycopg, same DB-API, `%s` + DSN)**. John wrote all routes incl. the 3 SQLite conversions; Claude wrote `list_samples` as the template + scaffolded `db.py`. Algo warm-ups: `top_rock_types.py` (PY) + `merge_drill_logs.ts` (JS) — logged in `01-algorithms/CLAUDE.md`. **Big outcome: John wants hands-on build reps as a recurring track → created [reps/](../../reps/) (fluid, pull-based, "let's do a rep"). Rep 001 (Postgres + Docker Compose, **backend-heavy** — rep the FastAPI route/CORS/SQL muscle against a real DB; frontend light) queued for Fri 2026-06-12.** Strong session: clarifying-Qs + plan-in-beats + cross-tool pattern-hunting (DB-API, AbortController generality) all senior-flavor. |
