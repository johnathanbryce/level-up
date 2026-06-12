# Diligent Case Study — Working Hub

**Round:** Final case-study interview (the "business use-case round" Cathy pre-briefed).
**When:** Wed **June 17, 2026, 10:00–11:00 AM PT**, via Microsoft Teams.
**Panel:** Thai Bao An Phan · Arthur Miyazaki (John's HM) · Morteza Jafari.
**Deliverable:** a high-level **design + process flow + high-level pseudo-code** for an
enterprise information-retrieval platform. **Not** a coded PoC, **not** a polished slide deck.

> Source of truth for the literal ask: [case-prompt.md](case-prompt.md) (verbatim, never edited).
> Decisions about tooling / repo / approach: [approach-decisions.md](approach-decisions.md).

---

## Status

| Item | State |
|------|-------|
| Email confirmed to recruiter | drafted (see chat) |
| Prompt captured verbatim | ✅ `case-prompt.md` |
| Approach / tooling decisions | ⬜ OPEN — to decide together (`approach-decisions.md`) |
| Solution design | ⬜ NOT STARTED (deliberately — groundwork only for now) |
| Diagram(s) | ⬜ |
| Pseudo-code | ⬜ |
| Out-loud walkthrough reps | ⬜ |

---

## What they're actually asking for (parsed — this is the rubric)

The instructions + PDF list overlapping requirements. De-duplicated, the graded deliverable is:

1. **A clear high-level design** to solve the business problem (any diagramming tool).
2. **Pre-steps / live-steps / post-steps**, clearly labelled.
   - *pre* = offline/ingestion/indexing work done before any query (the "how does the system know things" half).
   - *live* = what happens at query time during the sales cycle (Excel question → answer).
   - *post* = what happens after (write-back to Excel, review, feedback, eval, logging).
3. **Key GenAI / AI-ML technologies, actors, and flows** called out explicitly, with
   **recommendations on approaches** and **stated assumptions**.
4. **Process flows + high-level pseudo-code** (sequencing, steps, logic) — show the *how*,
   not just the boxes.
5. **An evaluation of effectiveness** — why this works, where it's weak, how you'd measure it.

### The four "ideal solution" constraints (must each be visibly addressed in the design)

| # | Constraint | What it really tests |
|---|-----------|----------------------|
| 1 | Scalable & modular for future workflows | Architecture maturity — clean seams, not a monolith script |
| 2 | Efficient, accurate, relevant retrieval | Core RAG / retrieval competence (chunking, embeddings, hybrid search, re-ranking) |
| 3 | **Secure, respects existing access permissions** | **The differentiator.** Per-user/per-doc access control on retrieval (ACL-aware RAG). GRC company — this is the trap most candidates underweight. |
| 4 | Auto-generate initial responses in the **same Excel file** | The "last-mile" integration — read questions from Excel, write answers back in place |

### Read on the panel / framing (carry over from prior prep)

- **Mixed audience, technical depth wanted.** The email tip literally says *"be detailed and go deep."* This is NOT the "don't be too technical" warning from the generic deck advice — they're explicitly asking for technical depth here. Go deep on the AI/ML.
- **Responsible AI is table stakes** (GRC company): security, access control, hallucination/grounding, citations, human-in-the-loop review before an answer lands in a client-facing proposal.
- **Thought process > polish** (Cathy). They want the *why* behind every choice and the alternatives you rejected.

---

## What we are NOT doing yet

Per John's instruction: **this is groundwork only.** No solution design, no diagrams, no tech
lock-in yet. Next working session we make the `approach-decisions.md` calls first
(repo strategy, diagramming tool, presentation surface), *then* start the design.
