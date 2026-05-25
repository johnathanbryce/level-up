# D3 Security — Role

## Posting

**Title:** AI Engineer
**Company:** D3 Security Management Systems
**Location:** Greater Vancouver Area (In-Office Only) — 300-1075 W Georgia St, V6E 3C9
**Type:** Full-time, permanent
**Schedule:** Monday-Friday
**Benefits:** Extended health, dental, on-site gym, commuter reimbursement

## Role Summary (verbatim, condensed)

> D3 Security is looking for a hands-on AI Engineer to build AI-powered product capabilities and improve how modern software is developed, tested, and delivered. **Sits at the intersection of AI product engineering, full-stack development, and AI-assisted coding workflows.**
>
> Work on practical product problems, build reliable software, apply modern AI tools and LLM capabilities to real customer and internal engineering use cases. Strong in implementation, comfortable across the stack, excited to build AI-enabled features in a production environment.

## What You'll Be Doing

- Build + ship AI-powered product features combining LLMs, backend services, APIs, data systems, frontend
- Implement AI-assisted development workflows for engineering productivity / software quality
- Contribute to **multi-step application flows** involving model outputs, tool usage, business logic, validation
- Integrate AI capabilities into production systems reliably + maintainably
- Collaborate with engineering, product, design
- Improve quality of AI-enabled systems through testing, experimentation, measurement, iteration
- Production readiness: observability, debugging, CI/CD, operational reliability
- Contribute to internal patterns and reusable components

## What You'll Bring

- **2+ years software engineering** building + shipping production applications
- Strong coding in **Python and/or C#** + solid backend fundamentals
- Modern web dev with **JavaScript/TypeScript**, ideally React or similar
- Building or integrating **API-driven systems** across application layers
- **Practical familiarity with LLMs, AI developer tools, or AI-powered product features**
- Turn ambiguous requirements into structured implementation plans
- **Judgment around when AI vs traditional software logic** is appropriate
- Strong problem-solving, attention to quality, builder mindset
- Comfort with code reviews, testing, continuous improvement
- Clear written + verbal communication

## Nice to Have

- Has used AI coding tools to meaningfully change how they build software (not just experimented)
- Familiarity with **Docker, Kubernetes, or Azure**
- Experience shipping AI-powered features in **enterprise software**
- Interest in cybersecurity, automation, workflow-heavy systems
- Exposure to **evaluation, prompt iteration, reliability practices for LLM apps**

---

## Stack Cross-Reference vs. John's Roadmap

| Stack item | John's coverage | Where in roadmap | Notes |
|---|---|---|---|
| **Python** | Rebuilding (1 yr surface, AI-assisted) | [`01-algorithms/CLAUDE.md`](../../01-algorithms/CLAUDE.md) | Primary focus topic; comfortable reading, growing on writing |
| **C#** | None | Not in roadmap | Skip — Python is the named alternative; lean on Python |
| **TypeScript / JavaScript / React** | Strong (3 yrs production) | [`06-frontend/CLAUDE.md`](../../06-frontend/CLAUDE.md), [`remitly/study-plan/react-js-ts.md`](../remitly/study-plan/react-js-ts.md) | Bread and butter |
| **LLM / AI integration** | Strong (Caseway production work) | n/a — workplace | RAG, BM25 search, public-facing search engine shipped |
| **AI-assisted dev tools** | Strong (uses Claude Code, Cursor) | n/a — workplace | Real differentiator vs candidates who've only "experimented" |
| **APIs / backend services** | Strong (FastAPI at Caseway) | [`02-system-design/CLAUDE.md`](../../02-system-design/CLAUDE.md) | Solid |
| **System design fundamentals** | Strong (12 notes complete) | [`02-system-design/notes/`](../../02-system-design/notes/) | API gateway, observability, idempotency, message queues, caching — all done |
| **Docker / K8s / Azure** | Light Docker; no K8s or Azure | [`07-devops/CLAUDE.md`](../../07-devops/CLAUDE.md) | Frame as learnable; not a likely test focus |
| **Evaluation / prompt iteration** | Partial (does this at Caseway implicitly) | TBD | Add concept layer during cram |
| **MongoDB / NoSQL** | Light (Postgres background) | TBD | Vocab pass during cram (per Glassdoor pattern across D3 roles) |

---

## Gap Inventory (vs. the test)

