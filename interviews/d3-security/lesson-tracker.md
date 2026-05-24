# D3 Security — Lesson Tracker

**This is the teaching content** Claude teaches from during the cram. Topic note files (`study-plan/<topic>.md`) are John's hand-notes scaffolds; this file is the source of truth for *what* gets taught.

---

## Current Position

> **Last completed:** _Nothing yet — cram not started._
> **Up next:** Lesson 1 — AI Engineering Foundations, Chunk 1 (Mon Block 1).
> **Last session date:** _Pre-cram scaffolding only (2026-05-22)._
>
> **Update this section at the END of every teaching session.** Format: `Lesson N — <name>, Chunk K` for last completed; same for next up. Update the session log at bottom too.

---

## How This File Works

1. **Claude teaches from this file**, lesson by lesson, chunk by chunk.
2. **John takes notes in the matching `study-plan/<topic>.md` scaffold** as Claude teaches each chunk.
3. **Between chunks:** Claude asks the chunk's check question; John answers in his own words; Claude confirms or clarifies before moving on.
4. **At end of each lesson:** Claude runs TWO assessments back-to-back —
    - (a) **Cold quiz** — 5-7 questions, no notes, conversational answers
    - (b) **Quick written exercise (<10 min)** — ONE structured-answer prompt in the D3 test format (bullets, pseudo-code, or architecture sketch). Drills the actual test format, not just recall. Claude drafts the prompt at lesson-end when context is fresh.
    - **Storage:** written exercises live in [study-plan/exercises/](study-plan/exercises/) as `lesson-NN-<topic>.md`. Each file has prompt + answer space + grading section + re-drill items. Persistent record across the cram.
5. **End of session:** update Current Position above + add session log entry below + flag any weak spots.

**Granularity rule (locked 2026-05-24):** every chunk taught at one of three tiers — Tier 1 (must know cold, full mechanism), Tier 2 (reason about, no recitation), Tier 3 (mentioned, not drilled). Default to leaner; trim memorization of lists; favor concept fluency. John pushes back if anything drifts toward textbook trivia.

**Resumability rule:** any context window says "let's continue with d3" → read CLAUDE.md → see Current Position pointer here → pick up from the next chunk. No re-teaching unless John flags it.

---

## Day-by-Day Plan (compressed cram)

| Day | Blocks | Lessons |
|---|---|---|
| **Mon (Block 1)** | 1.5h | Lesson 1 — AI Engineering Foundations |
| **Mon (Block 2)** | 2h | Lesson 2 — RAG Deep |
| **Mon (Block 3)** | 1.5h | Lesson 3 — Agents + Tool Use |
| **Mon — daily** | 30-40m | Logic Puzzle Drill — 6 puzzles cold (categories 1-6) |
| **Tue (Block 1)** | 1h | Lesson 4 — Multi-Agent Governance (Light) |
| **Tue (Block 2)** | 1h | Lesson 5 — Prompt Safety Essentials |
| **Tue (Block 3)** | 45m | Lesson 6 — SOC Domain Primer |
| **Tue (Block 4)** | 1h | Lesson 7 — MongoDB Essentials (30m) + Lesson 8 — System Integration LLM (30m) |
| **Tue afternoon** | 90m | **Mock Test #1** (paper, closed-book) → grade → patch weakest |
| **Tue — daily** | 30-40m | Logic Puzzle Drill — 6 puzzles cold (categories 7-10 + replay 2 weakest) |
| **Wed morning** | 1h | Vocab reflex + 1-2 puzzles + 1 architecture sketch + Mock #2 highlights |
| **Wed 3pm** | 2h | **INTERVIEW** at 300-1075 W Georgia St, V6E 3C9 |

---

## Daily Habits (non-negotiable both Mon + Tue)

### Logic Puzzle Drill (~30-40 min per day)

- **6 puzzles per day**, cold attempt first (max 5 min each)
- If stuck: name the CATEGORY + the TRICK before looking up
- Bank lives in `study-plan/logic-puzzles.md` (18 puzzles across 10 categories)
- See logic-puzzles drill protocol section below for daily distribution

### Vocab Reflex Pass (~10 min, end of each day)

- Pull 20 terms from the day's lessons (memorized check)
- Target: <2s recall per term, zero blanks
- Misses go into next day's spaced review

---

## Lesson 1 — AI Engineering Foundations

**Time:** ~1.5h (Mon Block 1)
**Status:** Not started
**Notes file:** [study-plan/ai-engineering-foundations.md](study-plan/ai-engineering-foundations.md)
**Goal:** John can speak authoritatively about production LLM engineering — prompts, structured outputs, streaming, error handling, cost control, model routing, evaluation.

### Chunks

