# Mock Test — D3 AI Engineer Written Test Simulation

**Format mirrors D3's actual test:** Multi-select choice questions (Part 1) + Short structured answers (Part 2). Closed-book, paper, no laptop, no Claude.

**Two sittings:**
- **Mock #1** — Tuesday afternoon, full 90 min
- **Mock #2** — Wednesday morning, compressed 75 min

Score yourself against the answer keys. Pass bar: 75%.

---

## Mock #1 — Tuesday Afternoon (90 min)

### Part A — Multi-Select (45 min, 15 questions)

Some have ONE correct answer; some have multiple. Read each carefully. **Select ALL that apply.**

**Q1.** In a production LLM system using prompt caching, which of the following SHOULD go in the system prompt?
- [ ] A) Role definition ("You are a security analyst")
- [ ] B) The current user's question
- [ ] C) Output format specification (JSON schema)
- [ ] D) Hard rules ("never call destructive tools without HITL approval")
- [ ] E) Per-request retrieved RAG context

**Q2.** Why is exponential backoff with JITTER preferred over plain exponential backoff?
- [ ] A) Jitter improves the model's quality
- [ ] B) Jitter prevents synchronized retry storms
- [ ] C) Jitter is required by HTTP spec
- [ ] D) Jitter reduces load on the rate-limited service during recovery

**Q3.** Which retrieval strategy gives ~91% recall@10 in typical RAG benchmarks (vs ~78% for pure vector)?
- [ ] A) Pure BM25 keyword search
- [ ] B) Pure vector with HNSW
- [ ] C) Hybrid (vector + BM25) with Reciprocal Rank Fusion (RRF)
- [ ] D) Cross-encoder reranking alone

**Q4.** Which are valid reasons to choose pgvector over a dedicated vector DB?
- [ ] A) You're already running Postgres
- [ ] B) You need <10M vectors
- [ ] C) You want zero ops overhead (managed service)
- [ ] D) Transactional consistency with your relational data matters
- [ ] E) You need >100M vectors

**Q5.** ReAct agent loops are known to fail in which ways? (select all that apply)
- [ ] A) Infinite loops (repeating the same action)
- [ ] B) Hallucinated tool calls (invented function names)
- [ ] C) Long-horizon decay (~60% success at 10 steps)
- [ ] D) Silent 200 responses (tool returns success with junk payload)
- [ ] E) Reduced model parameter count

**Q6.** "Multi-agent governance" most directly involves which of the following?
- [ ] A) Quantum-resistant encryption
- [ ] B) Role boundaries between agents
- [ ] C) Human-in-the-loop (HITL) checkpoints
- [ ] D) Audit trails of agent actions
- [ ] E) GPU memory allocation

**Q7.** Prompt injection through tool output is dangerous because:
- [ ] A) It can cause the agent to skip validation steps
- [ ] B) It can chain across multiple tool calls
- [ ] C) It can exfiltrate data via subsequent tool calls
- [ ] D) It bypasses HTTPS encryption
- [ ] E) It can hijack agent planning

**Q8.** The MongoDB ESR rule for compound indexes orders fields as:
- [ ] A) Sort, Range, Equality
- [ ] B) Equality, Sort, Range
- [ ] C) Range, Equality, Sort
- [ ] D) Equality, Range, Sort

**Q9.** Which is TRUE about MongoDB single-table vs Postgres relational design?
- [ ] A) MongoDB supports JOINs natively at the same speed as Postgres
- [ ] B) MongoDB encourages embedding related data; Postgres encourages normalization
- [ ] C) Postgres can replace MongoDB for high-throughput key-value workloads
- [ ] D) MongoDB schemas are enforced at the database level by default

**Q10.** Which of the following SHOULD trigger a HITL checkpoint in an autonomous SOC agent?
- [ ] A) Auto-suppressing a low-confidence known false positive
- [ ] B) Quarantining a customer endpoint
- [ ] C) Pushing a new firewall rule to production
- [ ] D) Logging a metric to CloudWatch
- [ ] E) Disabling a user account

**Q11.** "Lost in the middle" refers to which LLM behavior?
- [ ] A) Models forget content placed at start of context
- [ ] B) Models attend less to information in the middle of long context
- [ ] C) Models lose memory between API calls
- [ ] D) Models confuse tool descriptions when too many are provided

**Q12.** Faithfulness in RAG evaluation measures:
- [ ] A) How fast the system responds
- [ ] B) Whether the answer addresses the original query
- [ ] C) Whether every claim in the answer is grounded in retrieved context
- [ ] D) The diversity of retrieved chunks

