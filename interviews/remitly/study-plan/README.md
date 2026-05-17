# Remitly — Study Plan

**For JD analysis (tech stack, coverage, gap inventory, must-knows, cram priorities), see [../role.md](../role.md).** This file is the **day-by-day cram schedule** + topic-notes index.

---

## Days Remaining

**3 days** (today: 2026-05-17, interview: 2026-05-20)

Update each session.

---

## Context (recap)

3 target SDE II roles in Burnaby, BC — all $124K+ CAD base:

1. **Home and Explore** (frontend) — React/TS/CSS at scale. 5+ yrs required (gap).
2. **Customer Data Platform** (backend) — AWS/DynamoDB/distributed systems. No yrs floor.
3. **WARP / Wallet Product Risk** (polyglot) — Go/Java/Kotlin/TS/React Native/AWS/message brokers. 4+ yrs required (smaller gap).

Full JD analysis (stack, coverage table, gap inventory, must-knows, cram priorities) → [../role.md](../role.md).

---

## Day-by-Day Cram Plan

The intro chat on 2026-05-20 is **conversational, not technical**. Focus is company knowledge + behavioral + role fit. Skip deep tech drilling — that's for the technical phone screen.

### 2026-05-17 (today, done) — Research & scaffolding
- ✓ Directory + seed files created.
- ✓ Deep web research on Remitly 2026 (company, eng signals, careers, interview format).
- ✓ Analyzed 3 target SDE II JDs verbatim.
- ✓ Filled `talking-points.md` Part 1 (company side).
- ✓ Filled `role.md` with all 3 target roles + stack cross-reference.

### 2026-05-18 — Behavioral prep (~90 min)
Primary: fill `talking-points.md` Part 2.
1. **"Tell me about yourself"** — draft 60-90 sec pitch. Frame: current role → what John does day-to-day → deliberate transition into full-stack + AI engineering → why now. Lead with the AI-integration experience.
2. **"Why Remitly"** — draft. Hook to: immigrant-customer mission, the AI-first operating model under new CEO, fintech with a real engineering moat. Have a 30-sec version and a 60-sec version.
3. **"Why are you leaving / looking?"** — draft. Honest, forward-looking. No bashing.
4. **3 STAR stories** (pick the strongest 3 first; do the 4th if time):
   - Story 1 (theme: **LLM integration / AI engineering judgment**) — real story from John's current role
   - Story 2 (theme: **full-stack ownership / TS+React delivery**) — bread-and-butter
   - Story 3 (theme: **failure / learning-from-mistake**) — mid-level interviewers love this
5. **"Three roles" line** — draft the "I'm strongest on X, would stretch into Y, would love to grow into Z" line for when the recruiter asks which role interests him most.

### 2026-05-19 — Dry-run + close gaps (~60 min)
1. Read `talking-points.md` cold and **say each section out loud**. Anywhere it doesn't flow, rewrite.
2. **Payments domain 30-min primer** — read up on: idempotency in payments (you already know it), FX rate locking, atomicity across multi-leg transfers, compliance/AML basics, settlement vs. disbursement. Optional but high-yield for Role 3 conversation.
3. **Memorize the 5 talking points + the 5 questions to ask them** — at least the headlines. Don't need to recite verbatim; need to be able to drop them into the flow naturally.
4. **Day-of logistics check** — confirm time zone (Pacific?), format (Zoom/Google Meet/phone?), interviewer name, calendar invite, clean shirt, working camera, working mic.

### 2026-05-20 — Interview day
**Light review only.** No new material. 15 min before: re-read elevator pitch + "why Remitly" + the 5 talking points headlines. Then close the laptop, breathe, show up.

---

## Roadmap Cross-Reference (for context — not needed for the intro chat)

If a second/third round is offered, drill from these:

- [`02-system-design/CLAUDE.md`](../../../02-system-design/CLAUDE.md) — payments-flavored topics: idempotency (LOCKED), rate limiting, caching, circuit breakers, replicas.
- [`06-frontend/CLAUDE.md`](../../../06-frontend/CLAUDE.md) — if Role 1 advances, React performance, memoization, virtualized lists, bundle analysis.
- [`07-devops/CLAUDE.md`](../../../07-devops/CLAUDE.md) — AWS / Docker / K8s vocabulary.
- [`01-algorithms/CLAUDE.md`](../../../01-algorithms/CLAUDE.md) — for the technical phone screen if it's coding-flavored. Continue regular algo warmups during the cycle.

---

## Files in This Directory

- `README.md` — this file (cram plan + gap inventory).
- [interview-format.md](interview-format.md) — what to expect from the Remitly interview loop overall (not just this round).
- *(Topic notes added as the role demands — e.g. `payments-domain-primer.md` if we draft one on 2026-05-19.)*
- *(Uploaded materials — recruiter PDFs, JD docs, public talks — dropped here as received.)*
