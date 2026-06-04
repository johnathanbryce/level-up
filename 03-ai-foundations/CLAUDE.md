# AI Foundations (Light) — Progression Tracker

## Overview

Light pass on AI/LLM concepts. Goal is conceptual understanding and a basic working POC, NOT production-grade implementation. The deep dive happens in Section 5 after system design and backend knowledge are solid.

**Prior Knowledge:** Johnathan has already completed LLM integration patterns (streaming, cost control, prompt lifecycle, full request lifecycle). This section picks up from there.

## Definition of Done

Can explain RAG architecture end-to-end, describe chunking trade-offs with specific examples, articulate when vector search fails and what alternatives exist. Has a working basic RAG proof-of-concept.

---

## Section Operating Model

Locked in 2026-05-17 before the first chunk of real material. Future-Claude in a fresh window should read this section first to understand how this section is taught and where artifacts live.

### Folder map

```
03-ai-foundations/
├── CLAUDE.md
├── notes/          numbered .md files per sub-topic group (one file per group)
│                   01-embeddings-and-vector-concepts.md, 02-rag-architecture.md, 03-search-and-retrieval-concepts.md
│                   (files created lazily — only when John starts taking notes on that group)
├── experiments/    micro-scripts (~10-15 min each) that ride inside conceptual chunks to make abstract ideas concrete
│                   examples: embeddings_demo.py, cosine_similarity.py, chunking_demo.py
└── rag-poc/        capstone hands-on project (FastAPI + embeddings + vector store + LLM call)
                    populated only when sub-topic group 4 starts
```

### Notes-file pattern

Identical to System Design. Within each `notes/NN-*.md` file:
- `#` file title only
- `##` major sections (one per CLAUDE.md sub-bullet group)
- `###` sub-sections
- `**bold**` reserved for vocabulary/emphasis only — NEVER as a section marker

End-of-session heading audit (per project CLAUDE.md) applies.

### Teaching cadence

| Granularity | What happens |
|---|---|
| **Chunk** (5-10 min) | Teach one concept → one quick applied check question → confirm landed → next chunk. No formal quiz at this granularity. |
| **Sub-topic group** | "Now apply it" beat — applied scenario, diagram, or 2-3 question check before marking the group done. Per Daily Session Structure rule. |
| **Pre-POC gate** (after groups 1-3) | End-of-section warm-down quiz, 5-7 mixed-format questions across embeddings + RAG + search/retrieval. Mandatory gate before starting the POC build. |
| **Capstone** | POC Demo + Verbal Walkthrough — already defined further down this file. Section close gate. |

### Hands-on mix per sub-topic group

| Group | Mix | Specific hands-on |
|---|---|---|
| 1. Embeddings & Vector Concepts | Concept-heavy + 2 micro scripts | `embeddings_demo.py`, `cosine_similarity.py` |
| 2. RAG Architecture | Concept-heavy + diagram + 1 micro script | Pipeline flow diagram (ingest → chunk → embed → store → retrieve → generate); `chunking_demo.py` |
| 3. Search & Retrieval Concepts | Concept-only by default | Optional `bm25_vs_vector.py` if BM25 vs embeddings confusion lingers (flagged 2026-04-21, 2026-05-14) |
| 4. Hands-On: Basic RAG POC | Pure hands-on build under `rag-poc/` | Full pipeline — see Sub-Topics below |

Micro-scripts: Claude scaffolds the boilerplate, John writes the meaningful lines. Same rule as algos.

### Granularity guide — how deep to go on AI topics

Locked in 2026-05-17 in response to John's "how granular do I need to go?" question during chunk 2. Use as the rubric for any sub-topic in this section.

