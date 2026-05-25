# Lesson 2 — RAG Deep — Written Exercise

> **Format:** D3 test format. Short structured answer (bullets + 1-line justifications), closed-book, ~10 min.
> **Pass bar:** name the canonical root cause + canonical fix for each symptom. Bonus for operational gotcha + senior framing.

---

## Prompt

A security SaaS team is building a RAG-based "Ask Your Security Policies" feature for internal SOC analysts. The corpus is **~3M policy docs and incident write-ups** stored in their existing Postgres database. Current implementation:

- Vector store: **pgvector** on the same Postgres instance
- Embedding model: **`text-embedding-3-small`**
- Retrieval: **pure vector search, top-10 chunks**
- Generation: **GPT-4o-mini** with retrieved chunks in the prompt

A month after launch the team reports three production symptoms. For each, answer in 2-3 bullets:

**(a) Root cause** — what's actually wrong?
**(b) Canonical fix** — what would you implement?
**(c) Operational gotcha** — what should the team plan for when implementing the fix?

---

### Symptom A

Queries containing exact identifiers — **CVE-2024-12345**, IP ranges (**10.0.0.0/8**), policy IDs (**SEC-POL-0234**) — consistently return irrelevant chunks. Semantic queries like "what's our policy on data retention?" work fine.

**Your answer:**
- (a) Root cause: Lack of keyword matches on exact data like IDs.
- (b) Canonical fix: Hybrid search implementation via adding BM25 search functionality in tandem with semantic (vector) search
- (c) Operational gotcha: pgvector does not have a native hybrid search config. This will have to be created, tested, and handled manually by the dev team to ensure that it produces the best possible results from both retrieval meothods

---

### Symptom B

Long policy documents (**50+ pages**) sometimes return chunks that "technically mention the right topic but miss the actual policy detail." Investigation shows chunks are being split **mid-paragraph and mid-table**, breaking semantic coherence.

**Your answer:**
- (a) Root cause: Original embedding process did not account for natural breakpoints and instead chunked data "blindly"
- (b) Canonical fix: Re-index large documents to account for breakpoints like tables, or mid-paragraph related text.
- (c) Operational gotcha: Requires a full re-embedding of your failing data corpus 

---

### Symptom C

The lead engineer wants to switch the embedding model to **`text-embedding-3-large`** to improve recall on long semantic queries. A junior engineer asks why this can't ship as a config change in next Tuesday's deploy.

**Your answer:**
- (a) Root cause (why isn't it just a config change?): not entirely sure but 
- (b) Canonical fix (how DO you migrate?): have to re-ingest your entire data corpus using this new model as there is NO vector overlap between ingestion/embedding models 
- (c) Operational gotcha: Have to re-ingest your entire data corpus, test the new RAG pipeline thoroughly, and then intelligently swap out your outdata RAG pipeline in prod 

---

## Grading

### Symptom A — Hybrid retrieval (exact identifiers)
- **Grade: A-/A** — strongest of the three.
- **What landed:**
  - Root cause clean: pure vector search has no lexical-match capability for IDs.
  - Canonical fix named correctly (BM25 + vector hybrid).
  - **Operational gotcha was the senior-signal moment.** pgvector genuinely does NOT ship native hybrid/RRF (unlike ES, Qdrant, Weaviate). Hybrid in Postgres = combine pgvector with Postgres FTS (`tsvector` + `ts_rank`) and merge manually. Real knowledge, not memorized.
- **What missed:**
  - Didn't name **RRF (Reciprocal Rank Fusion)** as the canonical merge algorithm — the senior add would be: *"merge with RRF since BM25 and vector scores are on incompatible scales."*

### Symptom B — Chunking strategy
- **Grade: B+/A-**
- **What landed:**
  - Root cause: "blind" chunking ignoring natural breakpoints — right idea.
  - Operational gotcha: chunking changes require re-embedding affected corpus.
- **What missed:**
  - Didn't NAME the canonical fix: **recursive character splitter** (paragraph → sentence → word → char) with 10-20% overlap as the default; **document-aware splitters** for tables/Markdown/code as the upgrade path.
  - Same "knows mechanism, struggles with names" pattern from cold quiz Q2 — locked under cold pressure too.

### Symptom C — Embedding model migration
- **Grade: B-/B**
- **What landed:**
  - (b) was strong — "no vector overlap between models, full re-ingest required" is exactly right.
  - (c) named the parallel-test-then-swap operational plan correctly.
- **What missed:**
  - (a) "not entirely sure" — but the answer was IN your (b). Content was in the wrong slot. The WHY is: **different embedding models produce incompatible vectors — different dimensions (1536 vs 3072), different vector spaces. A 1536-dim vector from `3-small` is meaningless to `3-large` which produces 3072-dim vectors. Querying 3072-dim queries against a 1536-dim index = runtime failure or silent garbage retrieval.** That's the (a) answer.
  - "Intelligently swap" → name the pattern: **atomic index swap** or **index alias cutover** (production reads from alias → `index-v1`; build `index-v2` in background; flip alias atomically).
  - In a written test, "not entirely sure" forfeits the (a) points even when you knew the answer — write SOMETHING under each header, even if hedged.

### Overall
- **Total: B+/A- (~82-85%).** Passed the 75% bar cleanly. Matches Lesson 1 level (B+/A- ~78%).
- **Patterns observed:**
  - **POSITIVE: Real-knowledge senior signal on Symptom A operational gotcha.** Naming pgvector's lack of native hybrid is the kind of detail that separates someone who's shipped RAG from someone who's read about it.
  - **RECURRING: "Knows mechanism, struggles with names."** Both Symptom B (couldn't name recursive character splitter or document-aware chunking) and Symptom A (no RRF name). Same pattern as cold quiz Q2 + Q4. Mechanism is locked; specific vocabulary is the bottleneck under pressure.
  - **NEW: Content-in-wrong-slot.** Symptom C (a) said "not sure" while answering it fully in (b). Written-test mechanical: when the question explicitly labels (a)/(b)/(c) slots, the grader scores per slot. Write something even hedged for every slot.
  - **POSITIVE: Cross-symptom transfer holding.** Re-embedding cost named in both B and C, consistent with cross-chunk transfer from Q3/Q4 of cold quiz.
- **Re-drill items for mock test:**
  1. **Vocabulary drill** — under cold quiz pressure, force naming: recursive character splitter, RRF, atomic index swap, document-aware chunking, RAGAS (with the S).
  2. **No "not sure" on D3 written test** — always write SOMETHING in every labeled slot, even hedged. Honest "I don't know" works conversationally but forfeits points on a structured written test.
  3. **Stretch goal for senior signal:** when answering operational-gotcha slots, lean on Caseway-anchored real knowledge (like the pgvector hybrid example) — that's where you differentiate.
