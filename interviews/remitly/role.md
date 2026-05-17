# Remitly — Role

The specific role for this interview is not yet confirmed, but **John has identified 3 SDE II postings he'd qualify for** — all based in **Burnaby, BC, Canada**, all $124K+ CAD base. These three are the realistic target landscape. The recruiter intro chat on 2026-05-20 will likely cover which of the three is the best fit.

**Important honest recalibration (vs. earlier research):** these are *not* the "AI Native Software Engineer" or "Knowledge Development Engineer" roles. Those are aspirational Seattle-based roles that don't match what John has applied for. The AI narrative is still relevant for "why Remitly" (Q1 2026 AI-driven efficiency story, the new CEO's AI-first thesis) but **not as the role-fit hook**.

---

## Target Role 1 — SDE II, Home and Explore (Frontend) — **Strongest stack fit**

- **URL:** https://careers.remitly.com/job/23015992/software-development-engineer-ii/
- **Location:** Burnaby, BC, Canada (3 days/week in-office)
- **Salary:** $124,000 – $139,500 CAD base
- **Team:** Home and Explore (within Engineering)
- **What the team owns:** "A cohesive, personalized Home experience that makes sending money effortless" — scalable Home architecture, intelligent personalization, targeted experiences for new and growing customer segments. Frontend, millions of users.
- **Tech stack (verbatim):** **React, TypeScript, JavaScript, CSS, component-based architecture.** Frontend architecture, state management, API integration, testing, CI/CD, observability.
- **AI mention:** "Leverage modern AI-powered development tools (e.g., code assistants, automated testing, intelligent debugging, documentation generation)" — Copilot-style developer productivity, not the AI-Native engineer family.
- **Required experience:**
  - 5+ years building features for millions of users
  - 2+ years frontend feature development with engineers, PMs, designers
  - Leadership experience on projects / large features
- **Why this is the strongest stack fit:** Directly maps to John's strongest area — 3 years working with TypeScript/React/Next.js. Day-to-day work is what he already does.
- **Honest gap:** **The 5+ years requirement vs. John's ~3 years total** is real. Framing in the interview: emphasize **depth of work and ownership** over raw years. The "2+ years frontend" sub-requirement he likely clears.

## Target Role 2 — SDE II, Customer Data Platform (Backend / Data Platform)

- **URL:** https://careers.remitly.com/job/23212618/software-development-engineer-ii-sde2-customer-data-platform/
- **Location:** Burnaby, BC, Canada (3 days/week in-office)
- **Salary:** $124,000 – $155,000 CAD base
- **Team:** Customer Data Platform, within the **Identity & Trust** org
- **What the team owns:** "Builds and operates the systems that manage customer data at scale" on AWS. "High-throughput, high-availability services that are critical to Remitly's products and regulatory obligations."
- **Tech stack (verbatim):** **AWS, DynamoDB**, relational databases (unspecified), distributed systems. No programming languages named explicitly in the JD (likely **Go and/or Java** based on Remitly's broader stack pattern).
- **AI mention:** None.
- **Required experience:**
  - DynamoDB / large-scale NoSQL data stores
  - Distributed systems development
  - Multi-tenant or platform-oriented service design
  - Observability and operational best practices
  - Mentoring interns or new hires
  - **No explicit years-of-experience minimum stated**
- **Why this could work:** No years floor → John's ~3 years is not an explicit blocker. Identity & Trust org is mission-critical work.
- **Honest gap:** Backend / data platform / distributed systems / DynamoDB are John's **weakest profile areas**. From his roadmap CLAUDE.md: "Surface-level Postgres knowledge. Needs solid SQL query writing, indexing strategy, schema design." DynamoDB is new ground. He can be honest in the chat: surface familiarity with relational, eager to grow into distributed systems work.

## Target Role 3 — SDE II, WARP (Wallet Product Risk)

- **URL:** https://careers.remitly.com/job/23310276/software-developer-engineer-ii-warp/
- **Location:** Burnaby, BC, Canada (3 days/week in-office)
- **Salary:** $124,000 – $155,000 CAD base
- **Team:** Wallet Product Risk ("WARP" — likely stands for Wallet And Risk Platform or similar; not spelled out in JD)
- **What the team owns:** "Risk management controls—such as fraud prevention features—while delivering an industry-leading customer experience for our wallet and wallet adjacent products." Mission-critical fraud controls across multiple platforms.
- **Tech stack (verbatim):** **Go, Java/Kotlin, TypeScript, React Native, AWS, message brokers** (likely Kafka or Kinesis), various database technologies, testing frameworks, CI/CD, observability.
- **AI mention:** None.
- **Required experience:**
  - 4+ years production-grade code
  - Strong background in modern distributed system architecture
  - Cloud platforms, message brokers, database technologies
  - On-call rotation
- **Why this could work:** Polyglot stack — John has the TS side, learns the Go/Java side on the job. Fraud/risk is one of the most engineering-rich domains in fintech.
- **Honest gap:** 4+ years vs. John's ~3 years (closer than Role 1's 5+ gap). Go is new ground. Distributed systems / message brokers — light from roadmap so far.