**Q13.** Which weighing puzzle approach uses BINARY ENCODING?
- [ ] A) Divide coins into thirds, weigh two groups on a balance
- [ ] B) Take 1 coin from pile 1, 2 from pile 2, ..., 10 from pile 10
- [ ] C) Weigh each pile individually
- [ ] D) Use coins from sequential piles in powers of 2

**Q14.** An LLM application returns invalid JSON ~5% of the time. What's the MOST effective fix?
- [ ] A) Add "Please return valid JSON" to the prompt
- [ ] B) Use native structured outputs / JSON mode with a schema
- [ ] C) Add try/except around the JSON parser
- [ ] D) Use a larger model
- [ ] E) Increase max_tokens

**Q15.** A user reports streaming feels broken in your prod deployment though it works locally. Most likely cause?
- [ ] A) The LLM provider is rate-limiting
- [ ] B) Reverse proxy (nginx, ALB) buffering the response
- [ ] C) Browser cache misconfiguration
- [ ] D) Wrong API key

---

### Part B — Short Structured Answers (45 min, 4 questions)

**Q16.** (12 min) Sketch the architecture of an autonomous SOC alert-triage pipeline. Include: alert ingestion, triage agent, enrichment tools, investigation step, HITL gate, response action, audit log. Show where guardrails / prompt-safety controls live. Brief annotation on each component.

_Your answer:_

---

**Q17.** (10 min) Write pseudo-code for a tool-calling LLM workflow that includes:
- Schema validation of tool arguments
- Retry on tool failure (exponential backoff + jitter, max 3 retries)
- Fallback to a cached response if all retries fail
- Audit log entry per tool call

_Your answer:_

---

**Q18.** (10 min) Compare LangGraph vs CrewAI for building Morpheus's autonomous SOC agent. Pick one and defend the choice with 3 specific reasons tied to the SOC use case.

_Your answer:_

---

**Q19.** (13 min) List 4 prompt-injection defenses, ranked by effectiveness for a security agent that ingests untrusted alert text. Include one drawback per defense.

_Your answer:_

---

## Mock #1 — Answer Key

### Part A

| Q | Correct | Brief why |
|---|---|---|
| 1 | A, C, D | System prompt holds stable content (role, format, rules). User question + retrieved context are per-request. |
| 2 | B, D | Jitter spreads retries so concurrent clients don't thunder back together. Reduces recovery-time load. |
| 3 | C | Hybrid + RRF combines semantic (vector) + lexical (BM25). RRF fuses ranked lists by position. |
| 4 | A, B, D | pgvector wins for already-Postgres, small-to-mid scale, transactional needs. Loses on zero-ops and >50M scale. |
| 5 | A, B, C, D | All four are documented ReAct failure modes. (E is unrelated.) |
| 6 | B, C, D | Governance = boundaries + HITL + audit + escalation. (A/E unrelated.) |
| 7 | A, B, C, E | All true. (D — prompt injection doesn't bypass HTTPS; that's transport-layer.) |
| 8 | B | Equality, Sort, Range — for compound indexes. |
| 9 | B | MongoDB favors embedding; Postgres favors normalization. (A/C/D all false.) |
| 10 | B, C, E | Quarantining endpoints, pushing firewall rules, disabling accounts = destructive. Suppressing FP / logging metric = low-risk auto. |
| 11 | B | Models attend more to start and end of context, less to middle. |
| 12 | C | Faithfulness = claims grounded in retrieved context. (B = answer relevancy.) |
| 13 | B | Binary encoding: take *i* coins from pile *i*. (A = ternary balance; D = powers of 2 but for different framing.) |
| 14 | B | Native structured output = token-level grammar enforcement. Eliminates the failure mode entirely. |
| 15 | B | Most common cause: proxy buffering the entire response before forwarding. Fix with `proxy_buffering off`. |

### Part B — Rubric

**Q16.** (Architecture sketch) Look for: alert ingestion → triage agent → enrichment via tools (EDR/SIEM lookups, ideally via MCP) → investigation agent → verdict → HITL gate (especially for destructive actions) → response action. Guardrails layer between input and LLM AND between LLM output and tool execution. Audit log sink off to the side, receiving events from every step. Full marks for clear flow + correctly placed guardrails + audit trail.

**Q17.** (Pseudo-code) Look for: input validation against tool schema; try/except around tool call; sleep with `base * 2^attempt + random.uniform(0, base)` per retry; max 3 attempts; fallback to cached response on final failure; audit log entry with timestamp + tool name + args + result/error. Clean Python-flavored pseudo-code, ~15-25 lines.

