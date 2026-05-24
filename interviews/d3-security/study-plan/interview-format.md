# D3 Security — Interview Format

What to expect from the D3 written test, per D3's confirmation email + 5 Glassdoor reviews across multiple roles.

---

## Round 1 — Written Test (per D3's email 2026-05-22)

- **Duration:** 120 minutes
- **Date:** Wednesday 2026-05-27, 3:00 PM PT
- **Location:** 300-1075 W Georgia St, Vancouver, BC V6E 3C9. 3rd floor; press doorbell near clear glass door.
- **Arrival:** On time, no more than 10 min early.
- **Setup:** D3-provided laptop, password from Support Team. Test via bookmarked link in Chrome (likely Google Forms based on Glassdoor pattern).
- **Closed-book rules:** No phone. No external internet. No AI assistants.
- **Amenities:** Water, snacks, paper, pens on-site.
- **Test parts (per D3):**
  - **Part 1:** Multi-Select Choice Questions
  - **Part 2:** Short Structured Answer Questions — bullet points, pseudo-code, architecture descriptions
- **Stated topic areas (AI Engineer specific):** System Integration, Multi-Agent Governance, Prompt/Trust Controls

After submission, candidates are "good to go" immediately. D3 contacts short-listed candidates within 2 weeks.

---

## Glassdoor Intel — Universal D3 Test Structure (5 reviews, multiple roles)

**Critical pattern:** D3's written test has a **universal structure across all engineering roles**, not just the named topic areas. Confirmed across Frontend Dev, Intermediate Full Stack, AI Engineer (limited), and other reviews.

The structure typically includes:

1. **~90 min logical reasoning / pattern / riddle section** (the LONGEST chunk, multi-select format, **no coding**).
2. **~30 min frontend / React fundamentals** (React.memo, useState, re-rendering behavior, JS fundamentals, web performance).
3. **~30 min backend code-reading** (screenshots of code, fill missing lines based on expected output — typically Python).
4. **~30 min database** — **MongoDB** specifically (not SQL). Aggregation pipeline, indexes, query optimization, schema design.

**For AI Engineer specifically:** the named topics (System Integration / Multi-Agent Governance / Prompt/Trust Controls) likely REPLACE some of the frontend / backend / database portions, but the **logical reasoning section almost certainly stays** as the dominant chunk.

---

## Confirmed Question Examples (from Glassdoor reviews)

### Logic puzzles (universal across roles)

- **Coin weighing:** *"You have 10 piles of coins. Each pile has infinite coins; each coin weighs exactly 10g except one pile where coins weigh 11g. You may weigh ONCE on a digital scale. How do you find the heavy pile?"* → Binary encoding: take 1 coin from pile 1, 2 from pile 2, ..., 10 from pile 10. Total expected weight = 550g. Subtract actual − 550 → that's the pile number.
- **Candy / ternary variant:** *"x+y+z=10 piles of candies; each pile weighs 1g, 2g, or 4g. Single weigh to identify all piles."* → Ternary encoding (take 1/3/9 from sequential piles, math out the difference).
- **Average speed harmonic-mean trap:** *"Average speed when half journey is at x mph, other half at y mph."* → 2xy/(x+y), NOT arithmetic mean.
- **Einstein's riddle / zebra puzzle** (5-house logic grid).

### Frontend (when present)

- React.memo behavior + memoization pitfalls (passing inline objects breaks memo)
- useState batching / functional update form
- Re-rendering rules + hooks dependency arrays
- Stale closures
- Zustand basics (lightweight state library, no provider, selector pattern)

### Backend (when present)

- Read Python code from a screenshot, fill in missing line based on expected output

### Database (when present)

- MongoDB aggregation pipeline questions
- Index selection / query optimization
- Schema design (denormalize vs reference)

---

## Difficulty + Subjective Read

- Glassdoor: **14% positive interview rating** — candidates often report the experience as unpleasant, with unconventional / "IQ-test" questions.
- Some reports describe behavioral questions about handling "verbal abuse" — politically tricky framing in the room.
- General candidate sentiment: technical bar is fair but unconventional; communication of test structure beforehand is poor (D3's email is unusually detailed here, which is a positive shift).

**Implication for John:** read every question twice. Don't pattern-match to common questions if the wording is odd. Leave 15-20% mental buffer for unexpected angles.

---

## Logistics (for Wed 2026-05-27)

- Address: 300-1075 W Georgia St, Vancouver, BC V6E 3C9
- 3rd floor, press doorbell near clear glass door
- Arrive on time, max 10 min early
- D3 provides laptop, paper, pens, water, snacks
- Bring: nothing technical (phone gets stowed). ID maybe.
- Day-of dress: business casual (in-office cybersecurity company; safe default)

After submission → John leaves. Hear back within 2 weeks if short-listed for Round 2 (Hiring Manager).
