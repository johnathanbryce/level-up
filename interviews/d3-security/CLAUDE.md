# D3 Security — Interview Prep

## Status

**ACTIVE** — Round 1 (written test) confirmed for Wed 2026-05-27 3pm PT.

## Interview Info

- **Date:** Wednesday 2026-05-27, 3:00 PM PT (in-person)
- **Format:** Round 1 — 2-hour in-person written test. Closed-book, no phone, no internet, no AI. D3-provided laptop, bookmarked Chrome link.
- **Test parts:**
  - Part 1: Multi-Select Choice Questions
  - Part 2: Short Structured Answers (bullets, pseudo-code, architecture descriptions)
- **Named topic areas:** System Integration, Multi-Agent Governance, Prompt/Trust Controls
- **Location:** 300-1075 W Georgia St, Vancouver, BC V6E 3C9 (3rd floor)
- **Role:** AI Engineer
- **Source:** Direct application; recruiter outreach 2026-05-22
- **Format note:** Per Glassdoor pattern across all D3 roles, the test universally includes a large logical-reasoning section (~90 min, multi-select, no coding) alongside the named topic blocks. See [study-plan/interview-format.md](study-plan/interview-format.md) for full intel.

---

## Quick Facts

- **What D3 does (one-liner):** Vancouver-HQ cybersecurity company; builds **Morpheus**, an AI-driven Autonomous Security Operations Center (ASOC) platform that automates Tier 1-3 analyst work (alert triage + investigation + response).
- **Scale:** Morpheus triages 100% of alerts in <3 min, L2-depth investigations, 800+ security tool integrations. Showcased at RSA 2025; 24 months of dev by 60 specialists.
- **Competitive landscape:** ASOC space includes Torq, Tines, Dropzone AI, Prophet Security.
- **D3 interview reputation:** Glassdoor 14% positive interview rating; reputation for unconventional / "IQ-test" questions. Treat as rigorous.

---

## Current Position — READ THIS FIRST

> **Last completed:** _Nothing yet — cram not started. Scaffolding only._
> **Up next:** Lesson 1 — AI Engineering Foundations, Chunk 1 (Mon Block 1).
> **Lesson plan source of truth:** [lesson-tracker.md](lesson-tracker.md) — read it before teaching anything.

Any context window asked to "continue with D3" → read this section + the Current Position in [lesson-tracker.md](lesson-tracker.md) → pick up from the next chunk. Don't re-teach unless John flags it.

---

## Current Cram Focus

**2-day compressed cram (Mon 2026-05-25 + Tue 2026-05-26) + 1h Wed morning review.** Sunday for scaffolding only (Claude lands base files).

**Active learning model** — Claude TEACHES from [lesson-tracker.md](lesson-tracker.md); John takes hand notes in `study-plan/<topic>.md` scaffolds as each chunk lands. Same pattern as Remitly Phase 1.

Top 3 priorities:

1. **AI Engineering depth** — LLM application patterns, RAG architecture, agents + tool use. Transferable beyond D3.
2. **Logic puzzles** — 6/day daily warmup across 10 pattern categories. John's weakest area; drilled to reflex.
3. **D3-specific context + light prompt/safety + multi-agent governance concepts.** Concept-level, not framework-acronym memorization.

Deferred entirely: Round 2 (Hiring Manager) prep — only built out if Round 1 passes.

---

## Files in This Folder

- **[lesson-tracker.md](lesson-tracker.md)** — **TEACHING CONTENT + PROGRESS TRACKER.** Claude teaches from this. Always read first when resuming.
- [role.md](role.md) — JD analysis, stack table, gap inventory, must-knows
- [talking-points.md](talking-points.md) — stub; Round 2 prep deferred
- [interview-log.md](interview-log.md) — per-round debriefs (filled after Round 1)
- [study-plan/README.md](study-plan/README.md) — 2-day cram schedule index
- [study-plan/interview-format.md](study-plan/interview-format.md) — D3 test format detail (per email + Glassdoor)
- [study-plan/logic-puzzles.md](study-plan/logic-puzzles.md) — **drill bank** (18 puzzles + protocol; full content, not a scaffold)
- [study-plan/mock-test.md](study-plan/mock-test.md) — **drill bank** (2 mock sittings + answer keys; full content)
- [study-plan/ai-engineering-foundations.md](study-plan/ai-engineering-foundations.md) — John's hand-notes scaffold
- [study-plan/rag-deep.md](study-plan/rag-deep.md) — John's hand-notes scaffold
- [study-plan/agents-and-tool-use.md](study-plan/agents-and-tool-use.md) — John's hand-notes scaffold
- [study-plan/multi-agent-governance-light.md](study-plan/multi-agent-governance-light.md) — John's hand-notes scaffold
- [study-plan/prompt-safety-essentials.md](study-plan/prompt-safety-essentials.md) — John's hand-notes scaffold
- [study-plan/soc-domain-primer.md](study-plan/soc-domain-primer.md) — John's hand-notes scaffold
- [study-plan/mongodb-essentials.md](study-plan/mongodb-essentials.md) — John's hand-notes scaffold
- [study-plan/system-integration-llm.md](study-plan/system-integration-llm.md) — John's hand-notes scaffold

---

## Session Log

| Date | Focus | Outcome / Notes |
|------|-------|-----------------|
| 2026-05-22 | Intake + full scaffolding | Directory + 4 base files + study-plan README + interview-format + all 8 topic-note scaffolds + logic-puzzles drill bank + mock-test drill bank + **lesson-tracker.md (teaching content + progress tracker)** created. Plan mode → execution. Cram window: Mon+Tue full days, Wed 1h review. Skip C#, defer Round 2 prep, all content in this dir. Initially I wrote 3 topic notes with full content — corrected to scaffolds + lesson-tracker per John's "you teach, I take notes" model. |