| Tier | Meaning | Examples |
|---|---|---|
| **1 — Must know cold** | Interview-death-blow level. Cannot fumble. | What an embedding IS; why semantic search beats keyword for freeform queries; general RAG pipeline shape (ingest → chunk → embed → store → retrieve → generate); that chunking is necessary |
| **2 — Should reason about it** | Mid-level differentiator. Explain + justify trade-offs, don't memorize. | Cosine similarity (roughly why); chunking trade-offs (small vs large); API mechanics (tokens, batching, rate limits); different models → incompatible vectors |
| **3 — Senior / nice-to-have** | Look up when needed; do NOT memorize. | Specific dimensions per model (1536, 1024); specific token limits (8191); cost per 1M tokens; vector DB choice rationale; HNSW / ANN index internals; re-ranking strategies |
| **4 — Specialized only** | Not required for general AI engineering. | Transformer internals (attention math, layer norm); training your own embedding model; embedding fine-tuning |

**Rule of thumb:** if John can articulate Tier 1 + reason about Tier 2 trade-offs, that's mid-level competency for this section. Tier 3 specifics can be Googled when actually needed — don't burn cycles memorizing tier-3 numbers, burn them on locking Tier 1-2 mental models.

**When teaching:** flag concepts by tier as they come up ("this is a Tier 3 detail — know it exists, look it up"). When John pushes back on density, default to: keep Tier 1-2 in notes, mention Tier 3 in passing, skip Tier 4 entirely.

---

## Sub-Topics

### Embeddings & Vector Concepts

- [x] What embeddings are — text as numerical vectors, semantic similarity (2026-05-17)
- [x] How embedding models work (high level — not transformer internals) (2026-05-18)
- [x] Cosine similarity and distance metrics (2026-06-03)
- [x] Dimensionality and its impact on performance/quality (2026-06-03)
- [x] Common embedding models and their trade-offs (OpenAI, Cohere, open-source) (2026-06-03)

**GROUP 1 COMPLETE (2026-06-03)** — Embeddings & Vector Concepts done. `cosine_similarity.py` micro-script built + run (bank/loan 0.761, dog/puppy 0.576, unrelated 0.07–0.19 — semantic property proven hands-on). Next sub-topic group: RAG Architecture.

### RAG Architecture

- [ ] End-to-end RAG pipeline: ingest → chunk → embed → store → retrieve → generate
- [ ] Chunking strategies: fixed-size, semantic, recursive, overlap
- [ ] Chunking trade-offs: small chunks (precise, less context) vs large (more context, noisier)
- [ ] Retrieval: top-K selection, similarity thresholds, re-ranking
- [ ] Citation and grounding — how to attribute answers to source documents
- [ ] Hallucination risks and mitigation strategies

### Search & Retrieval Concepts

- [ ] Vector search: approximate nearest neighbors (ANN), HNSW index
- [ ] Keyword search: BM25, TF-IDF (conceptual understanding)
- [ ] Hybrid search: combining vector + keyword, why it outperforms either alone
- [ ] When vector search fails (out-of-domain queries, exact match needs, sparse data)
- [ ] Retrieval evaluation: precision, recall, relevance scoring

### Hands-On: Basic RAG POC

- [ ] Set up a simple Python project with FastAPI
- [ ] Implement document ingestion and chunking
- [ ] Generate and store embeddings (pgvector or in-memory for POC)
- [ ] Implement basic retrieval (vector similarity search)
- [ ] Connect to an LLM for answer generation
- [ ] Test with sample documents and queries

---

## End-of-Section Capstone

This section is lighter than System Design — the RAG POC is the primary proof of understanding. The capstone adds one verbal layer to confirm the concepts are internalized, not just implemented by following a tutorial.

### POC Demo + Verbal Walkthrough (20-30 min)
John runs the working RAG POC and explains the full pipeline end-to-end (ingest → chunk → embed → store → retrieve → generate) as if onboarding a junior engineer — no notes. Claude then asks 4-5 targeted follow-up questions, for example:
- "Why this chunk size? What would break if you doubled it?"
- "Your vector search returned a bad answer for an exact-match query. Walk me through how you'd debug it."
- "When would this POC fail at scale? What's the first thing you'd change?"
- "What's the difference between your vector search and what Elasticsearch does?"
- "How would you evaluate whether this RAG system is actually giving good answers?"

