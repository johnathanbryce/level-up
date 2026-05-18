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

## FX rate locking

When you initiate a cross-border transfer at 10:00am, the FX rate is X. By the time the transfer settles 30 minutes later, the rate may have moved. Customers expect the rate they saw at 10:00am — not the rate at settlement.

**The engineering pattern:** Lock a quoted rate at request time, hold it for some window (often minutes to hours), and execute the transfer at the locked rate. If the window expires, re-quote.

**Why it's hard:** the company carries FX risk during the locked window — if the market moves, they eat the spread. So the locking duration is a **business + risk decision**, not just an engineering one.

---

## Atomicity across multi-leg transfers

A cross-border transfer often has multiple legs:

1. Debit sender's card / bank account
2. Convert USD → local currency
3. Credit recipient's bank account (or cash agent)

These can happen across different systems, sometimes days apart. **You cannot run a single database transaction across all of them.** So how do you guarantee that either ALL legs complete or NONE do?

**Patterns used:**

- **Saga pattern** — sequence of local transactions, each with a *compensating action* if a downstream leg fails. E.g. if step 3 fails, step 1 issues a refund.
- **Event-driven choreography** — each leg emits an event; downstream legs react.
- **State machines** — every transfer has an explicit state (`INITIATED`, `DEBITED`, `CONVERTED`, `CREDITED`, `FAILED`, `REVERSED`). The whole system is built around getting transfers through the state graph correctly.

You don't need to implement these for a recruiter chat — just recognize the words.

---

## Settlement vs. disbursement

- **Settlement** — the underlying clearing of funds between banks. The actual money movement at the rail level. **Slow** (hours to days).
- **Disbursement** — the customer-facing event of the recipient receiving funds. **Fast** (Remitly's value prop: minutes).

Remitly's product is fast disbursement on top of slow underlying rails. They *front* the recipient's funds and settle with the sending side asynchronously. **This is the financial engineering moat** — it requires trust, capital reserves, fraud controls, and operational excellence.

---

## AML / KYC basics

- **AML** — Anti-Money Laundering. Regulations preventing money laundering through financial services.
- **KYC** — Know Your Customer. Identity verification at onboarding.
- **Sanctions screening** — checking senders / recipients against government watchlists (OFAC in the US, equivalents in other jurisdictions).
- **Transaction monitoring** — flagging suspicious patterns (structuring, unusual destinations, velocity anomalies, large round numbers).

These are **regulatory obligations, not optional.** They shape engineering decisions: identity data must be retained for X years, certain corridors require additional checks, every transaction must produce an auditable trail.

---

## Likely recruiter prompts + canonical answers

- **"Have you worked on payments systems before?"** → "Not specifically, but I have strong vocabulary on the core patterns — idempotency, atomicity across legs, settlement vs disbursement. Idempotency in particular is the foundation of any reliable transfer system, and I've worked deeply with it on the system design side."
- **"What interests you about fintech?"** → *Genuine answer.* Suggested framing: "The engineering constraints are unusually load-bearing — compliance, atomicity, and reliability aren't bolt-ons, they shape the architecture. That's interesting work."
- **"What do you think the hardest part of Remitly's engineering problem is?"** → "Probably layering the new Wallet / Card / Borrow products on top of the existing transfer engine without compromising the compliance and reliability guarantees the transfer side already meets. New product surfaces on a regulated platform is hard."
