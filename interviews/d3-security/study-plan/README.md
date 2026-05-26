# D3 Security — Study Plan

For JD analysis (tech stack, coverage, gap inventory, must-knows, cram priorities), see [../role.md](../role.md).

**The detailed lesson plans + per-chunk teaching content + progress tracker live in [../lesson-tracker.md](../lesson-tracker.md).** Claude teaches from there; John takes hand notes in the per-topic scaffold files in this folder.

This file is the high-level **2-day compressed cram schedule** + topic-notes index.

---

## Days Remaining

- **Friday 2026-05-22** — today (scaffolding only)
- **Saturday 2026-05-23** — off
- **Sunday 2026-05-24** — optional light start (1-2h if John has time; otherwise nothing)
- **Monday 2026-05-25** — full study day (~6-7h)
- **Tuesday 2026-05-26** — full study day + mock test (~6-8h)
- **Wednesday 2026-05-27** — 1h morning review only. Interview at 3:00 PM.

---

## Goal — what "ready" looks like

By Tuesday 2026-05-26 evening, John can:

1. Hold a real conversation about AI engineering concepts (LLM app patterns, RAG architecture, agent loops, multi-agent governance, prompt safety) in his own words, *not* as memorized vocabulary.
2. Recognize logic-puzzle category in <30s and reach for the trick.
3. Sketch 3 canonical architectures cold on paper in <5 min each.
4. Hand-write 3 reusable pseudo-code skeletons from memory.
5. Pass a 90-min mock test of D3's actual format at ≥75%.

**Out of scope (deferred entirely):**
- C# coverage (JD says Python AND/OR; lean on Python strength)
- Round 2 / behavioral prep (deferred until Round 1 passes)
- OWASP LLM Top 10 / NIST AI RMF acronym memorization (concept-level only)
- LeetCode-style algo practice (test format is architecture-flavored pseudo-code, not data structures)

---

## Compressed Cram Schedule (Mon + Tue)

### Monday 2026-05-25 — AI Engineering Depth (~6-7h)

| Block | Time | Activity |
|---|---|---|
| Warmup | 30 min | 3 logic puzzles cold (weighing + harmonic mean + bridge crossing) |
| Block 1 | 1.5h | Read + study `ai-engineering-foundations.md` — LLM application patterns, structured outputs, streaming, error handling, cost control |
| Break | 15 min | |
| Block 2 | 2h | Read + study `rag-deep.md` — full RAG architecture, chunking, retrieval, eval. Anchor in Caseway experience |
| Lunch | 45 min | |
| Block 3 | 1.5h | Read + study `agents-and-tool-use.md` — ReAct, function calling, multi-agent basics |
| Wrap | 30 min | 3 more puzzles (knights/knaves + probability + pigeonhole) + 20-card vocab self-quiz |

### Tuesday 2026-05-26 — D3-Specific + Mock + Polish (~6-8h)

| Block | Time | Activity |
|---|---|---|
| Warmup | 30 min | 3 logic puzzles (hat/prisoner + sequence + clock) |
| Block 1 | 1h | Read + study `multi-agent-governance-light.md` (concept-level, not framework cram) |
| Block 2 | 1h | Read + study `prompt-safety-essentials.md` (4-5 concepts) |
| Block 3 | 30 min | Skim `mongodb-essentials.md` (NoSQL primer) + skim `system-integration-llm.md` |
| Break | 30 min | |
| **MOCK** | 90 min | **Mock test, paper, closed-book, no laptop.** Mix of multi-select + structured answers. See `mock-test.md` |
| Grade | 45 min | Grade + identify top 3 weak areas |
| Patch | 1h | Targeted re-read of weakest 2 notes |
| Wrap | 30 min | 3 more puzzles (geometry + 2 weak categories) + vocab reflex pass |

### Wednesday 2026-05-27 morning — Final polish (~1h)

