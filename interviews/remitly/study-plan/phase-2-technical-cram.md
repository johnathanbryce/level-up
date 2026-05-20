# Phase 2 — Technical Cram

**Status:** ACTIVE — recruiter screen passed 2026-05-20 with positive signal. Awaiting hiring manager decision on advance. Cram begins now in parallel — if HM declines, we shelve; if HM advances, we're ahead.

---

## Interview Process (per Remitly recruiter on 2026-05-20)

1. **T1 — Tech Screen** (live coding, ~1 hour)
   - LeetCode-flavored challenge. Reach a working solution.
   - **Build test cases for the solution** (stated requirement, not "if there's time").
   - 1-2 behavioral / situational questions (STAR framing).
2. **15-min prep call** before the loop.
3. **4-round onsite loop:**
   - System design
   - General coding
   - Hiring manager interview
   - Frontend OR product (interactions with PMs / business stakeholders)

### Independent verification (web research 2026-05-20)

Sources confirm the live-coding emphasis and add useful texture:

- **Time-constrained DSA problems** with emphasis on explaining approach + trade-offs out loud.
- **Clean code + complexity analysis** weighted highly.
- One reported sample question: *"Given a set of bank accounts with dollar amounts and a threshold, find the number of transfers needed to get all accounts to meet the threshold. Watch edge cases."* → financial-flavored, edge-case-heavy. Remitly clearly leans toward problems thematically related to their domain.
- Onsite is **2 coding + 1 system design** per multiple sources, which aligns with what the recruiter outlined (modulo HM + frontend/product round on top).

---

## Current Focus — T1 Tech Screen prep

Highest priority right now: **LeetCode reps in Python (60%) and JS (40%)**, aligned to:

- Reach working solution within ~30-40 min.
- **Always write test cases at the end.** Not optional in Remitly's format.
- Talk through reasoning out loud (rehearse this — most candidates skip it).
- State time + space complexity explicitly when done.

### Pattern Priorities (from [../../../01-algorithms/CLAUDE.md](../../../01-algorithms/CLAUDE.md))

**MOSTLY LOCKED / LOCKED — drill for fluency, don't re-teach:**
- Hash-map-complement (Two Sum family)
- Frequency counting (count-then-inspect)
- Stack (recently introduced)

**TO INTRODUCE / EXTEND in Phase 2:**
- Running-state / single-pass (Best Time to Buy and Sell Stock-flavored)
- Two-pointer (same direction — bookmarked from Phase 1)
- Sliding window
- Binary search
- Tree traversal (BFS / DFS)
- Linked lists (basic ops + cycle detection)

**DEFERRED unless signals point that way:**
- Dynamic programming
- Graph algorithms (Dijkstra, topological sort)
- Heap / priority queue
- Backtracking

### Why Python-first this cycle

1. Remitly uses Python in backend services (per role JDs and broader stack research).
2. John's #1 skill-to-rebuild per main CLAUDE.md.
3. Python is well-suited to the "clean code under time pressure" framing — list comprehensions, built-in collections, dict/set operations are interview-fast.

---

## Role + Stack (still TBD)

- **Role:** TBD — hiring manager call will clarify which of the 3 target SDE II roles.
- **Interview dates:** TBD
- **Format per round:** see Interview Process above
- **Interviewer(s):** TBD

The 3 roles in scope (full JD analysis in [../role.md](../role.md)):
- Role 1 — Home and Explore (Frontend, React/TS/CSS)
- Role 2 — Customer Data Platform (Backend, AWS/DynamoDB)
- Role 3 — WARP / Wallet Product Risk (Polyglot, Go/Java/Kotlin/TS, fraud/risk)

---

## Drill Priorities (ordered)

1. **LeetCode reps daily** — patterns above. Build test cases as part of every solution.
2. **STAR story drafts** — T1 includes 1-2 behavioral. Have 4 ready:
   - **Scope-jump:** Caseway CTO + dev left same week, John promoted, no handover.
   - **AI integration / RAG:** the public search engine ship — full-stack, rate limiting, BM25.
   - **Failure / learning:** TODO — John to pick.
   - **Cross-functional:** working with PMs / stakeholders — TODO.
3. **System design fundamentals refresh** — pull from [../../../02-system-design/CLAUDE.md](../../../02-system-design/CLAUDE.md). Drill: request lifecycle, caching, rate limiting, DB scaling, idempotency (LOCKED). Refresh weak spots flagged in main CLAUDE.md current state.
4. **Behavioral fluency** — "Why are you leaving?" canonical answer never drilled in Phase 1. Worth a 10-min pass.
5. **Role-specific cram** — activates when HM clarifies which role.

---

## Anticipated Topic Notes (created as role direction firms up)

**If Role 1 (Home and Explore — frontend):**
- `react-performance-deep.md` — memoization, virtualized lists, code splitting, profiling
- `typescript-advanced.md` — generics, discriminated unions, conditional types
- `frontend-perf-at-scale.md` — bundle analysis, lazy loading, low-bandwidth markets, accessibility

**If Role 2 (CDP — backend):**
- `distributed-systems-deep.md` — CAP, consistency models, replication, partitioning
- `dynamodb-deep.md` — single-table design, GSIs, access patterns, hot partitions
- `aws-deep.md` — IAM, VPC, Lambda, the services you'd actually touch

**If Role 3 (WARP — fraud/risk):**
- `fraud-systems.md` — rules vs ML, latency budgets, false positive/negative trade-offs
- `message-brokers-deep.md` — Kafka partitions, ordering, exactly-once delivery
- `payments-flows-deep.md` — multi-leg transfers, saga pattern, reversal patterns, state machines (the Phase 1 `payments-domain.md` trim removed FX locking + multi-leg + AML/KYC content — git history will recover if needed)

---

## LeetCode Session Format

For each session:

1. **Pick problem** aligned with current pattern priority + (when possible) financial/transfer theme to match Remitly's style.
2. **~25-30 min solo** (timed). Talk through approach out loud as warmup for live-format delivery.
3. **After solution: write test cases.** Edge cases, large inputs, empty inputs, single-element. *This is the stated Remitly requirement — don't skip.*
4. **State complexity** explicitly (time + space).
5. **~5-10 min review with Claude** — clean code, naming, complexity analysis, alternative approaches.
6. **Log in [../../../01-algorithms/CLAUDE.md](../../../01-algorithms/CLAUDE.md)** with problem, pattern, result, and notes.

---

## Day-by-Day Schedule (build out as HM confirms timing)

For now: **one LC problem per session**, plus STAR story drafting as a side track. When HM call lands, add system design + role-specific drilling.