**Pass criteria:** POC works end-to-end, pipeline explained clearly without notes, 3/5 follow-up questions answered with specific reasoning (not vague gestures). Section closes when this passes. Log result in Session Log below.

**Capstone result:** NOT YET RUN

---

## Session Log

| Date | Topics Covered | Assessment | Next Focus |
|------|---------------|------------|------------|
| 2026-05-17 → 2026-05-18 | Section Operating Model locked (folder structure, teaching cadence, Granularity Guide); Chunk 1 (What an embedding is); Chunk 2 (How embedding models work); `embeddings_demo.py` micro-script (3 TODOs: single embedding, batched embeddings, determinism — all running end-to-end) | Strong session, but TWO critical mental-model corrections required mid-session: (1) embeddings ≠ LLMs (separate model categories, shared transformer architecture, different jobs) — John initially framed the section as "how LLMs work / how to train models" — corrected with "What this section IS/IS NOT" + "Embeddings ≠ LLMs" callouts added at top of notes file; (2) embedding output dimensions are FIXED by the model, NOT by input length — John asked "len(embedding) should match length of each SENTENCE in characters?" — corrected with strengthened "variable-length text → fixed-size vector is the whole point" framing in notes. Three real-world snags hit on the micro-script: modern OpenAI SDK v1.x instance-based pattern (`client.embeddings.create`, not legacy `openai.embeddings.create`), `Embedding` wrapper object vs `.embedding` float-list attribute, `assert` as a Python primitive (new to John). All addressed cleanly. POSITIVE: John self-asked for verbosity audit + tier-granularity rubric — strong calibration instinct. | Chunk 3 — Cosine similarity and distance metrics (concept ~10-15 min, then paired `cosine_similarity.py` micro-script computing pairwise similarity across the 5 sentences from `embeddings_demo.py` — should show bank/loan and dog/puppy as closest pairs, validating semantic-similarity property hands-on) |
| 2026-06-03 | **Low-energy/low-motivation slog day (John flagged upfront).** No algo (opted B = quick applied recall instead). Chunks 3-5 (cosine similarity, dimensionality, model trade-offs) — **GROUP 1 COMPLETE.** John's Tier-3 scoping pushback on cosine similarity (mid-chunk) → collapsed Chunk 3 to a 3-line Tier-1/2 version (concept + ranking role, NO formula memorization) per the Granularity Guide; agreed to skip then UN-skip the `cosine_similarity.py` micro-script (John re-opted in — "I can actually see that process"). Built it (Claude scaffolded cosine helper + TODO structure, John wrote `embed_all()` + the unique-pair nested loop). Ran clean: bank/loan **0.761**, dog/puppy **0.576**, unrelated 0.07–0.19 — semantic property proven on his own data. | Opening recall: John's "an embedding is the *process* of uploading text" slip (it's the OUTPUT/vector) + re-coupled embeddings to RAG/LLM again (2nd time — same gap as 2026-05-18). Corrected. Close-out 2-Q check: Q1 B+ (concept solid; didn't crisply name "cosine score = the ranking number"; said vectors represent "similarity" when they represent *meaning*), Q2 B (correct self-host decision + privacy reasoning, but did NOT name the operational cost — "you now own the infra" — when explicitly asked to name the trade-off → SAME knows-rule-not-implication shape as systems-design side). NEW Python fluency: f-string format specs `:.3f` (fixed-point, 3 decimals) + `!r` (repr → quotes). Env yak-shave: nodemon watcher runs bare `python` = anaconda (8.4G, corrupted dotenv); fix = run with `.venv/bin/python`; John floated nuking anaconda — DEFERRED (only bare `python` on system, would break all algo watchers + needs .zshrc/.bash_profile conda-init cleanup). | **RAG Architecture group** (notes file `02-rag-architecture.md`): end-to-end pipeline (ingest→chunk→embed→store→retrieve→generate) + chunking strategies/trade-offs + retrieval (top-K, thresholds, re-ranking) + citation/grounding + hallucination mitigation. Includes pipeline-flow diagram + `chunking_demo.py` micro-script. |