| Block | Time | Activity |
|---|---|---|
| Warmup | 10 min | 1-2 logic puzzles for warmup, not study |
| Vocab | 15 min | Reflex pass on key terms (<2s/term) |
| Drill | 25 min | Hand-draw 1 architecture sketch + hand-write 1 pseudo-code skeleton |
| Buffer | 10 min | Decompress, eat, travel to D3 for 3pm |

**Hard rule:** No new content after Wednesday morning. Confidence consolidation only.

---

## Topic Notes Index

**All topic-note files in this folder are SCAFFOLDS for John's hand notes**, except `logic-puzzles.md` and `mock-test.md` which are DRILL BANKS with full content. Lesson content lives in [../lesson-tracker.md](../lesson-tracker.md).

| Tier | File | Type | Topic |
|---|---|---|---|
| S | `ai-engineering-foundations.md` | Scaffold | LLM app patterns — prompt engineering, streaming, structured outputs, error handling, cost, eval |
| S | `agents-and-tool-use.md` | Scaffold | ReAct, plan-and-execute, function calling, MCP, multi-agent, HITL, security |
| S | `rag-deep.md` | Scaffold | Full RAG pipeline — chunking, embeddings, vector store, retrieval, rerank, eval (RAGAS) |
| S | `logic-puzzles.md` | **Drill bank** | 18-puzzle bank across 10 categories. Drilled 6/day Mon + Tue |
| S | `mock-test.md` | **Drill bank** | Mock #1 (Tue) + Mock #2 (Wed) with answer keys |
| A | `multi-agent-governance-light.md` | Scaffold | Concept-level — HITL, role boundaries, audit trails, escalation |
| A | `prompt-safety-essentials.md` | Scaffold | 4 concepts: prompt injection, jailbreak/system prompt leakage, output validation, defense-in-depth |
| B | `mongodb-essentials.md` | Scaffold | High-level NoSQL primer — Mongo vocab + when NoSQL vs SQL |
| B | `system-integration-llm.md` | Scaffold | Reference architecture (leverages existing `02-system-design/` notes) |

**Reuse — no new file needed:**
- [`../../remitly/study-plan/react-js-ts.md`](../../remitly/study-plan/react-js-ts.md) — React.memo, useState, hooks (re-read if React MCQ appears)
- [`../../../02-system-design/notes/07-load-balancing-and-networking.md`](../../../02-system-design/notes/07-load-balancing-and-networking.md) — API gateway, rate limiting
- [`../../../02-system-design/notes/12-observability.md`](../../../02-system-design/notes/12-observability.md) — logs/metrics/traces, golden signals
- [`../../../03-ai-foundations/notes/01-embeddings-and-vector-concepts.md`](../../../03-ai-foundations/notes/01-embeddings-and-vector-concepts.md) — embeddings + cosine similarity

---

## Logic Puzzle Daily Habit

Goal: **18-24 puzzles across the cram** = ~2 reps per pattern category.

10 categories to drill across:
1. Weighing / scales (binary or ternary encoding)
2. Harmonic mean / work rate (NOT arithmetic mean when distance/work is fixed)
3. Bridge crossing (pair slows, shuttle fasts)
4. Knights / knaves (meta-question framing)
5. Probability counter-intuitive (Monty Hall, birthday paradox)
6. Pigeonhole / counting (worst case fills slots first)
7. Hat / prisoner (parity / signaling)
8. Sequence / pattern recognition (sub-sequences before global rule)
9. Geometry / volume (trick observations)
10. Clock / time (hands move at fixed relative speed)

Rule: cold attempt first (max 5 min). If stuck, look up the trick, then re-attempt cold next session. Track wins/misses per category in `logic-puzzles.md`.

---

## Recovery Rule

If something asked on the test isn't covered: **honest framing**, then reason from first principles using related concepts. Don't bluff. Multi-select: when unsure, eliminate clearly wrong options first; mark the remaining best-guesses; move on, return if time.

---

## Files in This Directory

- `README.md` — this file (cram schedule + index)
- `interview-format.md` — D3 written-test format intel (email + Glassdoor)
- *(Topic notes added as cram progresses)*
