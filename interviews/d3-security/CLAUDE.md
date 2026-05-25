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

> **Last completed:** Lesson 2 — RAG Deep (all 9 chunks + cold quiz + written exercise). Cold quiz B/B+, written exercise B+/A- (~82-85%). Monday 2026-05-25. Mid-session chunk audit ran: Lessons 3-8 now have Tier markers (T1/T2/T3) + per-lesson Trim notes embedded in [lesson-tracker.md](lesson-tracker.md). Honor those at teach-time.
> **Up next:** Lesson 3 — Agents + Tool Use (1.5h, 10 chunks). **Morpheus-core, highest-leverage D3 lesson.** Fresh context window recommended.
> **Lesson plan source of truth:** [lesson-tracker.md](lesson-tracker.md) — read it before teaching anything.

Any context window asked to "continue with D3" → read this section + the Current Position in [lesson-tracker.md](lesson-tracker.md) → pick up from the next chunk. Don't re-teach unless John flags it.

**TEACHING BREVITY RULE (D3 cram only — locked 2026-05-24 Lesson 2 Chunk 1):**
- 8 lessons × multiple chunks each × hand-written notes = brevity is non-negotiable.
- Default to **bullets, not prose**. Diagrams and pipeline flows stay (scannable). Walls of explanatory paragraphs go.
- Each chunk should fit in ~10-15 lines of teaching content before the check question. If it doesn't, trim it.
- John takes hand-notes — he doesn't have time to transcribe textbook paragraphs. Give him **the bullets he'd actually write down**.
- Always include: (1) the killer stat / interview line for that chunk, (2) the vocab, (3) the trade-off framing. Cut everything else.
- If you catch yourself writing a paragraph that opens with "What this means in plain English..." or "Why this matters..." — trim it to one bullet.
- **Teach what WORKS, not what doesn't.** Interviewers ask "what would you use" — not "what would you avoid." Drop comparison tables that exist to dunk on the bad option. One sentence acknowledging the naive baseline is fine; a whole row in a table is not. Mechanism + when-to-use + interview line for the RIGHT tool.
- **Drop hyper-specific benchmark numbers** ("78% recall@10", "~91% with hybrid", "~69% vs ~54%") unless they're an industry-anchor stat John would actually quote (e.g. "73% of RAG failures are retrieval"). Memorizing percentages is Tier 3 trivia no interviewer will quiz on. Use *qualitative* framings instead — "biggest single lever," "step-change improvement," "covers both blind spots."
- **When in doubt, trim.** John's Tier-3 pushback has been right 5+ times this cram. Default cut: any "X% of Y at Z latency" stat that isn't an industry-anchor (like "73% of RAG failures are retrieval"); any product-version enumeration past 2 names; any "what NOT to use" comparison row. Default keep: the killer one-liner, the vocab, the trade-off framing, and any list short enough to be testable as a multi-select. Tier markers are now embedded in `lesson-tracker.md` per chunk (T1 = must know cold; T2 = reason about; T3 = name-drop only) plus a per-lesson Trim notes subsection — honor those at teach-time.

**Open weak spots carried into Lesson 3+ (must surface in mock test):**

*From Lesson 1 (still open):*
- **Structured outputs as a FIX, not just a concept.** On scenarios about "JSON parse failures" or "downstream needs structured data" → first answer is structured outputs / function calling + Pydantic schema, NOT eval-and-retry.
- **System-prompt placement needs BOTH reasons** (trust boundary + prompt caching).
- **`max_tokens` cap** as a cost-control reflex.

*From Lesson 2 (new 2026-05-25):*
- **Vocabulary precision under cold pressure (PRIMARY GAP).** Mechanism is locked across all 9 RAG chunks; SPECIFIC NAMES slip — couldn't name "recursive character splitter" (Q2 cold quiz + Symptom B written), didn't name **RRF (Reciprocal Rank Fusion)** as merge algorithm (Q4 + Symptom A), didn't name **atomic index swap** (Q3 + Symptom C), spelled RAGAS as "RAGA" (Q6). Drill: in mock test, force vocabulary recall on every chunk's canonical names.
- **73% retrieval-failures anchor stat** missed twice in one session (Chunk 1 check + Q1 cold recall). Mechanism solid; the killer NUMBER doesn't surface. Lock the stat.
- **Content-in-wrong-slot pattern (NEW).** Symptom C (a) said "not entirely sure" while answering it fully in (b). On D3 written tests with labeled (a)/(b)/(c) slots, the grader scores per-slot. Always write SOMETHING in every labeled slot, even hedged.
- **Narrowing "retrieval" to embedding only.** Q1 cold quiz, John narrowed "retrieval failures" to "improper embedding." Retrieval is the whole upstream stack (chunking + embedding + vector store + retrieval algorithm + reranking). Watch for this framing miss.

