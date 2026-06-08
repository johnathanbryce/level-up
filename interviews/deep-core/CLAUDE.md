# Deep Core Technology — Interview Prep

## Status

**ACTIVE** — Round 2 (technical discussion / opinions) confirmed **Wed 2026-06-10, 8:15 AM PT**. 45 min, remote, **no hands-on coding**.

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

> **Scaffolding built 2026-06-08 (Mon). Teaching not yet started.**
>
> **Cram window:** Mon 2026-06-08 afternoon (2-4h, fresh — front-load hard stuff) + Tue 2026-06-09 (full day, breadth + reinforcement + mock) + Wed AM light review before 8:15 AM.
>
> **Day plan:**
> - **Mon (today):** Lesson 1 (Agentic Orchestration) + Lesson 2 (Claude Code Internals). Highest-leverage + highest-interest + explicitly screened. End each with a quiz.
> - **Tue:** Lesson 3 (Caseway stories, spoken + tightened) + Lesson 4 (System Design — reactivation + AI framing) + Lesson 5 (Opinions rapid-fire) + Lesson 6 (Questions for Jeff + close). Full mock Q&A at the end.
>
> **⏱ ONE DAY of real study time — NO weeds.** Bar = speak intelligently about SWE trade-offs + AI. Stack focus = Next.js / TypeScript / Python. Supabase/Cesium NOT studied (one-line fallback only). Geology NOT studied (product context only). System design IS in scope (Jeff may probe). See TIME REALITY block in [lesson-tracker.md](lesson-tracker.md).
> - **Wed AM:** light reflex pass + re-read questions-for-Jeff. No new content.
>
> **Teaching source of truth:** [lesson-tracker.md](lesson-tracker.md). Teach from it chunk-by-chunk; John takes notes in `study-plan/<topic>.md`; quiz at end of each lesson.

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

- **[lesson-tracker.md](lesson-tracker.md)** — TEACHING CONTENT + PROGRESS. Read first when resuming.
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

---

## Session Log

| Date | Focus | Outcome / Notes |
|------|-------|-----------------|
| 2026-06-08 | Intake + scaffolding | Folder + 4 base files + study-plan README + 7 topic-note scaffolds + lesson-tracker (7 lessons) created. Round 1 already passed (casual intro). Round 2 = 45-min technical discussion/opinions, no coding, Wed 2026-06-10 8:15 AM. Day plan: Mon (L1 Agentic + L2 Claude Code), Tue (L3-L7 + mock), Wed AM light review. |
