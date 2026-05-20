# Remitly — Interview Prep

## Status

**ACTIVE — awaiting hiring manager decision** (recruiter screen passed 2026-05-20 with positive signal; Phase 2 technical cram active in parallel)

## Interview Info

- **Date:** 2026-05-20 (Wednesday) — intro chat
- **Role:** TBD — three target SDE II roles in **Burnaby, BC** (all $124K+ CAD base):
  1. **SDE II, Home and Explore** (frontend — React/TS) — strongest stack match
  2. **SDE II, Customer Data Platform** (backend — AWS/DynamoDB) — stretch on backend depth
  3. **SDE II, WARP / Wallet Product Risk** (polyglot — Go/Java/Kotlin/TS, fraud/risk)
  See [role.md](role.md) for full JD analysis of all three.
- **Source:** TODO — fill in (referral / recruiter / direct application)
- **Interviewer:** TODO — fill in if known (likely recruiter, not engineer, at this stage)
- **Format:** Recruiter screen — ~30 min, conversational. Behavioral, experience walkthrough, role overview. Not technical.

---

## Quick Facts

- **What Remitly does (one-liner):** Seattle-headquartered digital cross-border remittance and consumer fintech (NASDAQ: RELY, ~$3B market cap) — sends money to 170+ countries for ~9.6M quarterly active customers, now repositioning from a single-product transfer app into a four-pillar "financial partner" for immigrants (Send, Spend, Save, Borrow).
- **Tech stack across the 3 target roles:** **TypeScript / React / CSS** (Role 1), **AWS / DynamoDB / distributed systems** (Role 2), **Go / Java / Kotlin / TS / React Native / AWS / message brokers** (Role 3). Broader Remitly stack: **Go + Java/Kotlin + Python** backends, **React/TS** frontends, **AWS + Docker + K8s**, **Python/PyTorch** for ML.
- **Strategic 2026 context:** New CEO **Sebastian Gunningham** (ex-Santander Openbank / Amazon S-team) took over Feb 2026. Q1 2026 was a record quarter — $452.8M revenue (+25% YoY), net income +332% YoY — and management publicly attributed margin expansion to **AI-driven internal efficiency**.
- **Honest seniority read:** All three roles ask **4-5+ years** experience; John has **~3 years total**. Not a disqualifier for an intro chat, but the conversation will be evaluating whether John can credibly step up. Frame: depth of ownership + Python/AI integration experience as differentiators, not years.

---

## Current Cram Focus

**Phase 1 — recruiter screen prep:** COMPLETE 2026-05-20.

**Phase 2 — technical cram:** ACTIVE in parallel while awaiting hiring manager decision.

Top 3 priorities for Phase 2:

1. **LeetCode reps daily** — focus on JS/Python, patterns aligned to current [01-algorithms/CLAUDE.md](../../01-algorithms/CLAUDE.md) state. Build test cases as part of every solution (stated requirement of Remitly's T1 format).
2. **STAR story drafts** — T1 includes 1-2 behavioral. Have 3-4 stories ready: Caseway scope-jump (CTO + dev left), AI integration / RAG work, full-stack delivery, failure/learning.
3. **System design fundamentals refresh** — covered for one of the 4 loop rounds. Pull from [02-system-design/CLAUDE.md](../../02-system-design/CLAUDE.md) — request lifecycle, caching, rate limiting, DB scaling, idempotency.

Role-specific cram (frontend perf / DynamoDB deep / fraud systems) activates when the hiring manager confirms which of the 3 target SDE II roles is in play.

See [study-plan/phase-2-technical-cram.md](study-plan/phase-2-technical-cram.md) for the full plan.

---

## Files in This Folder

- [role.md](role.md) — top 5 SWE roles at Remitly that match the profile + tech stack consensus + seniority signals
- [talking-points.md](talking-points.md) — company research (filled) + STAR stories / "why X" (TODO — next session)
- [interview-log.md](interview-log.md) — per-round debriefs
- [study-plan/README.md](study-plan/README.md) — cram plan + topic notes index
- [study-plan/interview-format.md](study-plan/interview-format.md) — what to expect from the Remitly interview loop
- [study-plan/](study-plan/) — topic notes + uploaded materials, grows fluidly

---

## Session Log

| Date | Focus | Outcome / Notes |
|------|-------|-----------------|
| 2026-05-17 | Scaffolding | Directory + seed files created. |
| 2026-05-17 | Deep web research (2026) | Remitly company / eng signals / careers / interview format surfaced. `talking-points.md` Part 1 filled. `role.md` initially scaffolded toward AI-Native / KDE roles. |
| 2026-05-17 | Job-posting analysis (3 SDE II roles John applied for) | Realistic target landscape confirmed: 3 Burnaby BC SDE II roles ($124K+ CAD base) — Home and Explore (frontend), Customer Data Platform (backend), WARP / Wallet Product Risk (polyglot). `role.md` rewritten with verbatim JDs. `CLAUDE.md` Quick Facts + Cram Focus recalibrated. **Honest seniority read added: 4-5+ yrs required vs. John's ~3 yrs — stretch, not disqualifier.** |
| 2026-05-19 | Phase 1 cram — folder restructure + study plan scaffolding | Phase 1 / Phase 2 split established. 5 topic notes scaffolded: `react-js-ts.md`, `dynamodb-nosql.md`, `aws-services.md`, `payments-domain.md`, `message-brokers.md`. React/JS/TS section written + quizzed (B+). DynamoDB written + quizzed (B+). **Two mid-section conceptual corrections locked through quiz:** (1) Eventual vs strong consistency — John had inverted; corrected. (2) Single-table design — "dump everything" misframe corrected to "deliberate access-pattern-first design." |
| 2026-05-20 | Phase 1 completion + Recruiter screen + Phase 2 activation | AWS / Message Brokers / Payments sections completed (Payments trimmed 60% to idempotency + settlement vs disbursement only). "Tell me about yourself" + "Why Remitly" drafted and iterated through 2 cycles each. **Recruiter screen complete — 20 min casual, no tech, positive signal.** Interview process for tech rounds shared (T1 live LC + test cases + STAR; 15-min prep call; 4-round loop). Phase 2 activated — focus on LeetCode reps + STAR story drafts in parallel while awaiting hiring manager decision. Full debrief in [interview-log.md](interview-log.md). |
