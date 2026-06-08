# Deep Core Technology — Role

## Posting

**Title:** Founding Engineer (employee #1)
**Company:** Deep Core Technology — Squamish BC (deepcoretech.com)
**Comp:** $105-125K CAD + 1% equity
**Location:** Remote, Canada-eligible (John in Vancouver, ~1hr from Squamish)
**Perks:** yearly month abroad (last year Oaxaca)
**Stage:** actively fundraising; salary + equity funded

## Company

**"The subsurface thinking partner."** An agentic 3D modeling platform and geologic reasoning layer for mining / mineral exploration. Geologists describe geology in natural terms; the system reasons through data integration → model construction → iteration → validation. Live web app at app.deepcoretech.com.

**The pitch:** turns geologists from software *operators* back into *interpreters*. "Turn drill results into interactive 3D models in minutes."

**Founders:** Neil Seifert (CEO, structural geologist) + Jeff Thorslund (CTO, 10+ yrs resource-sector software). **John would be the first engineer.**

### The three layers (mental model)

1. **Data layer** — heterogeneous geoscience inputs (drillhole data, geologic maps, 2D/3D geophysics, block models, historical PDFs). Hard, unglamorous integration problem. John's wheelhouse.
2. **Reasoning / agent layer** — the wedge. Natural-language intent + data → orchestrates the modeling. The "thinking partner." **This is what Jeff screens for.**
3. **Visualization layer** — Cesium-based 3D web rendering; geologist sees / interacts with / validates the model in-browser.

---

## Tech Stack

- **TypeScript** — John strong (3 yrs production)
- **Python** — John strong (Caseway / FastAPI production)
- **Next.js** — John strong (production)
- **Supabase** — NEW. = managed Postgres + auth + RLS + realtime + storage + edge functions. Maps to John's Postgres + tenant-isolation experience.
- **CesiumJS** — NEW. Web 3D globe/terrain engine; perf with large subsurface meshes is the hard part.
- **Agentic systems / Claude Code** — John strong + a differentiator (daily Claude Code driver, built his own agentic system on top of it).

---

## Stack Coverage Table

| Stack item | John's coverage | Notes |
|---|---|---|
| TypeScript | Strong (3 yrs) | Bread and butter |
| Python | Strong (Caseway, FastAPI prod) | Daily |
| Next.js | Strong (prod) | Daily |
| Agentic systems / orchestration | **Strong + differentiator** | Claude tool-calling agents in prod; dual-model routing; built own agentic system on Claude Code |
| Claude Code internals | **Strong + differentiator** | Daily driver; CLAUDE.md state, subagents, MCP, hooks |
| Postgres / Redis / ES | Strong | Maps to Supabase (Postgres) |
| Supabase | None (Postgres maps over) | New surface = RLS; maps to JWT/tenant isolation |
| Cesium | None | Cocktail depth only; honest curiosity |
| Geology domain | None | Cocktail depth; informed questions, not expertise |

---

## Gap Inventory (vs. this round)

| Gap | Round relevance | Severity | Crammable in 2 days? |
|---|---|---|---|
| Agentic orchestration vocabulary + framing | **HIGH (screened)** | Low — has the experience, needs the language tight | YES |
| Claude Code internals as power-user talk | **HIGH (screened)** | Low — uses daily, needs to articulate | YES |
| Caseway stories tightened for spoken delivery | HIGH | Medium — rambling risk | YES |
| Supabase (RLS specifics) | MEDIUM | Low — Postgres maps | YES — 15 min |
| Cesium one-pager | LOW-MEDIUM | Low — curiosity only | YES — 15 min |
| Geology cocktail depth | MEDIUM | Low — informed questions | YES — 30-45 min |
| Opinions / trade-off articulation under light pressure | **HIGH (the "opinions" part)** | Medium | YES — rapid-fire drill |

---

## Must Speak Intelligently On

### Core (T1 — fluent, unprompted)

1. **Probabilistic planner + deterministic tools.** The LLM plans/interprets; anything that must be correct + repeatable is a deterministic tool the model orchestrates. (Geology has hard math — don't let the LLM do kriging in its head.)
2. **Planner-executor vs ReAct.** What each is, when each breaks. ReAct = think-act-observe loop (John's Casey retrieval loop). Planner-executor = inspectable plan before execution (trust win).
3. **Structured outputs as contracts + validation gates.** Typed JSON between steps; schema + semantic + human-in-the-loop validation. Pydantic / function-calling schemas enforce it.
4. **The Deep Core design-out-loud:** drillhole data + NL hypothesis → reviewable 3D model update. Six beats: planner → plan validation gate → deterministic geostat/geometry services → structured outputs validated each hop → render in Cesium → geologist human gate → loop.
5. **Claude Code as a power user:** context/compaction, CLAUDE.md state, tool permissions, subagents/parallel, MCP, hooks, headless/SDK.

### Supporting (T2 — reason about if asked)

6. **Eval strategy for agents** + failure modes (infinite loops, hallucinated tool calls, long-horizon decay) + retries/fallbacks/guards. Map to Caseway judge/eval + token/truncation guards + dual-model routing.
7. **System design, AI-flavored** — design-prompt framing, caching, rate limiting (cost control), async/queues for long jobs, idempotency, pgvector, LLM-specific observability. Reactivation of Section 2; Jeff may probe.
8. **Supabase = Postgres + RLS** → maps to JWT/tenant isolation. *(One-line fallback only — NOT studied.)*

### Out of scope (do NOT study)

- **Cesium** — one-line: web 3D engine, perf-with-large-meshes is the hard part. Curiosity, not expertise.
- **Geology domain** — product context only; curiosity beats bluffing.
- **C#, Docker/K8s deep, anything not Next.js/TS/Python** — not the focus.

**Primary stack to speak from real experience:** Next.js, TypeScript, Python.

---

## Seniority Signals

- Founding role = ownership + judgment + builder mindset, not narrow specialist. John owns two products end to end (arch → CI/CD → monitoring → releases) — ideal match.
- "Rooted in agentic systems" + explicit Claude Code ask = they want someone who *thinks correctly about agents*, not just calls an API. John's dual-model routing, tool loops, and self-built agentic system are direct evidence.
- Employee #1 at a fundraising startup = comfort with ambiguity + early-stage scrappiness. John's Caseway "took over as sole engineer, owned everything" story is on-point — frame honestly as lead, not sole.

---

## Why This Role Fits John (draft — refine in talking-points.md)

> "You're solving an agentic reasoning + trust problem on top of a hard data-integration problem, rendered in a 3D web app. I've spent the last year doing exactly the first two in a different vertical — production Claude agents, RAG over a real corpus, cost-aware routing, end-to-end ownership. The domain — geology, Cesium — is new, but the engineering shape is the same, and a real physical-world modeling problem is exactly the kind of thing I want to work on. Plus I'm an hour from Squamish and early-stage is where I do my best work."
