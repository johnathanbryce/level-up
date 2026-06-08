# AI Foundations Refresh (Area 2)


## RAG + hybrid search

- **RAG in one breath:** embed your corpus -> store in a vector index -> at query time, embed the query, retrieve **top-K** most similar chunks -> stuff them into the prompt as grounded context -> model answers from *grounded context instead of just memory*

- **Chunking trade-off:** too big = noise dilutes the match; too small = context gets lost.

- **Hybrid search (vector + BM25, fused via RRF):** **vector (semantic)** + **keyword (BM25)** combined, often fused with **Reciprocal Rank Fusion**. 
    - Vector catches *meaning*; keyword catches *exact terms* - names, codes, IDs, that semantic search fumbles

- **Why it matters (grounding):** RAG is how you do the "grounding" trust - its the mechanism behind "the agent reasons over real data, doesn't free associate"
