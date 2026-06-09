# Deep Core — Lesson Tracker

**This is the teaching content** Claude teaches from. Topic note files (`study-plan/<topic>.md`) are John's hand-notes scaffolds; this file is the source of truth for *what* gets taught.

---

## Current Position

> **SCOPE RESHAPED 2026-06-08 (Mon) mid-session — read this.** John pushed back (correctly) that the original plan over-indexed on *teaching concepts he already owns*. He builds agentic systems daily. This is **NOT a concept-learning cram — it's an articulation + opinion-readiness cram**: drill tight, honest, spoken answers to the questions Jeff will actually ask. Kill the lecturing on anything self-evident; the deliverable is a crisp spoken line + an honest anchor, not a textbook definition.
>
> **Two-day split (locked):**
> - **Mon PM/eve (today): NOTE-TAKING + quizzes mixed in.** Build solid, lean notes across the 5 areas below. One chunk → check question → confirm → next.
> - **Tue: depth + mock drilling** on Monday's notes (robust questions, Caseway stories tightened, opinions rapid-fire, full mock Q&A).
> - **Wed AM:** light reflex pass + re-read questions-for-Jeff. No new content.
>
> **5 study areas, ordered hardest/most-screened first:**
> 1. **Agentic systems must-knows** (THE screen) — ReAct vs planner-executor, the trust stack (grounding + structured outputs + validation gates + HITL), the six-beat Deep Core design-out-loud, Claude Code internals as a *power user*.
> 2. **AI foundations refresh** — only what supports agentic talk: context/compaction, RAG, structured outputs, evals.
> 3. **System design / technical**, framed to *their* product — long-running 3D-model build → async/queues, LLM caching, cost rate-limiting, monitoring.
> 4. **Database / backend** — Postgres/Supabase, schema + indexing basics, the likely architecture (below).
> 5. **React / Next.js** — high level only: rendering model, server vs client components, when to use which.
>
> **Cuts locked (do NOT lecture — one spoken line each):** planner+deterministic-tools (John flagged self-evident → one line + Caseway anchor only); structured outputs & validation gates folded INTO the "trust stack" answer; Supabase = "managed Postgres + RLS"; Cesium = "web 3D engine, large-mesh perf is the hard part"; geology = product context only.
>
> **CI/CD + monitoring bumped skip → LIGHT PASS** — explicitly in the JD ("ownership of the codebase, and the systems that support the software — project management, CI/CD, monitoring").
>
> **Likely backend architecture (John's peer-level inference, confirm w/ Jeff):** Next.js (Node) app layer via route handlers/server actions (NOT a separate Express server) + standalone **Python** geostat/agent services (geostats ecosystem = PyKrige/GeostatsPy/GemPy + NumPy/SciPy) + Supabase Postgres. Smart Q for Jeff: *"Next.js app layer talking to Supabase, geostat compute as separate Python services — is that the shape, or more consolidated?"*
>
> **Grading bar (spoken round):** fluency, honesty, brevity. John's #1 risk = overclaiming or rambling. Target every answer ~15-25 sec: name the trade-off, take a position, give the honest caveat, STOP.
>
> **Progress (Mon eve):** Notes DONE for **Area 1** (agentic: planner+deterministic, ReAct vs planner-executor, trust stack, failure modes, evals, six-beat design, tool-calling mechanism; Claude Code: MCP/hooks/subagents/compaction w/ code+diagrams in `claude-code-internals.md`), **Area 2** (`ai-foundations.md` — RAG/hybrid/embeddings-vs-response-caching), **Area 3** (`system-design.md` — all 11 concepts). **Area 5 (React/Next, MEDIUM)** chunks 1-5 done; **6-8 left**. **Area 4 (backend-databases) NOT started.**
> **ALL quizzes + interview Qs deferred to Tue.** Tue warm-up: write a `useDebounce` hook (hands-on). Carry-forward weak spot: Caseway-mapping reflex + tighten spoken delivery (rambling = #1 risk).

---

## ⏱ TIME REALITY — READ THIS (locked 2026-06-08)

**We have ~ONE DAY of real study time, max.** Hard rules:

- **NO getting into the weeds.** The bar is: *speak intelligently about software-engineering trade-offs and AI.* It is NOT: recite definitions, memorize APIs, or go deep on any one tool.
- **Stack focus = Next.js / TypeScript / Python.** These are John's daily-driver primary stack — speak from real experience here.
- **Supabase + Cesium: NOT studied.** One-line "if it comes up" fallback only (see bottom of L4). Supabase = managed Postgres + RLS → maps to his tenant-isolation work; Cesium = web 3D engine, perf-with-large-meshes is the hard part. That's all.
- **Geology: NOT studied.** Product context only (role.md / talking-points.md). Curiosity beats bluffing.
- **System design IS in scope** — John wagered Jeff may probe it (founding eng at an AI startup). He already owns Section 2 fundamentals; L4 is reactivation + AI framing, not new teaching.
- **Tier discipline:** drill T1 chunks to fluency; treat T2 as "reason about if asked, don't memorize." When in doubt, TRIM.

---

## How This File Works

1. Claude teaches from this file, lesson by lesson, chunk by chunk.
2. John takes notes in the matching `study-plan/<topic>.md` scaffold.
3. Between chunks: Claude asks the check question; John answers in his own words; confirm before moving on.
4. At end of each lesson: **cold quiz** (5-7 questions, conversational answers — this is a *spoken discussion* round, so grade for fluency + honesty + brevity, NOT exact vocab recall).
5. End of session: update Current Position + session log + flag weak spots.

**Tier markers:** T1 = speak fluently unprompted; T2 = reason about if asked; T3 = recognize / one-line. Default lean; John's Tier-3 pushback is reliably right.

---

## Lesson 1 — Agentic Orchestration (HIGHEST LEVERAGE)

**Time:** ~75-90 min (Mon)
**Notes file:** [study-plan/agentic-orchestration.md](study-plan/agentic-orchestration.md)
**Goal:** John speaks fluently about multi-step agent design and can run the Deep Core design-out-loud cold, mapping every piece to something he built at Caseway.

### Chunks

| # | Chunk | Tier | Teach | Check question |
|---|---|---|---|---|
| 1 | Probabilistic planner + deterministic tools | T1 | The single most important framing. "LLM plans + interprets; it does NOT compute. Anything that must be correct + repeatable → deterministic tool the model orchestrates." Geology has hard math (kriging, geometry, volumes) — LLM decides *which* operation + params, a service executes it. Caseway anchor: agents don't invent case law — they call ES retrieval (deterministic) and reason over results. | "Why is planner+deterministic-tools the right shape for Deep Core specifically?" → geology math must be correct/repeatable; LLM orchestrates services, doesn't do math in-head |
| 2 | Planner-executor vs ReAct | T1 | **ReAct** = think→act→observe loop, decides next step from last result. Adaptive, but can loop / drift. John's Casey retrieval IS ReAct. **Planner-executor** = produce full plan first, then execute. Plan is inspectable *before* running = trust + a natural HITL gate + cheaper (fewer LLM calls). Trade-off: less adaptive to surprises mid-run. | "When would you choose planner-executor over ReAct?" → when you want the plan reviewed before execution (trust/regulated), known step space, cost/SLA matters |
| 3 | Structured outputs as contracts | T1 | Between steps you pass **validated typed data (JSON to a schema)**, not freeform prose. Output of step N = typed input of step N+1. Enforced by Pydantic / native structured outputs / tool-call schemas. If it doesn't validate, you don't execute — retry or reject. Deep Core: planner emits `{operation, units, constraints}` a geostat service consumes. | "Why are structured outputs the 'glue' of a multi-step agent?" → typed contract between steps; invalid output caught before it corrupts the next step |
| 4 | Validation gates | T1 | Three flavors: **schema** (well-formed?), **semantic** (sensible? — geometry self-intersect? volume physically possible?), **human-in-the-loop** (geologist reviews + approves). Deep Core's whole product IS a HITL gate — the geologist is the final reviewer. Agent proposes, expert disposes. That's the design, not a weakness. | "Name the three kinds of validation gate and give a geology example of the semantic one." → schema/semantic/HITL; semantic = reject a self-intersecting surface or impossible volume |
| 5 | Failure modes + guards | T1 | Agent failure modes: infinite loops, hallucinated tool calls, long-horizon decay (quality drops over many steps), silent success (returns junk with a 200). Guards: **token budget guard**, **truncation guard** (context overflow), **loop/max-step cap**, **retry with corrective message**, **fallback** (cheap model fails → escalate; tool fails → degrade). John has all of these at Caseway — name them with this vocab. | "Name two agent failure modes and the guard for each." → e.g. infinite loop → max-step cap; hallucinated tool call → strict schema + validation |
| 6 | Evals | T2 | How you know the agent is good. Offline: test set of inputs w/ known-good outputs, scored (often **LLM-as-judge**). Online: production monitoring + regression tracking. Caseway anchor: judge/eval patterns. Deep Core eval is *hard + interesting* — how do you eval a geologic model? Against expert-validated reference models + geologist acceptance rate. Raising the question = senior signal. | "How would you even evaluate Deep Core's agent output?" → expert-validated reference models + geologist acceptance/edit rate; offline judge + online monitoring |
| 7 | The Deep Core design-out-loud (CAPSTONE) | T1 | *"An agent takes drillhole data + a geologist's described hypothesis and produces a reviewable 3D model update."* Six beats: (1) **planner agent** ingests NL hypothesis + data summary → structured plan of modeling ops; (2) **validation gate** on the plan (schema + sanity); (3) **deterministic geostat/geometry services** execute each step (LLM does NOT do the math); (4) **structured outputs** flow + validate each hop; (5) **render** candidate model in Cesium; (6) **human gate** — geologist accepts/refines in NL → loop. | John runs all six beats out loud, cold, mapping ≥3 to Caseway. |

### End-of-Lesson Quiz (conversational)

1. In one sentence: what should the LLM do, and what should it never do, in an agentic geology system?
2. ReAct vs planner-executor — define each, name when you'd pick planner-executor.
3. What's a "structured output as a contract" and why does it matter between steps?
4. Three validation-gate flavors + a geology example of the semantic gate.
5. Two agent failure modes + the guard for each.
6. Walk the six-beat Deep Core design out loud. Map at least three beats to Caseway.
7. How would you evaluate whether the agent's 3D model output is any good?

---

## Lesson 2 — Claude Code Internals + Agent-Assisted Dev (SCREENED)

**Time:** ~45-60 min (Mon)
**Notes file:** [study-plan/claude-code-internals.md](study-plan/claude-code-internals.md)
**Goal:** John talks about Claude Code as a *power user who understands the machinery*, not just a consumer. Jeff explicitly wants "understanding of Claude Code internals + orchestrating agents."

### Chunks

| # | Chunk | Tier | Teach | Check question |
|---|---|---|---|---|
| 1 | Context window mgmt + compaction | T1 | Finite context; long sessions get **compacted/summarized** so work continues without losing the thread. Power-user habit: keep durable state in files (CLAUDE.md) so context loss doesn't = memory loss. John's own system does exactly this (CLAUDE.md state tracking). | "How do you keep an agent effective across a long task when context is finite?" → compaction + externalize state to files, don't rely on the window |
| 2 | CLAUDE.md conventions + state | T1 | Project-level instructions + persistent state the agent reads each session. John's whole mentor system runs on this — structured sessions, state-tracking, model-as-reviewer. He can speak to it concretely because *it's the thing he built*. | "What goes in a CLAUDE.md and why does it matter for agent reliability?" → durable instructions + state; makes agent behavior consistent + resumable |
| 3 | Tool permissions | T1 | Agents act through tools; permission modes gate which tools run (allow/ask/deny). Least-privilege for safety. Maps to agentic governance + the Deep Core trust story (don't let an agent run destructive ops unreviewed). | "Why do tool permissions matter for a production agent?" → least privilege limits blast radius of a wrong/hijacked call |
| 4 | Subagents / parallel agents | T1 | Spawn focused sub-agents for independent work (search, review, scoped tasks) — each with its own context; run in parallel for fan-out. Keeps the main context clean (sub-agent returns the conclusion, not the file dump). | "When would you reach for a subagent instead of doing it inline?" → independent/parallelizable work, or to keep main context clean |
| 5 | MCP servers | T1 | **Model Context Protocol** — open standard for connecting LLMs to external tools/data sources uniformly. "USB-C of AI integrations." Standardized tool discovery + call format + audit trail. Relevant to integrating Deep Core's data sources cleanly. | "What problem does MCP solve?" → standard interface for LLM↔tool/data integration; uniform discovery + auditability across providers |
| 6 | Hooks | T2 | Deterministic scripts the harness runs on lifecycle events (pre/post tool use, on stop) — enforce policy the *model* can't be trusted to enforce. Example: a lint/test gate after every edit. Ties to "deterministic guardrails around a probabilistic core." | "Why use a hook instead of just instructing the model?" → hooks are deterministic; the harness runs them, not the model — guaranteed enforcement |
| 7 | Headless / SDK usage | T2 | Claude Code / Agent SDK can run non-interactively (CI, scripts, scheduled) — programmatic agents, not just a chat REPL. Enables building agentic features *on top of* the tooling (John's system). | "What does headless/SDK mode unlock?" → programmatic + automated agent runs (CI, pipelines), building agents into products |

### End-of-Lesson Quiz (conversational)

1. How do you keep an agent effective across a long task when context is finite?
2. What lives in a CLAUDE.md and why does it make agents more reliable?
3. Why do tool permissions matter — tie it to the Deep Core trust problem.
4. When do you reach for a subagent, and what does it buy you?
5. What is MCP and what does it standardize?
6. Hook vs prompt instruction — why is a hook stronger for enforcement?

---

## Lesson 3 — Caseway Stories (spoken + tightened)

**Time:** ~60 min (Tue)
**Notes file:** [study-plan/caseway-stories.md](study-plan/caseway-stories.md)
**Goal:** Crisp, honest, spoken versions of the anchor stories. Rambling is the enemy. Each story = situation → what John did → result, ≤90 sec.

### Stories to tighten

| # | Story | Honesty guard | Key beats |
|---|---|---|---|
| 1 | Caseway architecture end-to-end | "lead engineer," owns 2 products | Casey (AI legal research) + Bespoke (multi-tenant doc RAG); Next.js + FastAPI, Postgres + Redis, Elasticsearch, Docker + GH Actions; he owns arch→CI/CD→monitoring→releases |
| 2 | Cost optimization | "$150→$60/day, measured on billing dashboard, ~60%" | Dual-model routing: cheap model first, escalate on need; measured 2 months in prod |
| 3 | How agents fail + how he catches it | honest about what's monitored vs not | Tool loops, retrieval grounding, guards (token/truncation), eval/judge; observability + monitoring |
| 4 | Isolation story | Casey uploads (NOT Bespoke per-user index — that wasn't his design) | user_uploads ES index scoped by user_id, 24h TTL, Redis keys scoped per user/chat/file |
| 5 | Why founding / why mining | genuine | early-stage native, owns end-to-end, real physical-world domain, BC-local, agentic reasoning over a hard problem (not another chatbot) |
| 6 | The Bespoke rewrite | "leading the rewrite," NEVER "shipped" | LangChain/LangGraph v2, in-progress/unmerged |

### End-of-Lesson Quiz

Fire each story cold; grade for honesty + brevity + energy. Flag any overclaim immediately.

---

## Lesson 4 — System Design (reactivation + AI framing)

**Time:** ~45 min (Tue)
**Notes file:** [study-plan/system-design.md](study-plan/system-design.md)
**Goal:** John already owns Section 2 fundamentals — this is NOT new teaching. Reactivate the core concepts and re-frame them for an AI/agent product so he can answer a "design this" or "how would you scale this" question fluently. Keep it tight; lean on existing `02-system-design/notes/`.

### Chunks

| # | Chunk | Tier | Teach | Check question |
|---|---|---|---|---|
| 1 | The "design a system" framing | T1 | The interview shape: **clarify requirements → estimate scale → name high-level components → data model → deep-dive the bottleneck → trade-offs.** For an AI startup expect it flavored as "design a RAG / agent pipeline" or "how would you scale the modeling backend." Don't jump to components before scoping. | "What are the first two things you do when handed a design prompt?" → clarify requirements + estimate scale, before any architecture |
| 2 | Caching | T1 | Cache-aside pattern + TTL + when NOT to cache (personalized / rarely-read / staleness-sensitive). **AI angle:** cache LLM responses + embeddings to cut cost AND latency; semantic cache for repeated queries. | "Where would caching help in an LLM product, and what's the risk?" → cache responses/embeddings for cost+latency; risk = stale answers, invalidation |
| 3 | Rate limiting | T1 | Token bucket (capacity + refill rate — state BOTH). **AI angle:** protect expensive LLM endpoints; always anchor to **$/hour-per-abusive-user** math. Maps to John's Caseway cost work. | "How would you rate-limit an endpoint that costs $0.05/call?" → token bucket; compute worst-case $/hr per user; set limit to a defensible ceiling |
| 4 | Async + queues + idempotency | T1 | Long-running agent runs / batch evals = background job via a **queue**, not request-response. **Idempotency** (Idempotency-Key) for agent-triggered writes so retries don't double-execute. Maps to Deep Core: a 3D model build is a long job → async + status polling. | "A model build takes 2 minutes. How do you architect that request?" → enqueue background job, return job ID, poll/stream status; idempotent so retries are safe |
| 5 | Data + scaling | T2 | Postgres as default; read replicas before sharding; **pgvector** for vectors when you're already on Postgres. **Don't over-engineer at 2-person scale** — modular monolith, scale when you can name the bottleneck. | "5M vectors, you're already on Postgres — dedicated vector DB or pgvector?" → pgvector (one system, transactional, one backup); dedicated only at named scale/throughput |
| 6 | Observability + reliability | T2 | Standard logs/metrics/traces PLUS **LLM-specific:** cost-per-call, eval/faithfulness score, hallucination rate, drift. **Circuit breaker** for LLM provider failures (slow dependency = thread pool exhaustion). | "Name two LLM-specific things you'd monitor that a normal app wouldn't." → per-call cost + eval/hallucination rate (also: drift, token usage) |

### End-of-Lesson Quiz

1. First two moves when handed a "design X" prompt?
2. Where does caching help in an LLM product + what breaks?
3. Rate-limit a $0.05/call endpoint — what do you compute first?
4. A model build takes 2 min — how do you architect the request?
5. pgvector vs dedicated vector DB — your default and why?
6. Two LLM-specific observability metrics a normal app wouldn't have?

### Supabase + Cesium — "if it comes up" fallback (NOT studied, do not drill)

- **Supabase** = managed Postgres + auth + **RLS** + realtime + storage + edge functions. New surface for John = RLS (tenant isolation in the DB vs app layer) → maps to his JWT/per-user scoping at Caseway. Smart Q: *"RLS for tenant isolation, or app-layer?"*
- **Cesium** = web 3D globe/terrain engine; hard part = perf rendering large subsurface meshes (LOD/tiling/streaming). Smart Q: *"How are you handling perf with large meshes?"* Don't bluff — curiosity + one smart question.

---

## Lesson 5 — Opinions / Trade-off Rapid-Fire

**Time:** ~30-45 min (Tue)
**Notes file:** [study-plan/opinions-tradeoffs.md](study-plan/opinions-tradeoffs.md)
**Goal:** The "opinions" half of the round. Drill answering trade-off questions tightly: name the trade-off, take a position, give the honest caveat. NO rambling, NO fence-sitting.

### Question bank (Claude fires; grade for crispness + a defensible position)

1. **When would you NOT use an agent / LLM?** → when the task is deterministic + known-shape; a plain function or single structured call is cheaper, faster, testable. Reach for agents only for dynamic discovery / course-correction.
2. **How do you make agent output trustworthy enough that an expert accepts it?** → grounding (RAG/data), structured outputs, validation gates, HITL review, evals, citations/traceability. Trust is engineered, not prompted.
3. **Build vs buy a vector DB?** → start with what's in your stack (pgvector on Supabase Postgres = one system, transactional, one backup); reach for dedicated (Pinecone/Qdrant/Weaviate) only at scale/throughput you can name.
4. **Monolith vs services at a 2-person startup?** → monolith / modular monolith. Premature service-splitting is the classic early-stage mistake; you don't have the team or the scale. Honest + senior.
5. **How would you decide what to build first as employee #1?** → de-risk the riskiest assumption; talk to design partners; ship the smallest reviewable slice of the core loop. (Also a great answer to give Jeff.)
6. **Where does agentic reasoning break down on a hard modeling problem?** → long-horizon decay, hallucinated steps, can't verify its own geometry — which is exactly why deterministic services + HITL gates carry the correctness load.
7. **LLM vs traditional logic — how do you choose?** → LLM for ambiguous/natural-language/judgment; traditional code for anything correctness-critical + repeatable. (This is literally in their JD as a desired skill.)

---

## Lesson 6 — Questions for Jeff + Close

**Time:** ~15 min (Tue)
**Notes file:** [study-plan/questions-and-close.md](study-plan/questions-and-close.md)

### Best 4-5 questions (founding-eng diligence, casual tone)

1. **Product reality:** What's live today vs vision — paying users or design partners?
2. **First 90 days for employee #1:** shipping features, hardening, or figuring out what to build?
3. **Eng/product split:** how do Jeff + Neil divide things?
4. **Biggest technical risk (power move):** "My guess is making geologic reasoning trustworthy enough that geologists accept the output — is that the wall, or something else?"
5. **Runway/stage:** what are you raising and roughly when to close? (fair as employee #1 taking equity; keep light)
- **In pocket:** equity mechanics — "is the 1% a standard 4-yr vest, is there a strike set yet?" (only if comp comes up)
- **In-flow technical Q:** "Are you leaning planner-executor or ReAct, or a mix? Curious how you've structured the reasoning layer." Follow-up: "At Caseway my retrieval agents are basically ReAct loops — I've been curious where that breaks on a harder planning problem like 3D modeling." (peer, not applicant)

### The close

Ask for the next step explicitly: **"What does your process look like from here?"** Goals of this round: rapport, mutual fit, a concrete next step.

---

## Lesson 7 — AI Foundations Refresh (Area 2, lean)

**Notes file:** [study-plan/agentic-orchestration.md](study-plan/agentic-orchestration.md) (or fold into claude-code-internals notes)
**Goal:** Only the foundations that support agentic talk — no definitions-for-definitions'-sake. John just finished AI Foundations; this is reactivation.

| # | Chunk | Tier | Teach |
|---|---|---|---|
| 1 | Context window + compaction | T1 | Finite context; long agent runs get compacted/summarized; power-user habit = externalize durable state to files (CLAUDE.md). |
| 2 | RAG in one breath | T1 | Embed corpus → retrieve top-K by similarity → stuff into prompt as grounded context. Hybrid = vector + keyword (BM25). Caseway = ES retrieval. |
| 3 | Structured outputs | T1 | Typed JSON contract between steps (Pydantic / function-calling). Covered in Area 1 trust stack — don't re-teach. |
| 4 | Evals | T2 | Offline (test set + LLM-as-judge) + online (monitoring, regression). Deep Core eval is HARD + interesting → expert-validated reference models + geologist acceptance/edit rate. Raising the question = senior signal. |

---

## Lesson 8 — Database / Backend (Area 4)

**Notes file:** [study-plan/backend-databases.md](study-plan/backend-databases.md)
**Goal:** Speak to the data + backend layer of *their* stack as the owner the JD describes ("ownership through the entire stack from the database").

| # | Chunk | Tier | Teach |
|---|---|---|---|
| 1 | Likely architecture | T1 | Next.js (Node) app layer + Python geostat/agent services + Supabase Postgres. Why split: geostats ecosystem is Python. |
| 2 | Supabase = Postgres+ | T1 | Managed Postgres + auth + RLS + storage + realtime. **RLS** = row-level tenant isolation in the DB vs app layer → maps to John's JWT/per-user scoping at Caseway. One smart Q: "RLS or app-layer for tenant isolation?" |
| 3 | Schema + indexing basics | T2 | Normalize sensibly; index the columns you filter/join on; EXPLAIN ANALYZE to find slow queries; B-tree default. pgvector for vectors when already on Postgres. |
| 4 | Long-job persistence | T2 | A 3D model build = a job row (status, params, result ref) + async worker; store large model artifacts in object storage, reference by URL. |

---

## Lesson 9 — React / Next.js (Area 5, HIGH LEVEL ONLY)

**Notes file:** [study-plan/react-nextjs.md](study-plan/react-nextjs.md)
**Goal:** Speak fluently at a high level — John is strong here, this is reflex-refresh, NOT teaching. Do not go deep.

| # | Chunk | Tier | Teach |
|---|---|---|---|
| 1 | Rendering model | T1 | React re-renders on state/prop change; reconciliation/diffing; memoization (useMemo/useCallback/React.memo) only when there's a measured cost. |
| 2 | Server vs Client Components (Next App Router) | T1 | Server Components render on the server (no JS shipped, can fetch directly); Client Components for interactivity/hooks/browser APIs. Default to server; `"use client"` at the leaf. |
| 3 | Data fetching + rendering strategies | T2 | SSR / SSG / ISR / streaming; route handlers + server actions as the backend. When to use which (one line each). |
| 4 | Cesium-in-Next reality | T3 | Cesium is a heavy client-side WebGL engine → must be a Client Component, dynamic-import with `ssr: false`. One-liner only. |

---

## Mock Q&A (Tue, end)

Rapid-fire across all lessons. Grade every answer for **honesty, brevity, energy**. Likely questions: walk me through Caseway's architecture; how do your agents fail + how do you catch it; the cost-optimization story; why founding + why mining; what would you build first here; comp/equity expectations; availability.

---

## Session Log

| Date | Lessons | Weak spots | Next |
|---|---|---|---|
| 2026-06-08 | Scaffolding only | — | Teach L1 (Agentic Orchestration) Chunk 1 |
| 2026-06-08 PM | SCOPE RESHAPE + Area 1 start | Rambling on ReAct vs planner-executor (B-); missed "plan inspectable before execution" trust point | Continue Area 1: trust-stack answer → failure modes → six-beat design → Claude Code internals |
| 2026-06-08 eve | Notes-build: Areas 1,2,3 done + React/Next 1-5 | Caseway-mapping reflex weak; rambling = #1 risk; both → Tue drill | Finish React/Next 6-8 → Area 4 (backend-databases) → Tue: `useDebounce` warm-up + ALL quizzes/mocks |