---

## Confirmed Role (fill in once recruiter shares it)

- **Title:** TODO
- **JD (verbatim):** TODO — paste once recruiter confirms which role is being interviewed for.

---

## Stack Cross-Reference vs. John's Roadmap

| Stack item | John's coverage | Where in roadmap | Notes |
|------------|-----------------|-------------------|-------|
| **TypeScript / React / JS / CSS** | Strong (3 yrs) | [`06-frontend/CLAUDE.md`](../../06-frontend/CLAUDE.md) | Bread-and-butter. Role 1 = direct match. |
| **Go** | None | Not in roadmap | Don't try to cram. Frame as learnable. |
| **Java / Kotlin** | None | Not in roadmap | Same — frame as learnable. |
| **React Native** | None (web React only) | Not in roadmap | If asked: native React translates well. |
| **AWS** | Surface | [`07-devops/CLAUDE.md`](../../07-devops/CLAUDE.md) | Roles 2 + 3 use it heavily. |
| **Docker / K8s** | Some Docker Compose | [`07-devops/CLAUDE.md`](../../07-devops/CLAUDE.md) | Light coverage. |
| **DynamoDB** | None | Not in roadmap | Role 2 specific. Surface knowledge OK. |
| **Distributed systems** | Light vocabulary | [`02-system-design/CLAUDE.md`](../../02-system-design/CLAUDE.md) | Idempotency LOCKED, vocab in place. |
| **Message brokers (Kafka/Kinesis)** | Vocabulary only | [`02-system-design/CLAUDE.md`](../../02-system-design/CLAUDE.md) | Surface for Role 3. |
| **Python + AI/LLM integration** | Strong (current job) | n/a — workplace | Not directly in any of these 3 JDs, but reinforces the broader "why Remitly" narrative. |

---

## Gap Inventory (vs. the 3 target roles)

| Gap | Role(s) affected | Severity | Cram-able in 3 days? |
|-----|------------------|----------|----------------------|
| **Years of experience** (3 vs. 4-5+ required) | All three | Real | No — frame around depth of ownership instead |
| **Go** | Role 3 | Medium | No — frame as learnable (TS/Python transferable) |
| **Java / Kotlin** | Role 3 | Medium | No — frame as learnable |
| **React Native** | Role 3 | Low | No — translates from web React if asked |
| **AWS depth** | Roles 2, 3 | Real | Surface-only review — name services in the relevant family |
| **DynamoDB / NoSQL data modeling** | Role 2 | Real | Surface vocabulary only |
| **Distributed systems** (real depth) | Roles 2, 3 | Real | Vocabulary already exists — don't try to drill new |
| **Message brokers (Kafka / Kinesis)** | Role 3 | Medium | Vocabulary review only |
| **Payments / fraud / risk domain primer** | Role 3 (and broadly fintech) | Medium | YES — high-yield 30 min cram |
| **Frontend perf depth** (memoization, virtualized lists, bundle analysis) | Role 1 | Low-Medium | YES — high-yield 30 min cram |