**Q18.** (LangGraph vs CrewAI) **LangGraph** is the right answer for Morpheus. Reasons: (1) graph-based architecture maps to audit trails + rollback points (regulated workflow); (2) explicit state machine = checkpointable + resumable for long investigations; (3) LangSmith observability integration = essential for debugging security agent decisions. CrewAI's role-based approach is faster to prototype but lacks the auditability + checkpointing needed for regulated security ops.

**Q19.** Defenses, ranked:
1. **Isolate system prompts from user/tool input** (locked vault). Drawback: doesn't catch injections in retrieved content.
2. **Input validation / classifier** (prompt-injection detection model). Drawback: classifiers can be fooled by novel attacks.
3. **Output filtering / LLM-as-Judge** (catch suspicious responses). Drawback: adds latency + cost; may have false positives that reject valid output.
4. **Least-privilege tool access** (agent can only call tools it absolutely needs). Drawback: restricts agent capability; requires ongoing access review.

---

## Mock #2 — Wednesday Morning (75 min, compressed)

### Part A — Multi-Select (30 min, 12 questions)

[Same format as Mock #1, new questions covering the same topic mix.]

**Q1.** Which characteristic best distinguishes plan-and-execute from ReAct?
- [ ] A) Plan-and-execute uses more tokens overall
- [ ] B) Plan-and-execute generates a full plan before any execution
- [ ] C) Plan-and-execute requires GPU acceleration
- [ ] D) Plan-and-execute is naturally easier to HITL-gate before execution begins

**Q2.** Recursive character splitting for chunking — typical production default values?
- [ ] A) 128 tokens, 5% overlap
- [ ] B) 512 tokens, 10-20% overlap
- [ ] C) 2048 tokens, 50% overlap
- [ ] D) Variable, semantically determined

**Q3.** Reciprocal Rank Fusion (RRF) combines ranked lists by:
- [ ] A) Multiplying the raw scores
- [ ] B) Averaging the positions
- [ ] C) Summing 1/(k + rank) across systems
- [ ] D) Taking the max rank from any system

**Q4.** MCP (Model Context Protocol) is best described as:
- [ ] A) A proprietary Anthropic protocol
- [ ] B) An open standard for connecting LLMs to tools, donated to Linux Foundation
- [ ] C) A replacement for OAuth in agent systems
- [ ] D) A vector database protocol

**Q5.** Which actions should be auto-executable (no HITL) for a Tier 1 SOC agent?
- [ ] A) Suppressing a known-false-positive alert with >95% confidence
- [ ] B) Disabling a privileged admin account
- [ ] C) Enriching alert context with EDR lookups
- [ ] D) Logging the triage decision to the audit trail
- [ ] E) Pushing a new firewall block rule

**Q6.** A weighing puzzle says: "10 piles of coins, all 10g except ONE pile that's 11g. Single weigh." Solution approach:
- [ ] A) Weigh all piles together
- [ ] B) Binary encoding: take *i* coins from pile *i*; (actual - 550) = pile number
- [ ] C) Take 1 coin from each pile; weigh
- [ ] D) Divide piles into thirds and use balance scale

**Q7.** When does an agent loop genuinely beat a single LLM call with structured output?
- [ ] A) Latency-sensitive chat UI
- [ ] B) Dynamic discovery — what to do next depends on what you find
- [ ] C) Known answer shape, single reasoning pass
- [ ] D) Multi-step reasoning requiring real tool outputs along the way

**Q8.** Anthropic's prompt caching achieves ~100% cache hit rate (vs OpenAI's ~50%) because:
- [ ] A) Anthropic uses smaller models
- [ ] B) Anthropic uses explicit cache_control parameter; OpenAI uses implicit caching
- [ ] C) Anthropic caches at the GPU level
- [ ] D) OpenAI doesn't support prompt caching

**Q9.** Faithfulness > 0.8 in RAG evaluation indicates:
- [ ] A) Sufficient context recall
- [ ] B) Production-ready retrieval (answer grounded in retrieved chunks)
- [ ] C) Fast response time
- [ ] D) The system is hallucinating

**Q10.** "Lost in the middle" implies which context-packing strategy?
- [ ] A) Pack the most relevant chunks in the middle
- [ ] B) Pack the most relevant chunks at start AND end
- [ ] C) Distribute relevance uniformly
- [ ] D) Use only one chunk per request