**Strengths locking:**
- **Tier-3 scoping pushback now a documented stable pattern** — 5+ correct trims this cram (Lesson 1: 3 sections; Lesson 2: reranking Chunk 6, RAGAS Chunk 8 trimmed twice). Triggered the mid-session audit that locked Tier markers across Lessons 3-8. Senior-flavor interview triage instinct.
- **Cross-chunk transfer holding** — re-embed cost named unprompted in Q3 + Q4 of cold quiz AND Symptom B + Symptom C of written exercise. Senior signal: not pattern-matching, actually applying mechanism understanding.
- **Real-knowledge senior signal on pgvector hybrid gotcha (Symptom A).** Knew pgvector lacks native hybrid/RRF (unlike ES/Qdrant/Weaviate), would need manual implementation with Postgres FTS. Caseway-anchored real knowledge.
- **Honest "I don't know" pattern stable** — Symptom C (a), Q2 cold quiz "couldn't name it but described it." Conversationally senior; needs the "but I'll try anyway" companion on written tests.

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
- [study-plan/mongodb-essentials.md](study-plan/mongodb-essentials.md) — John's hand-notes scaffold
- [study-plan/system-integration-llm.md](study-plan/system-integration-llm.md) — John's hand-notes scaffold

---

## Session Log

| Date | Focus | Outcome / Notes |
|------|-------|-----------------|
| 2026-05-22 | Intake + full scaffolding | Directory + 4 base files + study-plan README + interview-format + all 8 topic-note scaffolds + logic-puzzles drill bank + mock-test drill bank + **lesson-tracker.md (teaching content + progress tracker)** created. Plan mode → execution. Cram window: Mon+Tue full days, Wed 1h review. Skip C#, defer Round 2 prep, all content in this dir. Initially I wrote 3 topic notes with full content — corrected to scaffolds + lesson-tracker per John's "you teach, I take notes" model. |
| 2026-05-24 | Lesson 1 — AI Engineering Foundations (running ahead of plan, Sunday before Mon+Tue cram) | All 8 chunks taught + cold quiz + first end-of-lesson written exercise. **B+/A- (~78%), PASSED 75% bar.** Cold quiz: A-/B+ (4 of 5 correct cleanly, 1 partial on system-prompt-placement). Written exercise (D3-format 3-symptom diagnostic): B+/A-. Exercise filed at [study-plan/exercises/lesson-01-ai-engineering-foundations.md](study-plan/exercises/lesson-01-ai-engineering-foundations.md). Established `exercises/` directory pattern + locked the lesson-end protocol (cold quiz + written exercise) in lesson-tracker. Trimmed three Tier-3 sections by John's pushback (7-part prompt structure list memorization, 2-pattern structured-output split, router-speed-and-tooling). All three trims correct calls. **Two retrieval-under-pressure misses surfaced** (structured-outputs-as-fix, system-prompt caching reason) — both flagged in Open Weak Spots above. Tracking files updated, ready for fresh-window Lesson 2. |
| 2026-05-25 | Lesson 2 — RAG Deep (Mon Block 2, on schedule) | All 9 chunks taught + cold quiz (B/B+, 7 questions) + written exercise (D3-format 3-symptom diagnostic — **B+/A- ~82-85%, PASSED**). Exercise filed at [study-plan/exercises/lesson-02-rag-deep.md](study-plan/exercises/lesson-02-rag-deep.md). **MID-SESSION CHUNK AUDIT** triggered by John's "is Chunk 6 too granular?" pushback: ran plan-mode audit, trimmed Lesson 2 Chunks 6-9, added **Tier markers (T1/T2/T3) + per-lesson Trim notes** to all of Lessons 3-8 in lesson-tracker.md, extended brevity rules in this file (3 → 4 rules including "when in doubt, trim"). **Two stubborn patterns surfaced (1+1=2 across cold quiz + written exercise):** (1) **vocabulary precision under cold pressure** — mechanism locked, specific names slip (recursive character splitter, RRF, atomic index swap, RAGAS spelling — 4 names missed across the session); (2) **NEW content-in-wrong-slot** on labeled (a)/(b)/(c) written-test format. **Strong wins:** real-knowledge senior signal on pgvector hybrid gotcha (knew it lacks native RRF — Caseway-anchored), cross-chunk transfer holding across cold quiz + written (re-embed cost named 4× unprompted), Tier-3 scoping instinct now a documented stable pattern (5+ correct trims this cram). Tracking files updated, fresh window recommended for Lesson 3. |