---

## Notes & Weak Spots

- **Foundational AI vocabulary needs definitions, not just terms (2026-05-18).** "Neural network" and "transformer" were terms-without-meaning until taught with one-sentence definitions + WHY-it-matters explanations. Expect this pattern for every new AI domain concept — define the term, explain the mechanism, then move on. Don't drop named concepts without grounding them.
- **Embeddings re-coupled to RAG/LLM — 2nd occurrence (2026-06-03).** Opening recall, John defined an embedding as "the process of uploading text to your RAG system... so the LLM can refer to it." Two slips in one: (1) an embedding is the OUTPUT (the vector), not a process; (2) embeddings have nothing to do with RAG/LLM by themselves — text→vector is the whole job; RAG is one *use case*. Same decoupling that needed correcting 2026-05-18. Re-test at RAG group start: "what is an embedding, and is an LLM involved in producing one?" (Answer: no.)
- **"Name the trade-off / cost" → restates the decision instead (2026-06-03).** Q2 close-out: asked to name the operational cost of self-hosting, John re-justified the decision ("use open-source locally") rather than naming the cost (*you now own/run the infra*). Same knows-rule-not-implication shape tracked extensively on the systems-design side. Drill in this section too: whenever a question says "name the cost/trade-off," force the concrete thing given up, not a restatement of the choice.
- **Embedding length misconception caught (2026-05-18).** John asked if `len(embedding)` should equal the number of characters in each input sentence. Corrected hard: embedding output dimensions are FIXED by the model (1536 for text-embedding-3-small), NOT by input. The variable-length-text → fixed-size-vector mapping IS the whole point of embedding models. Notes strengthened. Watch for similar shape-of-output confusion in chunk 3 (cosine similarity output is a single float, not a vector) and chunk 4 (dimensionality trade-offs).
- **Embeddings ≠ LLMs mental model (2026-05-18).** John initially framed this section as "how LLMs work under the hood + how to train models" — both wrong. Embeddings and LLMs are SEPARATE model categories with different jobs (search/retrieval vs generation), sharing transformer architecture as common building block. We are CONSUMERS of pre-trained models in this section. Locked via "What this section IS/IS NOT" + "Embeddings ≠ LLMs" comparison table at top of notes file. Re-test at chunk 3+ start to confirm it stayed locked.
- **Modern OpenAI SDK pattern (2026-05-18).** Pre-2023 tutorials all show `openai.embeddings.create(...)` (legacy v0.x module-based). Modern SDK is instance-based: `client = OpenAI(); client.embeddings.create(...)`. Real interview gotcha for anyone Google-searching for "Python openai embeddings."
- **OpenAI response wrapper structure (2026-05-18).** `response.data[i]` is an `Embedding` object, NOT a float list. The actual vector is `response.data[i].embedding`. Cleaner habit: extract once with `[d.embedding for d in response.data]` before doing anything downstream — gives clean `List[List[float]]` and decouples from OpenAI-specific wrapper types.
- **`assert` is new to John (2026-05-18).** Taught syntax, truthy/falsy evaluation, senior caveat (stripped with `-O`, never use for security/control flow / input validation — use `if not condition: raise ValueError(...)` instead).
- **POSITIVE: tier-granularity rubric born from John's pushback (2026-05-18).** John asked "how granular do I need to go?" — codified as 4-tier Granularity Guide in the Section Operating Model. He immediately validated by correctly identifying "memorize 8191 tokens for text-embedding-3-small" as Tier 3 (look up when needed). Use this rubric consistently going forward.
- **POSITIVE: verbosity self-awareness (2026-05-18).** John explicitly asked for trim audit mid-section before content piled up. Healthy senior-flavor calibration. Honor it — don't bloat notes with Tier 3 specifics.

---

## Bridge to Section 5

When this section is complete, Johnathan will have conceptual understanding and a basic POC. Section 5 (AI Production) revisits all of this with system design knowledge: caching embeddings, scaling retrieval, hybrid search implementation, evaluation pipelines, cost optimization, and production failure handling.
