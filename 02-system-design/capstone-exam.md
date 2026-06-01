# Section 2 — End-of-Section Capstone Exam

**Date attempted:** *(TBD — populated when John calls "ready for Capstone")*
**Status:** Not yet attempted
**Format locked:** 2026-06-01

This file is the single tracking artifact for the entire Capstone exam. All three parts logged here. Pass/fail decision at the bottom.

---

## Format (locked 2026-06-01)

Three-part exam in one session, ~90-120 min total. John's preferences captured below.

### Part 1 — Written Quiz (~25-35 min)

- **John's preference:** decently heavy + dense — uses it to warm his brain up for the cold case study.
- **Format:** ~15 questions, mix of:
  - **~6-7 multiple choice** (quick recall, brain warmup, low-stakes lock-in).
  - **~6-7 short-answer written** (explain-why, trade-off reasoning, definition+implications).
  - **~2-3 applied written scenarios** (small design vignettes — 1 paragraph response each).
- Drawn primarily from existing [interview-questions.md](./interview-questions.md) bank with 3-5 fresh questions to prevent pure pattern-matching.
- John types answers directly under each question in this file.
- Claude grades all questions after John submits (not question-by-question).
- **Pass:** ≥70% overall AND no catastrophic miss on core topics (CAP, caching, DB scaling, load balancing).

### Part 2 — Cold Case Study (~45-60 min)

- **John's preference:** interview-style, oral. Mix of handwritten notes (paper) + speaking. John drives most of the design himself; Claude plays the interviewer — clarifying questions, probing, hole-poking.
- **Prompt:** fresh system John hasn't designed. NOT any of: URL shortener, real-time chat, rate limiter, social feed, notifications. Claude picks from menu: Twitter feed, Uber dispatch, Dropbox/file sync, Tinder/dating swipe, ride-sharing, ticketing (à la Ticketmaster).
- **Flow:**
  - Claude states the prompt + initial constraints.
  - John asks clarifying questions (oral). Claude answers in interviewer voice (some answers, some punts).
  - John designs verbally + on paper. Walks through Requirements → Estimation → API → Architecture → Live-flow walkthrough at his own pace.
  - Claude probes throughout — interviewer-style ("why X not Y?", "what breaks first?", "walk me through what happens when…").
  - Claude takes notes in this file as we go — key decisions + load-bearing critiques. NOT a full transcript; just enough to grade and feed forward.
- **Pass:** No major conceptual errors. Trade-offs articulated. Live-message-flow walkthrough produced under pressure (this was a CS #2 gap — must surface here).

### Part 3 — Rapid-Fire Defense (~10-15 min)

- **John's preference:** oral.
- **Format:** Claude asks 5-7 follow-up questions on John's Part 2 design. Interview-style follow-ups: "why X?", "what about Y failure mode?", "scale this 10x — what changes?", "what's your p99 SLA and how do you know?". John responds verbally. Claude tracks question + per-Q grade in this file.
- **Pass:** ≥4/7 answered confidently.

### Overall Pass Criteria

ALL THREE parts must pass for the section to close. Failing any single part → targeted re-teach + retry of that part only (not the whole Capstone). The gate exists to surface real gaps, not to be one-shot pass-or-fail.

---

## Part 1 — Written Quiz

*(populated when Capstone begins — Claude generates questions, John types answers under each)*

### Questions

### Grading

*(populated after John submits)*

---

## Part 2 — Cold Case Study

*(populated when Capstone begins)*

### Prompt

### Clarifying questions + interviewer answers

### Live notes — key decisions + Claude's critiques

### Final grade + summary

*(populated after Part 2 wraps)*

---

## Part 3 — Rapid-Fire Defense

*(populated during Part 3)*

### Questions + per-Q grade

### Final grade

*(populated after Part 3 wraps)*

---

## Overall Result

**Pass/Fail per part:**
- Part 1: *(TBD)*
- Part 2: *(TBD)*
- Part 3: *(TBD)*

**Section close decision:** *(TBD — pass all three → Section 2 closes; fail any → targeted re-teach + retry that part)*

**Summary of strongest topics:** *(TBD)*

**Carry-forward gaps (logged to section CLAUDE.md Surfaced Gaps):** *(TBD)*