**What John already has strong:** TS/React/JS/CSS at scale (Role 1 stack), idempotency LOCKED from system design review, surface system-design vocabulary (caching, rate limiting, circuit breakers, replicas), Python + AI/LLM integration experience (no JD names it but it's a differentiator at his cohort level).

---

## Must Speak Intelligently On

Non-negotiable concepts for the intro chat. These are things John must **understand** to engage credibly — distinct from talking points (lines to say in the room — those live in [talking-points.md](talking-points.md)).

### Core 5 (every conversation)

1. **The 4-pillar product evolution (Send / Spend / Save / Borrow).**
   *Why this matters:* If John can't articulate that Remitly is no longer just a transfer app in 2026, he hasn't done the homework. Anchors the elevator pitch and "why Remitly."

2. **The Q1 2026 AI-driven efficiency narrative.**
   *Why this matters:* It's THE strategic story of Remitly in 2026 — margin expansion attributed to AI in product + ops, not pricing. If asked "what stood out to you?", this is the answer. Also opens the door to talking about John's own LLM-integration experience as relevant.

3. **The years-gap framing — depth over years.**
   *Why this matters:* All 3 roles ask 4-5+ years; John has ~3. The recruiter screen evaluates whether he can credibly step up. Have a one-line framing ready: "I'm three years in, but the work I've done — especially the LLM integration on the production side — is where most folks 3 years in haven't gotten yet."

4. **Idempotency in payments / multi-leg transfers.**
   *Why this matters:* Fintech-101. Whether the recruiter asks technically or not, John should be able to explain in 30 sec why retries matter, what breaks without idempotency keys, and why it's harder when the transfer touches multiple corridors. He has this LOCKED from system design review — make sure it surfaces under pressure.

5. **The "3 roles" landscape and which one interests John most + why.**
   *Why this matters:* Recruiter WILL ask. Honest answer: "Home and Explore is closest to what I do today; CDP is the stretch on backend depth; WARP / wallet risk is where I'd most love to grow into because fraud/risk is one of the most engineering-rich problems in fintech." Lock this line.

### Role-contingent (drill the one that matches the actual role)

6. **Fraud controls at a fintech** (Role 3 contingent).
   *Why this matters:* If the recruiter steers toward WARP, John should be able to talk about: rules-based vs. ML-based detection, why latency matters (a 500ms fraud check blocks the user's transfer experience), idempotency on writes (don't double-block, don't double-allow), false-positive vs. false-negative trade-offs.

7. **Frontend performance at scale on low-bandwidth markets** (Role 1 contingent).
   *Why this matters:* Remitly's customer base is global immigrants — many on Android, many in low-bandwidth regions. The Home and Explore mandate is "millions of users" — fluency on bundle size, code splitting, accessibility, perceived performance matters.

---

## Cram Priority

Ordered by impact for the intro chat. Top 3 are non-negotiable; #4-6 are optional if time allows.

1. **Memorize the elevator pitch + "why Remitly" answer.**
   *Why first:* These are the two most likely things to come out of John's mouth in the first 5 min. If they're sharp, the rest of the call coasts. If they're not, recovery is hard. (Source: [talking-points.md](talking-points.md))

2. **Drill the "3 roles fluency" line out loud.**
   *Why:* Recruiter will ask. Don't compose it on the spot. Practice the "strongest on X, would stretch into Y, would love to grow into Z" framing until it's natural.

3. **Internalize the years-gap framing.**
   *Why:* It WILL come up implicitly even if the recruiter doesn't explicitly name it. Lead with depth-of-work + Python/AI integration as differentiators. Don't apologize for the years.

4. **(Optional, ~30 min) Payments domain primer.**
   *Why:* Reinforces Must-Know #4 (idempotency) and adds context: FX rate locking, atomicity across multi-leg transfers, settlement vs. disbursement, compliance/AML basics. Most impactful for Role 3 conversation.

5. **(Optional, ~20 min) DynamoDB single-table design vocabulary.**
   *Why:* For Role 2 fluency. Just enough vocab to engage if the recruiter mentions CDP — know what "partition key," "sort key," and "single-table design" mean. Don't try to learn the depth.

6. **(Optional, ~20 min) Frontend perf vocabulary review.**
   *Why:* For Role 1 fluency. React.memo / useMemo / useCallback / virtualized lists / code splitting / bundle analysis — at the level of "I know what each does and roughly when to use it."

**Skip entirely for this round:** Go syntax, Java/Kotlin, deep distributed systems, Kafka internals. Wrong battle for a 30-min recruiter screen.

---

## Seniority Signals

- All three roles are **SDE II** (mid-level).
- Required experience: **5+ yrs (Role 1), unspecified (Role 2), 4+ yrs (Role 3)**.
- John's **~3 yrs total** is the realistic gap. **Not a disqualifier for an intro chat** — recruiters routinely talk to candidates 1-2 years short of stated minimums when other signals are strong. The intro chat is to evaluate whether John can credibly step up.
- Framing in the chat: lead with **breadth of work and ownership**, not years. The Python + AI integration experience is differentiated for his cohort — most people 3 yrs in haven't shipped production LLM features.

---

## Why These Roles Fit John (draft pitch — refine in [talking-points.md](talking-points.md))

> "All three roles are Burnaby SDE II positions, and they cover different sides of my profile. Home and Explore is the closest match to where I already work — TypeScript and React on a high-traffic surface — and that's where I've shipped the most over the past three years. The Customer Data Platform role would be a stretch on backend depth, but it's the kind of work I'm pointed at growing into. And the Wallet Product Risk team is interesting because fraud / risk systems are one of the most engineering-rich problems in fintech — that's the side I'd be most excited to grow into."

(Refine over the next two sessions in [talking-points.md](talking-points.md) Part 2.)
