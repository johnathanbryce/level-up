# RAG Deep — My Notes

> **Status:** Not yet taught.
> **Lesson plan:** [../lesson-tracker.md](../lesson-tracker.md) → RAG Deep section.
> Take notes below as Claude teaches. You ship RAG production code at Caseway already — this lesson formalizes and deepens what you do.

---

## Chunk 1 — Full RAG pipeline (offline indexing + online querying)

**RAG = two parallel pipelines, sharing the vector store as handoff.**

- **Indexing (offline):** `Documents → Chunk → Embed → Store`. Batch/async, latency irrelevant, cost = embedding calls.
- **Querying (online):** `Query → Embed → Retrieve top-K → Rerank → Assemble → Generate → Cite`. User-facing, sub-second target, cost = LLM + reranker.

**Why "two pipelines" matters as framing:** can't reason about chunking, embedding model, or vector store choice without knowing whether you're optimizing ingestion throughput (offline) or query latency (online). They pull opposite ways.

**Killer stat (memorize):** ~73% of RAG failures are RETRIEVAL, not generation.

**Interview line:** *"Bigger LLMs are the wrong lever. ~73% of RAG failures are retrieval, so I'd invest in chunking, hybrid search, and reranking before reaching for a more expensive generator."*

---

## Chunk 2 — Chunking strategies (recursive 512-token default; fixed / semantic / document-aware)

- **Default → recursive character splitter** — 512 tokens, 10-20% overlap.
  - **What "recursive" means:** splitter tries natural boundaries **in order** — paragraph → sentence → word → char
  - Keeps chunks coherent: sentences stay intact, paragraphs stay grouped where they fit

- **Upgrade to document-aware splitters** when format has structure worth preserving:
  - **Code** — split on functions/classes, not mid-function
  - **Markdown** — split on headers
  - **PDFs with tables** — preserve table boundaries

- **Long-doc trick — parent-document retrieval:** index *small* chunks for retrieval position; return the parent doc for generation context.

- **Interview line:** *"Recursive 512-token splitter with 10-20% overlap is the prod default. Splits on natural boundaries so chunks stay coherent. Upgrade to document-aware splitters when the format has structure worth preserving, like code or tables in PDFs."*

---

## Chunk 3 — Embedding model choice (text-embedding-3-small default; when to self-host)
- **Default:** OpenAI `text-embedding-3-small`.
    - Cheap enough that re-embedding a corpus is affordable
    - 1536 dimensions = fits comfortably in any vector store
    - Multilingual
    - OpenAI's batch API gets you 50% off for offline indexing

- **When to upgrade to `text-embedding-3-large`:** if benchmarks show recall@k is your bottleneck.
- **The migration trap:** different embedding models produce **incompatible vectors**. You CANNOT mix them in the same index. Switching models means re-embedding your ENTIRE corpus.

---

## Chunk 4 — Vector store choice (pgvector / Pinecone)

- **pgvector (Postgres extension)** — default when already on Postgres + corpus <10M vectors. Transactional consistency with app data, single backup, no cross-system sync.
- **Pinecone (managed SaaS)** — default when you want zero ops + can pay + scale matters. Scales to billions, predictable latency.
- **Elasticsearch** — what Caseway uses. Search engine that added vector capabilities later; valid when keyword + vector are both first-class.

- **Interview line:** *"pgvector for Postgres shops under 10M vectors — same DB, transactional, free. Pinecone when scale or zero-ops matter. Elasticsearch when keyword + vector are both first-class, like Caseway."*

---

## Chunk 5 — Retrieval techniques (vector vs BM25 vs hybrid + RRF)
- **Pure vector misses exact-token matches:** finds **semantic** matches ("car" ↔ "automobile") but misses model numbers, error codes, IDs, acronyms.
    - Query *CVE-2024-1234* against pure vector → returns semantically-similar vuln descriptions but misses the doc that literally contains that CVE ID.

- **Pure BM25 misses conceptual matches:** keyword relevance via term frequency + rarity. Finds exact tokens beautifully; misses synonyms.
    - Query *car safety* won't match "vehicle crash protection."

- **They fail in opposite directions** → hybrid wins by covering both blind spots.

- **The merge problem:** can't average BM25 scores and vector scores — different scales, not comparable.
- **Reciprocal Rank Fusion (RRF)** — standard solution. Merges by **rank position**, not score. Docs that rank high in BOTH lists score highest.
- **Most modern vector stores handle RRF natively** (ES, OpenSearch, Qdrant, Weaviate) — config flag, not something you implement.

- **Interview line:** *"Hybrid retrieval is the biggest single lever in RAG. Vector finds semantic matches; BM25 finds exact tokens like CVE IDs or model numbers. They fail in opposite directions, so combining them covers both blind spots. The merge problem is that the two have incompatible score scales — RRF solves it by merging on rank instead of score. Most modern vector stores ship RRF natively, so it's a config-level decision."*

---

## Chunk 6 — Reranking
- **2-stage retrieval pattern:** Hybrid retrieve (top 50-100) → Rerank (top 5-10) → LLM.

---

## Chunk 7 — Context assembly + citations (dedupe, order, "lost in the middle")
- Top 5-10 re-ranked chunks — don't just dump into the prompt. 3 things to handle before LLM call:
    1. **Dedup near-duplicates** — if two chunks say nearly the same thing, drop one
    2. **Ordering matters ("lost in the middle")** — LLMs attend more to **start and end** of context window. Put **most-relevant chunk at start, second-most-relevant at end**
    3. **Mandatory "I don't know" fallback** — if retrieval returns nothing relevant (low confidence scores), system must return "I don't have enough info to answer that"

- **Citations:** each retrieved chunk should carry metadata (doc ID, section, line range). Embed those as inline citations in the answer.

---

## Chunk 8 — RAG evaluation (faithfulness, answer relevancy, context precision; RAGAS)
- **How do you evaluate a RAG system?** → a framework. **RAGAS** is the prod standard.
- **How does it work mechanically?** → **LLM-as-judge**. A second LLM scores the first LLM's output, lets you eval on **live production traffic** without human labels.
- **Why does it matter?** → **No human-labeled ground-truth data needed.**

---

## Chunk 9 — Advanced patterns (HyDE, parent-document retrieval, multi-query)
1. **HyDE (Hypothetical Document Embeddings):**
    - **The trick:** generate a hypothetical answer to the user's query, then embed THAT and search with it (instead of embedding the question)
    - **Why it works:** answer-text matches answer-text in vector space better than question-text matches answer-text. Questions and answers don't look semantically identical even when they should.

2. **Query Rewriting:**
    - **The trick:** before retrieval, rewrite the user's query (fix spelling, expand acronyms, generate multiple paraphrases and retrieve against all of them)
    - **Why it works:** users write messy queries. Cleaning + expanding before retrieval catches docs the original phrasing would miss.

---

## End-of-Lesson Self-Quiz Answers

_Filled in after Claude runs the quiz._