| # | Chunk | ~Time | Teach | Key vocab | Check question |
|---|---|---|---|---|---|
| 1 | System vs user prompts | 8m | Hard boundary; what goes where; tie to prompt caching benefit (stable content = 90% cost discount on cache hits) | system prompt, user prompt, prompt caching, cache hit, stable vs dynamic content | "Where do safety guardrails go, and why?" → System; harder to override + benefits from caching |
| 2 | Production prompt structure | 10m | Role → Task → Context → Instructions → Output Format → Constraints → Examples. Flat monolithic prompts unmaintainable. Optimal 150-300 words. "Lost in the middle" effect. | role assignment, few-shot, zero-shot CoT, "lost in the middle" | "Why is 'lost in the middle' real — and what's the production response?" → Models attend more to start/end; put critical content there |
| 3 | Structured outputs | 12m | Three patterns: prompted (fragile) / native structured (constrained decoding) / tool output. Token-level grammar means model can't emit invalid JSON. Pydantic + Instructor + native APIs. | JSON schema, constrained decoding, Pydantic, Instructor, native structured outputs, tool output | "What does 'constrained at the token level' actually mean?" → Model physically cannot emit tokens that violate schema; eliminates post-hoc parsing failures |
| 4 | Streaming + SSE | 10m | SSE = HTTP-based, stateless, de facto standard. TTFT > total latency for UX. nginx `proxy_buffering off` mandatory. | Server-Sent Events (SSE), EventSource, time-to-first-token (TTFT), proxy buffering | "User reports streaming broken in prod, fine local. Most likely cause?" → Reverse proxy buffering the response (nginx/ALB defaults) |
| 5 | Error handling + fallbacks | 12m | Exponential backoff + jitter (prevent thunder). Respect `Retry-After`. 3-tier fallback hierarchy. Circuit breaker for LLM providers. Graceful degradation menu. | exponential backoff, jitter, Retry-After header, circuit breaker, fallback hierarchy, graceful degradation | "Why does jitter matter for retries?" → Without it, 100 clients retry at same instants → thunder back → AWS research: jitter cuts retry storms 60-80% |
| 6 | Cost control + prompt caching | 12m | 90% input-cost discount on cache hits. Anthropic explicit `cache_control` (~100% hits); OpenAI implicit (~50%). Placement rule: stable first, variable last. Cache writes cost 1.25× or 2.0×. | prompt caching, cache_control, cache hit rate, batch API, max_tokens cap | "Why is Anthropic's caching more reliable than OpenAI's?" → Explicit cache_control parameter = deterministic; OpenAI implicit = best-effort |
| 7 | Model routing / cascading | 10m | Cheap-first → escalate on low confidence or self-consistency disagreement. 85% cost cut potential. Routing decision must be FAST (rules µs, classifier ms, small LLM <200ms). LiteLLM / Portkey / OpenRouter. | model routing, cascading, confidence threshold, self-consistency, LiteLLM | "What's required for '85% cost cut with no quality loss'?" → Fast router + correct confidence detection + clean escalation path |
| 8 | Evaluation in production | 12m | Eval harness as test suite for LLM features. 100-200 production-sampled cases. Track accuracy + latency + cost. A/B testing in prod (Langfuse, LangSmith). Drift detection. | eval harness, RAGAS, A/B testing, drift detection, Langfuse, LangSmith, Arena Elo | "Why does an eval harness matter MORE for agents than single-call features?" → Multi-step compound errors; small per-step quality drops produce big end-to-end failures |

### End-of-Lesson Quiz (5-7 questions, John answers cold)

1. Where do safety guardrails go: system or user prompt? Why? *Answer: System. Harder to override + benefits from prompt caching.*
2. What's the canonical way to prevent retry storms? *Answer: Exponential backoff + random jitter.*
3. What does "constrained at the token level" actually mean for structured outputs? *Answer: Model physically cannot emit tokens that violate the schema; constrained decoding at the token level eliminates post-hoc JSON parsing failures entirely.*
4. User reports streaming feels broken in production though it worked locally. Most likely cause? *Answer: Reverse proxy (nginx, ALB) buffering the response. Need `proxy_buffering off` for SSE routes.*
5. Why is Anthropic's prompt caching more reliable than OpenAI's? *Answer: Anthropic uses explicit `cache_control` parameter for deterministic caching; OpenAI uses implicit/automatic caching with ~50% hit rate.*
6. Cascading model routing — when does the cheap model fail open vs fail closed? *Answer: Fail open (escalate to bigger model) when low confidence or self-consistency disagreement; fail closed (return error) on hard validation failure.*
7. Why does an eval harness matter more for agents than for single-call features? *Answer: Multi-step workflows compound errors; small per-step quality drops produce big end-to-end failures. Need eval to detect regression.*

### Reference URLs (for deeper reading post-interview)

