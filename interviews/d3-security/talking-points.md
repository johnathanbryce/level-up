# D3 Security — Talking Points

**Status: ACTIVE.** 30-min behavioral interview Tue 2026-06-02 3:30 PM with **Jennie Jin (HR Manager)**. Round 1 (written test) passed. Technical depth (Morpheus architecture, MCPs, AI engineering specifics) saved for next round.

---

## Part 1 — Company

### D3 in 3 bullets (memorize these, not paragraphs)

- **SOC alert overload — they automate it.**
- **Two products:** Smart SOAR (established, no-code automation) + Morpheus (new, AI-driven autonomy). **I'd be on Morpheus.**
- **15 years of SOC workflow knowledge is the edge** over AI-first newcomers.

### Quick context (only if asked deeper)

- Smart SOAR: 500+ integrations, reduces alert volume 90%+
- Morpheus: triages 100% of alerts in <3 min, L2-depth investigations, launched RSA 2025
- Buyers: SOC teams at mid-to-large enterprises drowning in alert volume; Tier 1 work is unhireable at scale.

### Signal worth knowing privately

- Written test was MCP-heavy → D3 is likely building MCP-based tool integration into Morpheus. Don't surface to HR; save for next round.

---

## Part 2 — Me

### TMAY (mic and refine — target ~90 seconds)

Anchor: ~3 years production TypeScript/React; last year+ shipping production AI features at Caseway (RAG, public-facing search, full-stack, Lead role); looking for a role where **AI is the core product, not a feature on the side**.

### Why D3 (sharpened — speakable cold)

> "Two pieces. First, the role itself — building AI-powered product features at the intersection of LLMs, backend, and production reliability — maps almost exactly to what I've been doing at Caseway. Second, what makes D3 specifically interesting: AI in security is the hardest version of the trust problem. You're not shipping a feature — you're shipping autonomous reasoning on data where being wrong is a breach, not a typo. The engineering discipline around it — guardrails, eval, observability, AI as a trust layer — actually matters here. That's a natural extension of the AI work I've already been shipping."

### Concrete Caseway anchor (pick ONE to lead with)

- Public-facing legal-case search engine with BM25 fallback, ambiguous-query handling, rate limiting
- Production RAG pipeline using Elasticsearch + Postgres
- AI-assisted coding workflow (Claude Code / Cursor) as part of daily ship discipline

### Why leaving Caseway (DRAFT TODAY — biggest gap, HR will ask)

(TBD via mic. Keep neutral, forward-looking. Frame as "I want to go deeper on AI as the core product" rather than anything negative about Caseway.)

### STAR story candidates (pick 1-2 for today)

- **Caseway scope-jump (ownership).** CTO + other dev left same week Sept 2025, promoted to Lead, owned dev end-to-end with no handover. Hits **ownership** — the exact word Glassdoor flagged.
- **AI/RAG production ship (builder + domain fit).** Full-stack legal-case search engine. Hits "shipped AI-powered features in enterprise software" almost verbatim.
- **AI-assisted dev workflow (meta + builder mindset).** Meaningful use of Claude Code / Cursor as part of shipping discipline.
- **Failure / learning** — TODO if time.
- **Conflict / hard tradeoff** — TODO if time.

---

## Reverse Questions for HR (5 to bring on paper)

1. "What's the engineering team culture like day-to-day?"
2. "How does D3 think about engineer growth paths?"
3. "If I'm 12 months in and you're happy with this hire, what does that look like?"
4. "What does the rest of the interview process look like after this round?"
5. "What do you personally like most about working at D3?"

**Save for next round (technical / HM):**
- MCP integration in Morpheus
- Eval and trust story for autonomous investigations
- Team shape between AI/ML and product engineers
- AI-assisted dev workflow practices
- Escape hatch for wrong investigations