| Gap | Test relevance | Severity | Crammable in 2 days? |
|-----|----------------|----------|------------------------|
| **Multi-agent governance vocabulary + concepts** | HIGH (named topic) | Real | YES — concept-level only, not framework alphabet soup |
| **Prompt/Trust controls framing** | HIGH (named topic) | Real | YES — 4-5 key concepts (injection, jailbreak, validation, defense-in-depth, system prompt leakage) |
| **Agent patterns (ReAct, function calling, multi-agent)** | HIGH (cross-cutting) | Medium | YES — extends his Caseway LLM work |
| **RAG architecture depth** | MEDIUM-HIGH | Low | YES — leverage Caseway production experience, formalize the vocabulary |
| **Logic puzzles** | HIGH (~90 min of the test based on Glassdoor universal pattern) | **REAL — John self-flagged weakest** | YES — drill 6/day across 10 pattern categories |
| **D3 / Morpheus / ASOC domain** | MEDIUM | Low | YES — 30-45 min primer |
| **MongoDB essentials** | LOW-MEDIUM (universal D3 pattern, may not appear for AI Engineer) | Low | YES — 30 min vocab |
| **C# fluency** | LOW (Python AND/OR per JD) | Skip | NO — defer entirely, lean on Python |

**What John has strong (use as leverage):**
- Ships LLM/RAG features daily at Caseway — real production AI engineering experience
- Strong TypeScript/React for any frontend portion
- Strong FastAPI/Python backend
- Solid system design fundamentals (12-note pass complete)
- Uses AI dev tools meaningfully — direct nice-to-have hit

---

## Must Speak Intelligently On

Non-negotiable concepts for the written test. Reflex-level recall, no fumbling.

### Core 5 (foundation for any test section)

1. **What an LLM application actually IS as a system.** Not just "call an LLM" — the full loop of prompt construction, tool calling, output validation, error handling, observability.
2. **RAG architecture end-to-end.** Ingest → chunk → embed → vector store → retrieve → rerank → context assembly → generate → cite. Know each stage's failure mode.
3. **Agent patterns:** ReAct loop, plan-and-execute, function calling. When to use a single LLM call vs an agent loop.
4. **Multi-agent governance — at the CONCEPT level.** Role boundaries, human-in-the-loop checkpoints, audit trails, escalation policies. Not framework names.
5. **Prompt/Trust controls — at the CONCEPT level.** Prompt injection, jailbreak, system prompt leakage, output validation, defense-in-depth as a principle. Not OWASP list memorization.

### Domain-contingent (drill enough to engage)

6. **ASOC / SOC tiers + Morpheus positioning.** T1 = triage, T2 = investigate/respond, T3 = hunt. Morpheus claims L2-depth automation. Competitive: Torq, Tines, Dropzone, Prophet.
7. **Logic-puzzle pattern reflex.** Recognize the puzzle category in <30s, reach for the trick.

### Lower priority

8. MongoDB aggregation + indexes + when-vs-Postgres
9. System integration architecture diagrams (LLM gateway, RAG pipeline, multi-agent orchestrator)

---

## Cram Priority

Ordered for the 2-day window (Mon + Tue):

1. **`ai-engineering-foundations.md`** — LLM application patterns; transferable beyond D3
2. **`agents-and-tool-use.md`** — ReAct, function calling, multi-agent basics
3. **`rag-deep.md`** — full RAG architecture; formalize Caseway experience
4. **`logic-puzzles.md`** — 18-puzzle bank across 10 categories; drill 6/day
5. **`multi-agent-governance-light.md`** — concept-level governance
6. **`prompt-safety-essentials.md`** — 4-5 concepts (not OWASP cram)
7. **`mongodb-essentials.md`** — high-level NoSQL primer
8. **`system-integration-llm.md`** — reference architectures (leverages existing sysdesign notes)
9. **Mock test** Tuesday afternoon

---

## Seniority Signals

- Role asks **2+ years** software engineering — John clears this (3 years).
- "Hands-on AI Engineer" implies builder mindset, not research scientist. John's Caseway shipping experience is the ideal match.
- Production-readiness language (observability, CI/CD, operational reliability) signals they want engineers who've actually run things in prod — not LLM-tutorial-completer profile.
- Mention of "AI-assisted development workflows" suggests they care about *meta* — using AI to ship better, not just shipping AI features. John's Claude Code / Cursor usage is a real differentiator.

---

## Why This Role Fits John (draft pitch — refine in [talking-points.md](talking-points.md) if Round 2 advances)

> "I've spent the past year-plus shipping production AI features at Caseway — RAG with Elasticsearch and Postgres, a public search engine with BM25 fallback, the full integration story across Next.js, FastAPI, Nginx. The 'AI Engineer at the intersection of product, full-stack, and AI-assisted workflows' framing matches almost exactly what I already do. And Morpheus is interesting because the engineering problem — automating Tier 1-3 analyst work reliably enough that humans can trust it — is exactly the kind of problem where the AI engineering discipline (prompt safety, eval, observability, governance) actually matters, not just the model layer."