- [Prompt Engineering Best Practices 2026](https://reintech.io/blog/prompt-engineering-best-practices-production-llm-applications)
- [Pydantic AI — Output](https://ai.pydantic.dev/output/)
- [Anthropic Structured Outputs](https://tessl.io/blog/anthropic-brings-structured-outputs-to-claude-developer-platform-making-api-responses-more-reliable/)
- [SSE for LLMs](https://procedure.tech/blogs/sse-for-llms/)
- [Retry Strategies for LLM API Calls](https://callsphere.ai/blog/retry-strategies-llm-api-calls-exponential-backoff-jitter-tenacity/)
- [Anthropic Prompt Caching](https://www.finout.io/blog/anthropic-api-pricing)
- [LLM Routing in Production](https://blog.logrocket.com/llm-routing-right-model-for-requests/)
- [Eval Harness 2026](https://logiciel.io/blog/llm-eval-harness-internal-build-2026)

---

## Lesson 2 — RAG Deep

**Time:** ~2h (Mon Block 2)
**Status:** Not started
**Notes file:** [study-plan/rag-deep.md](study-plan/rag-deep.md)
**Goal:** Formalize and deepen John's existing Caseway RAG knowledge. Add the vocabulary, the trade-off arguments, and the production failure modes interviewers probe.

### Chunks

| # | Chunk | ~Time | Teach | Key vocab | Check question |
|---|---|---|---|---|---|
| 1 | Full RAG pipeline | 15m | Two parallel pipelines: OFFLINE indexing (ingest → chunk → embed → store) + ONLINE querying (query → retrieve → rerank → assemble → generate → cite). Killer fact: **73% of RAG failures are retrieval, not generation.** | RAG, indexing pipeline, querying pipeline | "Where do most RAG failures originate? What's the implication?" → 73% retrieval; spend effort on chunking + retrieval + reranking, not bigger models |
| 2 | Chunking strategies | 15m | Recursive 512-token splitter (LangChain default) with 10-20% overlap is the production default. Beats semantic chunking on most QA benchmarks (~69% vs 54%). Document-aware: code/Markdown/PDF preserve structure boundaries. | recursive character splitting, fixed-size, semantic chunking, document-aware, hierarchical chunking, overlap | "Why is fixed-size chunking the wrong default for production?" → Splits mid-sentence/table/function — retrieves technically-relevant but practically-useless chunks |
| 3 | Embedding model choice | 12m | Defaults: OpenAI text-embedding-3-small (1536 dim, cheap, SOTA). Self-host break-even ~$500/mo API. **Critical: different models = incompatible vectors → re-embed entire corpus on migration.** | text-embedding-3-small, text-embedding-3-large, Cohere embed v3/v4, BGE-M3, E5-Mistral, dimensionality, model migration | "What happens to your corpus when you switch embedding models?" → Vectors incompatible; full re-embed required; plan migrations carefully |
| 4 | Vector store choice | 15m | pgvector (Postgres ext, <10M vectors), Pinecone (managed zero-ops), Qdrant (high throughput), Weaviate (native hybrid), Milvus (massive scale). Caseway uses Elasticsearch — valid (search engine that added vector). | pgvector, Pinecone, Qdrant, Weaviate, Milvus, HNSW, IVF | "Recommend pgvector vs Pinecone for 5M vectors on a Postgres-based product." → pgvector — same DB = transactional consistency, single backup, no cross-system sync, well within range |
| 5 | Retrieval techniques | 15m | Pure vector ~78% recall@10. Pure BM25 ~65%. Hybrid + RRF ~91%. **RRF = Reciprocal Rank Fusion: merge ranked lists by position, not score** (formula: Σ 1/(k + rank), k=60). Native in ES, OpenSearch, Qdrant, Weaviate. | BM25, hybrid search, Reciprocal Rank Fusion (RRF), HNSW, recall@k, MRR | "You're at 78% recall@10 with pure vector. Single biggest lever?" → Hybrid (BM25 + vector with RRF); typically jumps to 91% |
| 6 | Reranking | 10m | Cross-encoder reranker after retrieval (top 50-100 → top 5-10 for LLM). Cohere Rerank 3, Voyage Rerank-2, BGE-Reranker-v2. **10-30% precision lift at 50-100ms latency.** Why cross-encoders win: query + doc through one model = better signal. | cross-encoder, bi-encoder, Cohere Rerank, BGE-Reranker, two-stage retrieval | "After hybrid + RRF, what's the next-highest-ROI addition?" → Cross-encoder reranking; +10-30% precision for 50-100ms latency |
| 7 | Context assembly + citations | 10m | Dedup near-duplicates (cosine > 0.95). Order by relevance — most-relevant at start AND end (combat lost-in-the-middle). Citations mandatory for regulated domains. Handle "no relevant context" with explicit "I don't know" — don't hallucinate. | citation, deduplication, lost-in-the-middle, "I don't know" fallback | "If retrieval returns no relevant chunks, what should production RAG do?" → Return "I don't have enough information to answer" — never let LLM hallucinate |
| 8 | RAG evaluation | 15m | 5 metrics: faithfulness (answer grounded?), answer relevancy (addresses query?), context precision (chunks relevant?), context recall (got everything?), recall@k/MRR. RAGAS framework. Targets: faithfulness >0.8, answer relevancy >0.8, context precision >0.7. | faithfulness, answer relevancy, context precision, context recall, recall@k, MRR, RAGAS, DeepEval, TruLens | "What does RAGAS measure WITHOUT ground truth labels?" → Faithfulness, answer relevancy, context precision (all via LLM-as-judge) |
| 9 | Advanced patterns | 13m | Query rewriting (spelling, expansion, multi-query). **HyDE** (Hypothetical Document Embeddings) — embed a hypothetical answer not the question; +10-30% recall. **Parent-document retrieval** — index small chunks, return parent for context. | HyDE, query rewriting, multi-query, parent-document retrieval, query decomposition | "Explain HyDE in one sentence." → Generate a hypothetical answer, embed THAT instead of the question; answer-text matches answer-text better than question-text matches answer-text |

### End-of-Lesson Quiz

1. Where do most RAG failures come from, retrieval or generation? *Answer: 73% retrieval; spend engineering effort there.*
2. Production default for chunking? *Answer: Recursive character splitter, ~512 tokens, 10-20% overlap.*
3. What happens to your corpus when you switch embedding models? *Answer: Vectors are incompatible — must re-embed entire corpus.*
4. Pure vector gives 78% recall@10. Biggest single lever? *Answer: Hybrid search (BM25 + vector + RRF) → ~91%.*
5. After hybrid retrieval, what's the next ROI move? *Answer: Cross-encoder reranking; +10-30% precision, 50-100ms latency.*
6. What does faithfulness measure? *Answer: Does the answer use ONLY retrieved context (no hallucination).*
7. Explain HyDE in one sentence. *Answer: Generate a hypothetical answer to the user query, embed that hypothetical answer (not the question), retrieve docs similar to it — answer-text matches answer-text better than question-text matches answer-text.*

### Reference URLs

- [RAG in Production 2026](https://www.abhs.in/blog/rag-in-production-chunking-retrieval-cost-developers-2026)
- [Best Chunking Strategies](https://www.firecrawl.dev/blog/best-chunking-strategies-rag)
- [Embedding Models Comparison 2026](https://reintech.io/blog/embedding-models-comparison-2026-openai-cohere-voyage-bge)
- [Hybrid Search with RRF](https://ashutoshkumars1ngh.medium.com/hybrid-search-done-right-fixing-rag-retrieval-failures-using-bm25-hnsw-reciprocal-rank-fusion-a73596652d22)
- [RAGAS for RAG Evaluation](https://dkaarthick.medium.com/ragas-for-rag-in-llms-a-comprehensive-guide-to-evaluation-metrics-3aca142d6e38)
- [HyDE and Multi-Query RAG](https://medium.com/@mudassar.hakim/retrieval-is-the-bottleneck-hyde-query-expansion-and-multi-query-rag-explained-for-production-c1842bed7f8a)

---

## Lesson 3 — Agents + Tool Use

**Time:** ~1.5h (Mon Block 3)
**Status:** Not started
**Notes file:** [study-plan/agents-and-tool-use.md](study-plan/agents-and-tool-use.md)
**Goal:** Most D3-relevant lesson — Morpheus is an autonomous security operations agent. Discuss agent patterns + failure modes + governance with authority.

### Chunks

| # | Chunk | ~Time | Teach | Key vocab | Check question |
|---|---|---|---|---|---|
| 1 | Single call vs agent loop | 10m | **Default = single call with structured output.** Agent loop only when dynamic discovery / course-correction needed. Token cost grows O(n²); by turn 30, 25-35k accumulated context per request. | single-call LLM, agent loop, context window explosion, cost compounding | "When should you choose a single LLM call over an agent loop?" → When answer shape is known + no tool calls + latency matters; default single, reach for agent only for dynamic discovery |
| 2 | ReAct pattern | 12m | Thought → Action → Observation loop. Transparent + adaptive. **4 failure modes:** infinite loops, hallucinated tool calls, long-horizon decay (~60% success at 10 steps), silent 200s with junk. | ReAct, thought-action-observation, infinite loop, hallucinated tool call, long-horizon decay | "Name the 4 failure modes of ReAct agents." → Infinite loops, hallucinated tool calls, long-horizon decay, silent 200s with junk payload |
| 3 | Plan-and-execute | 8m | Plan upfront → execute deterministically. **~40% cheaper than ReAct.** Natural HITL gate at plan-review step. When ReAct: real-time dynamic. When P&E: production SLAs, regulated, multi-step coding. | plan-and-execute, deterministic execution, HITL gate, replanning | "Why is plan-and-execute ~40% cheaper than ReAct?" → One big planning round vs replan-each-step; fewer total LLM calls; plan = single HITL gate vs N gates |
| 4 | Reflection / self-critique | 8m | Generate → evaluate → revise. Reflexion (verbal memory), critic agent, self-refine. Quality lift without multi-model cost. Production-common for high-stakes outputs. | Reflexion, critic agent, self-refine, Process Reward Model (PRM), self-consistency | "When does reflection help most?" → High-stakes outputs (security verdicts, legal) where quality matters more than latency |
| 5 | Function calling / tool use | 12m | Provider landscape: OpenAI/Anthropic/Gemini all 95-99% tool selection. JSON schema for tool definitions. **Parallel tool calls cut latency 60-70%.** Schema discipline (descriptions, required vs optional, strict types) prevents hallucinated args. Without guardrails: 20-40% success. With: 70-80%+. | function calling, tool use, parallel tool calls, tool_choice (auto/required/specific), schema validation | "Tool selection accuracy without guardrails vs with?" → Without: 20-40%; with (schema validation + retries + dedup): 70-80%+ |
| 6 | MCP (Model Context Protocol) | 8m | Open standard for LLM ↔ tool integration. Donated to Linux Foundation Dec 2025. 97M monthly SDK downloads. 5,800+ community servers. "USB-C of AI integration." Standardized audit trails. | MCP, Linux Foundation, MCP server, tool discovery, standardized audit | "What does MCP standardize, and why does that matter for governance?" → Tool discovery + call format + audit-trail format; centralized governance can audit any tool call regardless of provider |
| 7 | Multi-agent orchestration | 12m | 4 patterns: supervisor (delegate to specialists), pipeline (sequential), swarm (parallel autonomous), hierarchical (multi-level). **Killer failure mode: CONTEXT INCONSISTENCY** (agents don't share state, step on each other). Mitigation: shared state store, explicit handoffs. | supervisor pattern, pipeline, swarm, hierarchical, context inconsistency, agent handoff | "What's the canonical multi-agent failure mode?" → Context inconsistency — agents don't share state, step on each other |
| 8 | Agent frameworks 2026 | 8m | **LangGraph (regulated/auditable — graph-based state machine)**; CrewAI (fast prototyping, role-based); AutoGen/AG2 (maintenance mode); Anthropic Agent SDK (Claude-native, MCP integration). LangGraph surpassed CrewAI on GitHub stars in 2026. | LangGraph, CrewAI, AutoGen, AG2, Anthropic Agent SDK, LangSmith | "Which framework would you recommend for Morpheus? Why?" → LangGraph — graph-based architecture maps to audit trails, checkpointing, rollback points — required for regulated security workflows |
| 9 | HITL + tiered autonomy | 12m | Two HITL flavors: approval gate (binary) or collaborative edit. Identity-aware orchestration: pause → authorized human → time-boxed window → log. **Tiered autonomy:** Tier 1 = auto-action (high conf, low risk); Tier 2 = HITL approval (mid); Tier 3 = full analyst review (low conf OR destructive). RBAC enforces who can approve what. | HITL, approval gate, collaborative edit, identity-aware orchestration, tiered autonomy, RBAC | "Map Morpheus Tier 1/2/3 to autonomy tiers + HITL patterns." → T1 high-conf low-risk = auto; T2 mid = HITL approval; T3 low-conf or destructive = full review; RBAC enforces approver authority |
| 10 | Production gotchas + security | 12m | Token cost explosion (hard budgets). Infinite retry loops (max-step + loop detection). Hallucinated tool calls (strict schema). **Security:** prompt injection through tool output ("equivalent to letting every GitHub user shell access"). Mitigations: isolate system prompts from user/tool input, input validation, output filtering, least-privilege tool access, separate creds per tier. | prompt injection via tools, system prompt isolation, least privilege, output filtering, max-step budget | "Why is 'isolate system prompts from user/tool input' a security requirement?" → Prompt injection through tool output can chain across tools, exfiltrate data, hijack planning — equivalent to letting untrusted users edit your prompt template |

### End-of-Lesson Quiz

1. When should you choose a single LLM call over an agent loop? *Answer: Known answer shape + no tool calls + latency matters. Default single; reach for agent only for dynamic discovery.*
2. Name the 4 failure modes of ReAct agents. *Answer: Infinite loops, hallucinated tool calls, long-horizon decay (~60% at 10 steps), silent 200s with junk.*
3. Why is plan-and-execute ~40% cheaper than ReAct? *Answer: One big planning round vs replan-each-step; fewer total LLM calls; plan = single HITL gate.*
4. Canonical multi-agent failure mode? *Answer: Context inconsistency — agents don't share state, step on each other.*
5. Recommend a framework for Morpheus and defend. *Answer: LangGraph — graph-based architecture = auditable + checkpointable + resumable; essential for regulated security workflows.*
6. What does MCP standardize and why does that matter for governance? *Answer: Tool discovery + call format + audit trail format. Centralized governance layer can audit any tool call regardless of LLM provider.*
7. Why is "isolate system prompts from user/tool input" a security requirement, not a best practice? *Answer: Prompt injection through tool output chains across tools, exfiltrates data, hijacks planning. The system-prompt boundary IS the trust boundary.*
8. Map Tier 1/2/3 autonomy to Morpheus. *Answer: T1 = high-confidence low-risk = auto-action; T2 = mid = HITL approval; T3 = low-confidence OR destructive = full analyst review; RBAC enforces approver authority.*

### Reference URLs

- [Function Calling 2026 Guide](https://ofox.ai/blog/function-calling-tool-use-complete-guide-2026/)
- [ReAct Framework](https://www.lowtouch.ai/what-is-react-in-agentic-ai-reasoning-acting-framework/)
- [LangGraph vs CrewAI vs AutoGen 2026](https://medium.com/data-science-collective/langgraph-vs-crewai-vs-autogen-which-agent-should-you-actually-use-in-2026-b8b2c84f1229)
- [MCP Complete Guide 2026](https://www.essamamdani.com/blog/complete-guide-model-context-protocol-mcp-2026)
- [HITL Patterns](https://www.strata.io/blog/agentic-identity/practicing-the-human-in-the-loop/)
- [Prompt Injection Agentic Amplification](https://christian-schneider.net/blog/prompt-injection-agentic-amplification/)

---

## Lesson 4 — Multi-Agent Governance (Light)

**Time:** ~1h (Tue Block 1)
**Status:** Not started
**Notes file:** [study-plan/multi-agent-governance-light.md](study-plan/multi-agent-governance-light.md)
**Goal:** Discuss governance in your own words — NOT recite NIST/OWASP/TRiSM lists. Concept-level fluency.

### Chunks

| # | Chunk | ~Time | Teach | Key vocab | Check question |
|---|---|---|---|---|---|
| 1 | What "governance" means for an agentic system | 15m | Governance = the policies, controls, and traceability that make autonomous systems SAFE to deploy. Not about restricting agents — about making them auditable + correctable + accountable. Three pillars: WHAT they can do, WHO approves, HOW you trace. | governance, autonomy, accountability, traceability | "Define governance for an agentic system in one sentence — your words." → Policies + controls + traceability that make autonomous systems safe to deploy = auditable, correctable, accountable |
| 2 | Role boundaries + HITL | 15m | Each agent has explicit role + permissions. Enrichment agent can't take destructive action. Response agent can't modify detection rules. HITL where: irreversible actions, low confidence, high-risk operations. Identity-aware (RBAC). | role boundary, least privilege, HITL, identity-aware orchestration, approval gate | "Why are role boundaries part of governance, not just clean architecture?" → Boundaries prevent capability creep and limit blast radius of compromise/hallucination; auditable separation of concerns |
| 3 | Audit trails + accountability | 15m | Every agent decision logged: timestamp, agent ID + version, inputs, tool calls + args, outputs, confidence, HITL approvals (if any), policy violations triggered. Async log sink — never blocks. Used for: incident investigation, compliance, drift detection, training data. | audit trail, observability, compliance, decision logging, post-incident investigation | "An agent hallucinated a tool call. What 5 fields in your audit trail help investigate?" → timestamp, agent ID + version, tool name + args, tool result, confidence score, HITL gate state, prompt hash |
| 4 | Escalation policies + tiered autonomy | 15m | Map (confidence, risk) → tier → who approves. Time-boxed decision windows (30 min low-risk, 5 min emergency). Define what gets auto-escalated when (timeout, low confidence, novel scenario). | tiered autonomy, escalation policy, time-boxed approval, RBAC | "How do you decide what gets auto-action vs HITL?" → Map (confidence × risk) → tier; high conf + low risk = auto; mid = HITL approval; low conf OR destructive = full review |

### End-of-Lesson Quiz

1. Define governance for an agentic system in your own words. *Answer: Policies + controls + traceability that make autonomous systems safe to deploy — auditable, correctable, accountable.*
2. Why are role boundaries a governance concern, not just architecture? *Answer: Limit blast radius of hallucination or compromise; auditable separation of concerns.*
3. 5 audit-trail fields critical for investigating an agent's bad tool call. *Answer: timestamp, agent ID + version, tool name + args, result/error, confidence score, HITL gate state, prompt hash.*
4. How do you decide auto-action vs HITL? *Answer: Map (confidence × risk) → tier; high conf + low risk = auto; mid = HITL approval; low or destructive = full review.*
5. Why time-box approval windows? *Answer: Prevent stale decisions; force escalation when humans don't respond; auditable accountability.*

---

## Lesson 5 — Prompt Safety Essentials

**Time:** ~1h (Tue Block 2)
**Status:** Not started
**Notes file:** [study-plan/prompt-safety-essentials.md](study-plan/prompt-safety-essentials.md)
**Goal:** 4-5 concepts you can discuss in your own words. NOT OWASP-list memorization.

### Chunks

| # | Chunk | ~Time | Teach | Key vocab | Check question |
|---|---|---|---|---|---|
| 1 | Prompt injection | 15m | Attacker embeds instructions in user input or tool output → LLM follows them instead of your system prompt. **#1 LLM risk every year since 2023.** Direct (in user input) vs indirect (in retrieved content / tool output). Why it's so hard: LLMs can't distinguish "instructions" from "data" — it's all just text. | prompt injection, direct vs indirect, jailbreak, instruction following | "Why is prompt injection hard to fully prevent?" → LLMs can't distinguish "instructions" from "data" — both are just text tokens; trust boundary must be enforced externally |
| 2 | Jailbreak + system prompt leakage | 12m | Jailbreak = bypass safety guardrails (DAN, role-play, "ignore previous"). System prompt leakage = trick model into revealing its system prompt → attackers can craft targeted attacks. Both are sub-categories of prompt injection. | jailbreak, DAN, role-play attack, system prompt leakage, refusal | "Distinguish jailbreak from prompt injection." → Prompt injection = make LLM follow attacker's instructions; jailbreak = specifically bypass safety guardrails. Jailbreak is one type of prompt injection |
| 3 | Output validation | 15m | Don't trust LLM output — validate before downstream use. Patterns: LLM-as-judge (second LLM evaluates), schema enforcement, content filters, rule-based checks. Llama Guard, ShieldGemma, IBM Granite Guardian. | LLM-as-judge, output filter, content moderation, schema enforcement, Llama Guard, ShieldGemma | "Why is LLM-as-judge a common pattern for safety?" → Cost-effective second-opinion on first LLM's output; catches policy violations + hallucinations that downstream systems would otherwise propagate |
| 4 | Defense-in-depth as a principle | 15m | No single defense is enough. Stack: input validation → system prompt isolation → LLM call → output filter → execution sandbox → continuous monitoring. Each layer catches what others miss. **Trust boundary is at every layer crossing.** | defense-in-depth, trust boundary, layered security, monitoring | "Explain defense-in-depth for an LLM-powered API in 30 seconds." → Stack of independent defenses; input validation + system-prompt isolation + LLM + output filter + sandbox + monitoring; each layer catches what others miss; assumes any single layer can fail |

### End-of-Lesson Quiz

1. Why is prompt injection hard to fully prevent? *Answer: LLMs can't distinguish instructions from data; both are tokens. Trust boundary must be enforced externally.*
2. Distinguish jailbreak from prompt injection. *Answer: Prompt injection = make LLM follow attacker's instructions; jailbreak specifically bypasses safety guardrails. Jailbreak is a type of prompt injection.*
3. Why is LLM-as-judge a common safety pattern? *Answer: Cost-effective second-opinion on first LLM's output; catches policy violations + hallucinations.*
4. Explain defense-in-depth for an LLM API in 30 seconds. *Answer: Stack of independent defenses — input validation + system-prompt isolation + LLM + output filter + sandbox + monitoring — each catches what others miss; assumes any single layer can fail.*
5. Which two prompt-safety controls would you put BEFORE the LLM call and which AFTER? *Answer: Before: input validation, prompt-injection detection. After: output filter / LLM-as-judge, schema enforcement.*

---

## Lesson 6 — SOC Domain Primer

**Time:** ~45m (Tue Block 3)
**Status:** Not started
**Notes file:** [study-plan/soc-domain-primer.md](study-plan/soc-domain-primer.md)
**Goal:** Engage credibly about Morpheus + the SOC space. Not deep — enough to discuss intelligently.

### Chunks

| # | Chunk | ~Time | Teach | Key vocab | Check question |
|---|---|---|---|---|---|
| 1 | What an ASOC is | 8m | Autonomous Security Operations Center — agentic AI handles threat detection, investigation, response that human analysts traditionally do. Amplifies analyst capability; humans focus on hunting + strategy. | ASOC, SOC, autonomous AI, agentic security | "Define ASOC in one sentence." → Operating model where agentic AI handles threat detection/investigation/response instead of human analysts manually triaging each alert |
| 2 | SOC tiers T1/T2/T3 | 10m | T1 = alert triage (legit vs false positive, enrich, escalate). T2 = deep investigation + response (correlate, contain, malware analysis, remediation). T3 = threat hunting + strategy (proactive, vulnerability assessment, detection optimization). | T1 analyst, T2 analyst, T3 analyst, alert triage, threat hunting, incident response | "Map T1/T2/T3 to Morpheus's stated value prop ('Tier 1-3 automation')." → Morpheus claims automation across all 3 tiers — auto-triage (T1), auto-investigate + recommend response (T2), auto-hunt and optimize detection (T3) |
| 3 | Morpheus positioning | 10m | D3's autonomous SOC platform. Triages 100% alerts in <3 min. **L2-depth investigations.** 800+ integrations. RSA 2025 launch. 24 months / 60 specialists. "No per-alert fees, no token billing" = key differentiator. | Morpheus, ASOC, RSA, alert triage at scale, autonomous investigation | "What's Morpheus's pricing-model differentiator and why does it matter?" → No per-alert / no token billing → predictable cost at scale, vs competitors charging per-alert |
| 4 | Competitive landscape | 10m | **Torq** (HyperSOC + Socrates, 95% T1 auto). **Tines** (no-code workflow, general automation, no native investigation). **Dropzone AI** (narrow T1 investigation, 100+ enterprise). **Prophet Security** (agent-based, replaces static playbooks). Distinction: agentic platforms (autonomous reasoning) vs workflow builders (faster static playbooks). | Torq, Tines, Dropzone AI, Prophet Security, agentic vs workflow | "What separates Morpheus from Tines?" → Tines = no-code workflow builder (you write playbooks); Morpheus = autonomous agent that generates playbooks at runtime. Tines accelerates legacy playbook construction; Morpheus replaces it |
| 5 | Key vocab (SIEM, SOAR, EDR, MDR, XDR) | 7m | SIEM = Security Information & Event Management (log aggregation + correlation). SOAR = Security Orchestration, Automation, Response (playbook automation). EDR = Endpoint Detection & Response. MDR = Managed Detection & Response (outsourced SOC). XDR = Extended Detection & Response (multi-source). | SIEM, SOAR, EDR, MDR, XDR | "What's the difference between SOAR and an ASOC?" → SOAR = automate playbooks YOU write; ASOC = AI generates + executes playbooks autonomously |

### End-of-Lesson Quiz

1. Define ASOC in one sentence. *Answer: Operating model where agentic AI handles threat detection/investigation/response instead of human analysts manually triaging each alert.*
2. What does each SOC tier do? *Answer: T1 = triage; T2 = investigate + respond; T3 = hunt + optimize.*
3. What's Morpheus's pricing-model differentiator? *Answer: No per-alert fees, no token billing → predictable cost at scale.*
4. Distinguish Morpheus from Tines. *Answer: Tines = no-code workflow builder (you write playbooks); Morpheus = autonomous agent that generates playbooks at runtime.*
5. SOAR vs ASOC? *Answer: SOAR = automate playbooks YOU write; ASOC = AI generates + executes playbooks autonomously.*

---

## Lesson 7 — MongoDB Essentials

**Time:** ~30m (Tue Block 4, first half)
**Status:** Not started
**Notes file:** [study-plan/mongodb-essentials.md](study-plan/mongodb-essentials.md)
**Goal:** Practical-discussion-level. Vocab + aggregation + indexes.

### Chunks

| # | Chunk | ~Time | Teach | Key vocab | Check question |
|---|---|---|---|---|---|
| 1 | Core vocabulary | 5m | Document (JSON-like) → Collection (table equivalent). BSON (binary JSON, allows binary + ObjectId + datetime). ObjectId (12-byte auto-ID, encodes timestamp). Embedded (sub-docs in parent) vs Referenced (foreign-key). Denormalize-first culture. | document, collection, BSON, ObjectId, embedded, referenced, denormalization | "Embed vs reference — when each?" → Embed when frequently co-accessed (1:few); reference when many-to-many or large sub-docs |
| 2 | Aggregation pipeline | 8m | Stages: $match (filter), $project (reshape), $group (aggregate), $lookup (join), $unwind (flatten arrays), $sort, $limit. $match FIRST for early filtering. $lookup is expensive. | aggregation pipeline, $match, $group, $project, $lookup, $unwind, $sort | "Why put $match first in an aggregation pipeline?" → Early filtering = smaller dataset flowing through later stages = faster |
| 3 | Indexes + ESR rule | 8m | Index types: single field, compound, multikey (array fields), text (full-text), geospatial, TTL (auto-delete). **ESR rule for compound indexes:** Equality fields → Sort fields → Range fields. Covered query = index has all needed fields. | single-field index, compound index, multikey, ESR rule, covered query, index intersection | "What's the ESR rule and why does the order matter?" → Equality, Sort, Range — equality eliminates the most docs first; sort uses index ordering; range last because it scans |
| 4 | Sharding + replicas | 5m | **Replica set** = 1 primary + N secondaries; failover automatic. **Sharding** = horizontal partition via shard key + mongos router. Hashed shard key avoids hotspots; range-based gives fast range queries but hotspots on monotonic keys. | replica set, primary, secondary, sharding, shard key, hashed vs range-based, mongos | "Hashed vs range-based shard key — when each?" → Hashed = even writes (no hotspots, slow ranges); range = fast range queries but hotspots on monotonic keys |
| 5 | When MongoDB vs Postgres | 4m | **Mongo wins:** flexible schema, rapid iteration, embedding-friendly data, horizontal scale. **Postgres wins:** complex queries, joins, ACID across entities, ad-hoc analytics. Most teams start Postgres, move to Mongo for specific workloads. | flexible schema, ACID, horizontal scale, polyglot persistence | "Recommend Mongo or Postgres for a security event log with high write throughput?" → Mongo — flexible schema (different event types), horizontal scale via sharding, time-series friendly with TTL indexes |

### End-of-Lesson Quiz

1. Embed vs reference — when each? *Answer: Embed when 1:few and frequently co-accessed; reference for many-to-many or large sub-docs.*
2. Why put $match first in aggregation? *Answer: Early filtering = smaller dataset flowing through later stages = faster.*
3. What's the ESR rule? *Answer: Compound index field order: Equality, Sort, Range. Equality first eliminates most docs.*
4. Hashed vs range-based shard key trade-offs? *Answer: Hashed = even writes, slow ranges; range = fast range queries, hotspots on monotonic keys.*
5. Mongo vs Postgres for security event logs? *Answer: Mongo — flexible schema for different event types, horizontal scale via sharding, time-series friendly.*

---

## Lesson 8 — System Integration (LLM)

**Time:** ~30m (Tue Block 4, second half)
**Status:** Not started
**Notes file:** [study-plan/system-integration-llm.md](study-plan/system-integration-llm.md)
**Goal:** Synthesis — how production AI features assemble. Lean heavily on existing system design notes.

### Chunks

| # | Chunk | ~Time | Teach | Key vocab | Check question |
|---|---|---|---|---|---|
| 1 | LLM reference architecture | 10m | Client (web/mobile) → API gateway (auth, rate limit) → backend service → LLM API + tools + RAG context → response (streaming SSE) → observability sidechannel. Each layer = standard service patterns. | API gateway, LLM service, tool router, RAG context, streaming, observability sidechannel | "Walk me through the reference architecture for an LLM-powered chat product, layer by layer." → Client → API gateway → backend → LLM with retrieved context + tool calls → streaming response → audit log |
| 2 | Where existing sysdesign concepts apply | 10m | **Rate limiting** at API gateway (same as Remitly). **Idempotency** for write operations from agent (Idempotency-Key header). **Async queues** for background LLM jobs (batch eval, long-running agent runs). **Circuit breaker** for LLM provider failures. All from existing sysdesign notes. | rate limiting, idempotency, async queue, circuit breaker | "Name 3 existing system design concepts that apply directly to LLM apps." → Rate limiting (API gateway), idempotency (write operations), circuit breaker (LLM provider failures) — all from `02-system-design/notes/` |
| 3 | LLM-specific observability | 10m | Beyond standard logs/metrics/traces: per-call cost (token in/out × price), faithfulness/eval scores, drift metrics, hallucination rate. LangSmith, Langfuse, SigNoz for traces. Aggregate cost per user/session/feature. | cost per call, faithfulness metric, drift, LangSmith, Langfuse, SigNoz, eval pipeline | "What 4 LLM-specific metrics would you add to your observability stack?" → Per-call cost (token × price), faithfulness/eval score, drift metric (eval over time), hallucination rate |

### End-of-Lesson Quiz

1. Walk the reference architecture for a production LLM app, layer by layer. *Answer: Client → API gateway (auth, rate limit) → backend → LLM API (with RAG context + tool calls) → streaming SSE response → audit log sidechannel.*
2. Name 3 existing system design concepts that apply directly to LLM apps. *Answer: Rate limiting, idempotency, circuit breaker (all from existing `02-system-design/notes/`).*
3. 4 LLM-specific metrics to add to observability. *Answer: Per-call cost, faithfulness score, drift over time, hallucination rate.*

---

## Logic Puzzle Drill Protocol

See [study-plan/logic-puzzles.md](study-plan/logic-puzzles.md) for the 18-puzzle bank + drill instructions.

**Daily distribution (don't grind one category in a row):**

- **Mon AM (3 puzzles, 15-20 min):** P1.1 weighing (binary), P2.1 average speed, P3.1 bridge crossing
- **Mon PM (3 puzzles, 15-20 min):** P4.1 two doors, P5.1 Monty Hall, P6.1 sock drawer
- **Tue AM (3 puzzles, 15-20 min):** P7.1 100 prisoners, P8.1 sub-sequence trap, P10.1 clock overlaps
- **Tue PM (3 puzzles, 15-20 min):** P9.1 cube faces + replay 2 weakest categories from Mon

Reflex check Wed morning: 5 puzzles speed-run, <2 min total, just name the trick (not full solve).

---

## Mock Test Schedule

Full content + answer keys: [study-plan/mock-test.md](study-plan/mock-test.md)

- **Mock #1** — Tuesday afternoon (after all 8 lessons taught), 90 min closed-book paper. Grade against rubric. Pass bar 75%.
- **Mock #2** — Wednesday morning, 75 min compressed, new question set, tougher curveballs.

**Failure mode:** below 70% on Mock #1 → Tuesday-evening re-cram of 2 weakest topic notes; then retry failed questions Wed morning.

---

## Session Log

Update after every teaching session. Format: date | lessons covered | chunks completed | weak spots flagged | next session start.

| Date | Lessons | Chunks | Weak spots | Next session |
|---|---|---|---|---|
| _ | _ | _ | _ | _ |
