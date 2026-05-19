# Payments Domain Primer

Highest-leverage non-tech topic for Remitly specifically. They move money for a living. Every role touches the money flow in some way.

---

## Why this matters

Remitly's core engineering problem is **moving money correctly across borders.** Reliability and compliance aren't features — they're the architecture's hard constraints. Recruiters love when candidates show domain awareness because most engineers walk in cold.

---

## Idempotency (you have this LOCKED — refresh)

**Definition:** An operation is idempotent if doing it multiple times produces the same result as doing it once.

**Why it matters in payments:** Networks fail. Retries happen. Without idempotency, a retry can double-charge or double-send.

**How it's implemented:** Clients send a unique `Idempotency-Key` header per logical operation. Server records the key + result. Retries with the same key return the cached result instead of re-executing.

**Killer answer if asked:** *"Idempotency guarantees that a customer's card gets charged once, even if the network hiccups and the client retries five times."*

---

## Settlement vs. disbursement (Remitly product moat)

- **Settlement** = slow underlying clearing between banks (hours to days).
- **Disbursement** = customer-facing delivery of funds (minutes — Remitly's value prop).

Remitly *fronts* the recipient's funds and settles with the sending side asynchronously. **That's the financial engineering moat** — fast disbursement on top of slow rails, made possible by trust, capital reserves, and fraud controls.

---

## Likely recruiter prompts + canonical answers

- **"Have you worked on payments systems before?"** → "Not specifically, but I have strong vocabulary on the core patterns — idempotency in particular, which is the foundation of any reliable transfer system. I've worked deeply with it on the system design side."
- **"What interests you about fintech?"** → *Genuine answer.* Suggested framing: "The engineering constraints are unusually load-bearing — compliance, atomicity, and reliability aren't bolt-ons, they shape the architecture. That's interesting work."
- **"What do you think the hardest part of Remitly's engineering problem is?"** → "Probably layering the new Wallet / Card / Borrow products on top of the existing transfer engine without compromising the reliability guarantees the transfer side already meets. New product surfaces on a regulated platform is hard."

---

## Phase 2 expansion topics (deferred — if WARP advances)

If Role 3 (WARP / Wallet Product Risk) goes to a technical screen, re-read prior git history of this file or expand `phase-2-technical-cram.md` to cover: **FX rate locking**, **multi-leg atomicity (saga pattern, state machines)**, **AML / KYC basics, sanctions screening, transaction monitoring**. Not needed for the recruiter chat.
