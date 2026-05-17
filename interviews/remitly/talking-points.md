# Remitly — Talking Points

Everything John will *say in the room*. Top half (Part 1): what I know about them — **filled from 2026-05-17 deep research**. Bottom half (Part 2): what I'll say about myself — **TODO, drafted next session 2026-05-18**.

---

## Part 1 — Company (what I know about them)

### Elevator Pitch (2-3 sentences)

> "Remitly is a Seattle-based digital cross-border remittance company — public on NASDAQ as RELY, around 9.6 million quarterly active customers, moving money to 170+ countries. They've spent the last year repositioning from a single-product transfer app into a four-pillar financial partner for immigrants — Send, Spend, Save, and Borrow — through Remitly One, the new wallet, card, Flex cash advance, and a credit-building product launching Spring 2026. And they just brought in a new CEO from Santander's Openbank specifically to lean into AI-first operations."

### Mission & Products

- **Mission (as stated):** "Transform the lives of immigrants and their families by providing the most trusted financial services products on the planet."
- **Core product surface in 2026:**
  - **Send** — original cross-border money transfer (mobile + web app), 170+ countries
  - **Remitly One** — $9.99/mo membership tier (launched at Remitly Reimagine event, mid-2025)
  - **Remitly Wallet** — multi-currency, locked FX rates, 4% USD-balance boost for members, USDC stablecoin support
  - **Remitly Card** — digital debit card, no FX fees
  - **Remitly Flex** — cash advance / send-now-pay-later up to $250, no interest
  - **Remitly Business** — SMB cross-border payments. US Q2 2025 launch, UK live, **Canada GA May 2026**. 20,000+ businesses on the platform. New features (May 2026): Bulk Payments, Send-by-Link.
  - **Credit-building product** — coming Spring 2026, money transfers reported to credit bureaus

### Recent News / Strategic Moves (2025-2026)