**Q11.** Average speed when half the distance is at 60 mph and half at 40 mph:
- [ ] A) 50 mph
- [ ] B) 48 mph
- [ ] C) 52 mph
- [ ] D) 100 mph

**Q12.** MongoDB sharding: which shard key strategy avoids monotonic-write hotspots?
- [ ] A) Auto-increment ID
- [ ] B) Timestamp
- [ ] C) Hashed shard key
- [ ] D) User ID (random distribution)

---

### Part B — Short Structured Answers (45 min, 3 questions)

**Q13.** (15 min) An LLM-powered SOC agent has just hallucinated a tool call to disable a real admin account. Design an audit trail format that would help post-incident investigation. List ≥5 specific fields and why each matters.

**Q14.** (15 min) Architecture: sketch a "guardrail pipeline" that sits between a user query and an LLM. Include input validation, prompt-injection detection, LLM call, output filtering, and audit logging. Annotate WHERE each component runs (gateway / app / sidecar / dedicated service).

**Q15.** (15 min) John's Caseway product uses Elasticsearch as both keyword search engine AND vector store. Defend OR critique this architectural choice for a legal-case search engine — give the strongest arguments on both sides, then state your recommendation.

---

## Mock #2 — Answer Key

### Part A

| Q | Correct | Brief why |
|---|---|---|
| 1 | B, D | Full plan upfront vs interleaved; natural HITL gate before any execution. |
| 2 | B | 512 tokens, 10-20% overlap is the production default for recursive splitting. |
| 3 | C | RRF: Σ 1/(k + rank). k usually 60. Position-based, not score-based. |
| 4 | B | Open standard, donated to Agentic AI Foundation (Linux Foundation) Dec 2025. |
| 5 | A, C, D | Auto-allowed: low-risk (FP suppress), read-only (enrichment), logging. HITL: destructive (B, E). |
| 6 | B | Binary encoding — take i coins from pile i. |
| 7 | B, D | Dynamic discovery + multi-step with real tool outputs are the agent-loop sweet spots. |
| 8 | B | Explicit cache_control = deterministic caching; implicit = best-effort. |
| 9 | B | Faithfulness measures answer-to-context grounding. >0.8 = production-ready retrieval. |
| 10 | B | Place most relevant chunks at start AND end of context. |
| 11 | B | Harmonic mean: 2(60)(40)/(60+40) = 4800/100 = 48 mph. NOT 50. |
| 12 | C | Hashed shard key distributes writes evenly; range/monotonic keys create hotspots. |

### Part B — Rubric

**Q13.** Audit fields: (1) timestamp, (2) agent ID + version, (3) tool name + version, (4) tool arguments (full), (5) tool result / error, (6) confidence score (if applicable), (7) HITL approval (yes/no + approver if yes), (8) parent trace ID (for multi-step investigations), (9) policy violations triggered (if any). Bonus: prompt hash so you can correlate to system prompt version. Each field has a clear post-incident use case.

**Q14.** Pipeline: User query → API gateway (auth, rate limit, request log) → Input validation service (size limits, PII scrub) → Prompt injection classifier (ML model, sidecar or dedicated service) → LLM call (with proper system prompt isolation) → Output filter (LLM-as-Judge OR rule-based, sidecar) → Audit log sink (async, never blocks response) → Response. Components annotated by deployment location.

**Q15.** **Defend:** Single system, single backup, single operational story. ES has BM25 + vector built-in; native hybrid search via Reciprocal Rank Fusion. No cross-system sync. Mature operational tooling. **Critique:** Vector capabilities in ES are newer / less optimized than purpose-built vector DBs; expensive on storage compared to specialized stores; harder to tune for pure vector workloads. **Recommendation:** For Caseway's scale, ES hybrid is the right call. Reconsider if (a) vector volume hits 50M+, (b) latency requirements drop below 50ms, OR (c) need advanced vector-specific features (multi-vector indexing, etc.).

---

## Grading Protocol

- **Part A:** 1 point per fully correct question (all selected correct + no incorrect). 0.5 if partial. 0 if missed key correct or selected major incorrect.
- **Part B:** 0-1 per question on a 0/0.25/0.5/0.75/1 scale against the rubric.
- **Pass bar:** 75% overall.
- **Below 70%:** re-cram the 2 weakest topic notes; redo the missed questions Wednesday morning.

---

## Self-Reflection Log

After each mock, capture:

| Date | Mock # | Score | Top 3 weak areas | Action |
|---|---|---|---|---|
| _ | _ | _ | _ | _ |
