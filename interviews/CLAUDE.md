# Interviews — Per-Company Cram Pipeline

## Purpose

This directory is for **company-specific** interview prep — by-company, time-bound, per-opportunity. Each company gets its own folder with research, role analysis, study plan, behavioral prep, and post-interview debriefs.

Distinct from [10-interview-prep/](../10-interview-prep/), which is the by-technology generic question pool. This directory does NOT depend on that one — they are standalone. If a question from `10-interview-prep/<tech>/` happens to map to a company's stack, you can reference it manually during cram, but no automated dependency.

---

## Active Interviews

| Company | Role | Date | Status | Next Action |
|---------|------|------|--------|-------------|
| [Remitly](remitly/) | TBD (likely AI SWE) | 2026-05-20 | Active | Company research + behavioral prep |

---

## Company Index

| Company | Folder | Status |
|---------|--------|--------|
| Remitly | [remitly/](remitly/) | Active |

---

## Priority Mode

When at least one company has status `Active` with a future interview date, sessions DEFAULT to interview cram.

**Default session shape (Priority Mode on):**
1. Algorithm warmup (15-30 min) — kept. Fluency reps that transfer directly to interviews.
2. Bridge recall (2-3 min) — kept. Pulls from prior roadmap topics.
3. **Interview cram block (45-120 min)** — replaces Block 2 roadmap topic. Pulls from the active company's folder (research, behavioral, role-specific drilling).

**At session start, Claude announces the default** — e.g. *"Remitly is active — defaulting to interview cram today. Say the word if you want regular pipeline instead."*

**Fluid opt-out.** John can say "regular pipeline today" or "need a break from interview prep" at any session start and Claude switches without friction. No forced lock-in.

**Reverting to regular pipeline.** Once the interview is logged in the company's `interview-log.md` and any surfaced gaps are written back to the relevant roadmap section CLAUDE.md, the company moves to `Closed` and the default reverts.

---

## Per-Company Workflow (7-step)

When a new company lands:

1. **Intake** — populate the company's `CLAUDE.md`: status, interview date, role (or "TBD"), source (referral / recruiter / applied), interviewer if known.
2. **Company research** — web search for mission, products, recent news (last 6-12 months), engineering blog, public architecture, leadership. Output: top half of `talking-points.md` + a memorized 2-3 sentence elevator pitch.
3. **Role analysis** — paste JD verbatim into `role.md` when available. Extract tech stack, responsibilities, seniority signals. If JD is unknown, prep against an archetype (e.g. "AI software engineer at a fintech / payments company") until the role lands.
4. **Study plan build** — `study-plan/README.md` maps the role's stack to roadmap sections, flags gaps to drill, lays out a day-by-day cram schedule. Topic-specific notes go into `study-plan/` as sibling files. Uploaded materials (recruiter PDFs, JD docs, decks, public talks) also live in `study-plan/`.
5. **Behavioral prep** — bottom half of `talking-points.md`: "tell me about yourself," "why this company," "why are you leaving," 4-6 STAR stories tailored to the role, standard curveballs.
6. **Mock rounds (optional)** — if time allows. Log into `interview-log.md` with `(Mock)` prefix in the Round column.
7. **Debrief** — after each real round: log questions, performance, follow-ups, surfaced gaps. Gaps get fed back into the main roadmap as weak spots — write them into the relevant section's CLAUDE.md so they surface in future learning sessions.

---

## Per-Company Folder Shape

```
<company>/
  CLAUDE.md            <- state, status banner, cram focus, session log
  role.md              <- JD, tech stack, responsibilities
  talking-points.md    <- company research (top) + STAR stories / "why X" (bottom)
  interview-log.md     <- per-round debriefs
  study-plan/
    README.md          <- cram plan + index of files in this folder
    (topic notes, uploaded PDFs, recruiter docs — added as needed)
```

**4 files + 1 directory.** Lean by design. No `_template/` folder — convention is documented here and followed when adding a new company.

---

## How to Add a New Company

1. Create `interviews/<company>/`.
2. Seed the 4 base files (`CLAUDE.md`, `role.md`, `talking-points.md`, `interview-log.md`) and the `study-plan/` directory with `README.md`. Copy section structure from [remitly/](remitly/) as the reference.
3. Run intake (step 1 of the 7-step workflow).
4. Add the company to the **Active Interviews** and **Company Index** tables above.