- **CEO change (Feb 19, 2026):** Co-founder Matt Oppenheimer stepped down after ~15 years; transitioned to Chairman. **Sebastian Gunningham** is the new CEO — formerly Chairman of Santander Consumer Finance, VC of Openbank (Santander's digital/AI-native arm), 10+ year Amazon S-team SVP who led marketplace, payments, and search.
- **Q1 2026 record quarter (May 6, 2026):** Revenue $452.8M (+25% YoY), send volume $22.1B (+37% YoY), active customers 9.6M (+20% YoY), net income $49.1M (+332% YoY), adjusted EBITDA $101.6M (+74% YoY, 22% margin). Full-year 2026 guidance raised to $1.96–1.98B. **Margin expansion publicly attributed to "AI-driven efficiency."**
- **Matt Oppenheimer's July 2025 AI letter:** "*Transforming Remitly with AI*" — framed AI as a generational shift comparable to internet/mobile, declared it "no longer optional, it's essential."
- **AI-Native engineer job family launched:** New role types — *AI Native Software Engineer*, *Senior AI Native SWE (Autonomous Systems)*, *Knowledge Development Engineer* — engineers whose production code is "near-100% agent-generated."
- **AI support assistant in production:** Resolves 74%+ of issues at first contact, only 3% escalate to humans, cuts handle time 75%, EN/ES/FR.
- **ML fraud detection:** Scores tens of thousands of transactions/hour, reported 25% drop in fraud-intervention rate, 30% drop in transaction loss rate.

### Engineering / Tech Signals

- Engineering blog ([medium.com/remitly](https://medium.com/remitly)) is **low-volume** — they don't publish like Stripe/Uber engineering blogs. Don't lean on the blog as a talking point.
- Tech stack from JDs: **Go primary backend + Java/Kotlin/Python + TypeScript/React frontend + Python/PyTorch for ML, on AWS with Docker/K8s.** Heavy 2026 investment in agentic coding workflows internally (the AI-Native engineer family).
- ML in-house since 2017 — fraud detection is mature, not a recent bolt-on.
- Public ML/AI write-ups by Robin McFee (Director of Engineering) and Mike Foster (VP Product) on the newsroom.

### Specific Things to Bring Up (in priority order — calibrated to the 3 target SDE II roles)

1. **Q1 2026 EBITDA expansion attributed to AI-driven operational leverage.** *"What stood out in the Q1 earnings call was that the margin jump wasn't from pricing — it was attributed to AI-driven internal efficiency. That's a real engineering moat if you can build it. Most fintechs talk about AI in support; doing it across product and ops is the harder version, and it's what got me reading more about how Remitly's engineering org operates."*

2. **(If asked about Wallet / WARP role)** **Remitly Business + Bulk Payments mapping to backend payments + risk engineering.** *"The Bulk Payments and Send-by-Link launch this month is interesting — the engineering problem under Bulk Payments is non-trivial: atomicity across N international transfers, partial-failure handling, idempotency on retries. And on the wallet side, the fraud/risk problem space is one of the most engineering-rich domains in fintech — it's the kind of work I'd be excited to grow into."*

3. **(If asked about Home and Explore role)** **Personalization at scale on a high-trust surface.** *"The Home and Explore mandate — 'cohesive, personalized Home experience for millions of users' — that's the kind of frontend work where the bar isn't just 'does it render' but 'does it render fast enough on a slow Android device in a low-bandwidth market.' That's the frontend engineering challenge I'd want to take on, and it maps directly to what I've been doing for three years at my current role."*

4. **(If asked about CDP role)** **Customer Data Platform → regulatory obligations as engineering constraint.** *"The CDP JD calls out 'high-throughput, high-availability services critical to Remitly's regulatory obligations.' That's the part that interests me — designing data systems where compliance isn't a layer you bolt on, it's the constraint that shapes the architecture from day one."*

5. **The 9.6M-to-300M-addressable-market gap.** *"Remitly hit 9.6M quarterly active customers and is positioning toward the 300M+ cross-border worker market with Wallet, Card, Flex, and the credit product. The interesting engineering challenge isn't scaling transfers — it's layering Save / Spend / Borrow on top of an existing high-trust, regulated transfer platform without breaking core compliance guarantees."*

6. **Gunningham's Santander/Openbank background (use sparingly — 1 of the above 5 is enough).** *"Bringing in a CEO from Openbank — Santander's digital/AI-native arm — and before that Amazon, feels like a deliberate move past 'remittance app' toward 'full digital financial services with an AI-first operating model.' That's the trajectory I'd want to join."*

### Open Questions to Ask THEM (in priority order)

1. **(Product/strategy)** *"Remitly One launched at Reimagine last year and you've got the credit-building product coming in Spring 2026. From an engineering perspective, what's been harder — building the new product surfaces, or refactoring the original transfer engine to support a much broader product set without compromising compliance?"*

2. **(Engineering culture / tech decisions)** *"I saw the senior SWE postings call out Go on AWS for backend services. Was that always the case, or was there a deliberate migration from Java? How does the team make language-and-platform decisions when there's a mix of Go, Kotlin, Java, and Python across services?"*

3. **(AI/ML direction)** *"Matt's AI letter from last July called AI a generational shift, and the AI-Native Engineer roles are essentially saying production code should be near-100% agent-generated. How is the team measuring whether that workflow is working — code quality, throughput, time-to-prod? And where has it not worked as expected?"*

4. **(Role-specific)** *"For the role I'm interviewing for, what does the first 90 days look like for someone who's strong on full-stack TypeScript/React and growing on the Python and agentic-AI side? Where do new hires usually find the biggest ramp-up curve at Remitly specifically?"*

5. **(Team/onboarding)** *"Remitly has 2,700+ employees across 10 offices — Seattle, Krakow, Burnaby, etc. How does the engineering org coordinate across those geos? Is the team I'd be on co-located or distributed?"*

---

## Awareness — Things to know but DO NOT raise unprompted

These are real headwinds. Useful to know in case the interviewer brings them up; **do not bring them up yourself** — it reads as either negative or naive.

- **Stock pressure despite Q1 beat.** Volume grew 37% but revenue only 25% — per-dollar margin is compressing, signaling pricing pressure. If asked about business sustainability, frame as "interesting growth-vs-margin tradeoff" rather than "I'm worried about it."
- **Founder transition risk.** Matt Oppenheimer was founder-CEO for ~15 years. Founder departures introduce 12–18 month execution risk. Gunningham's background is strong, but strategic direction will shift.
- **Competitive squeeze.** Wise undercuts on transparent FX; Western Union does ~55%+ digital revenue with a huge agent network. Don't bring up competitors unprompted.
- **Stablecoin uncertainty.** USDC rails could disintermediate parts of the FX-spread revenue. Remitly is leaning in (USDC in Wallet) which is the right move. If they ask, frame as "interesting infra bet" not "existential risk."
- **Regulatory / immigration exposure.** Customer base is heavily immigrant; US immigration policy shifts directly affect customer acquisition. Q1 framed regulatory pressure as a tailwind (drove digital remittance demand) but it cuts both ways. **Politically sensitive — keep neutral if it comes up.**
- **AI-Native role is unproven culturally.** "Near-100% agent-generated production code" is an aggressive bet with no public outcome data. Be curious in the room, not skeptical.

---

## Part 2 — Me (what I'll say about myself)

**TODO — fill in 2026-05-18 behavioral prep session.**

### "Tell me about yourself" (60-90 sec)

TODO — draft. Frame: current role → what John does day-to-day → the deliberate transition into full-stack + AI engineering → why now. **Lead with the AI-integration experience** (streaming, cost control, prompt lifecycle) since it maps directly to Remitly's AI-Native direction.

### "Why this company?"

TODO — draft. Hook to specifics:
- AI-Native engineer role family being a real strategic bet (not Copilot bolt-on)
- Immigrant-customer mission (genuine resonance, not generic "I love fintech")
- The four-pillar evolution beyond pure remittance

### "Why are you leaving / looking?"

TODO — draft. Honest, forward-looking. No bashing current employer.

### STAR Stories

TODO — 4 stories minimum. Themes to cover:

#### Story 1 — Theme: **TODO — LLM integration / AI engineering judgment**
*Highest priority for Remitly. Use a real story about an LLM production integration John has shipped — what broke, what he'd do differently.*

- **Situation:** TODO
- **Task:** TODO
- **Action:** TODO
- **Result:** TODO

#### Story 2 — Theme: **TODO — full-stack ownership / TS+React delivery**
*Bread-and-butter — demonstrate the 3 years of full-stack experience cleanly.*

- **Situation:** TODO
- **Task:** TODO
- **Action:** TODO
- **Result:** TODO

#### Story 3 — Theme: **TODO — failure / learning-from-mistake**
*Senior-flavored move. Mid-level interviewers love this one.*

- **Situation:** TODO
- **Task:** TODO
- **Action:** TODO
- **Result:** TODO

#### Story 4 — Theme: **TODO — scope-cut / pragmatism / cross-functional collaboration**

- **Situation:** TODO
- **Task:** TODO
- **Action:** TODO
- **Result:** TODO

### Standard Curveballs

- **Biggest weakness:** TODO — frame around Python production fluency being a deliberate rebuild (matches Remitly's stack, shows self-awareness).
- **Where do you see yourself in 5 years:** TODO
- **What's a project you're proud of:** TODO — probably the LLM integration project (same story as STAR #1, different framing).
- **Tell me about a disagreement with a manager:** TODO
- **Why should we hire you:** TODO
