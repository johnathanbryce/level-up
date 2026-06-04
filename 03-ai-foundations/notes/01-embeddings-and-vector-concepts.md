# Embeddings and Vector Concepts

## Section Legend

- [x] Chunk 1: What an embedding is
- [x] Chunk 2: How embedding models work (high level)
- [ ] Chunk 3: Cosine similarity and distance metrics
- [ ] Chunk 4: Dimensionality and its impact on performance/quality
- [ ] Chunk 5: Common embedding models and trade-offs

---

## What this section IS (and is NOT)

**IS:** Understanding embeddings — a category of model that converts text into vectors representing meaning. Used for SEARCH and RETRIEVAL (the "R" in RAG).

**IS NOT:** How LLMs work internally. Embeddings and LLMs are separate models with different jobs, though both use transformer architecture under the hood.

**IS NOT:** How to train models. We are consumers of pre-trained models — call an API, get a vector. Training is Tier 4 (specialized).

---

## Embeddings ≠ LLMs

They are **separate model categories** with different jobs.

| | Embedding model | LLM (Claude, GPT-4) |
|---|---|---|
| **Input** | Text | Text |
| **Output** | A vector of floats | More text |
| **Job** | Turn meaning into geometry (for SEARCH/RETRIEVAL) | Generate human-like responses to prompts |
| **Architecture** | Transformer (typically) | Transformer (typically) |
| **Use case** | Search index, RAG retrieval, dedup, recommendations | Answers, code, summaries, chat |

**The shared piece:** both use transformer architecture. That's why chunk 2 covered transformers — same building block, different model trained for a different job.

**Where they meet (this is RAG):**

1. **Embedding model** finds the most relevant docs from your knowledge base
2. Those docs get stuffed into the **LLM's prompt** as context
3. **LLM** generates the final answer using question + retrieved docs

**Embeddings = the search engine. LLM = the writer.** Two different models, two jobs, used together.

**And — we are NOT training models in this section.** We are **consumers** of pre-trained embedding models. Call OpenAI's API, get vectors back, use them to power search. Training your own embedding model is **Tier 4** (specialized — not general AI engineering).

---

## What an Embedding Is

- An **embedding** is a list of floating-point numbers - a **vector** - that represents the _meaning_ of a piece of text (or an image, or audio - but text is our focus)
- EXAMPLE: if you embed the string _"the cat say on the mat"_ with OpenAI's small model, you get back something like:
  - [0.012, -0.084, 0.231, 0.005, -0.117, ..., 0.043] # 1536 numbers

### The core property - why embeddings matter

- **Similar meaning → similar direction.**
- _Meaning becomes geometry. Two texts that mean similar things produce two vectors that point in similar directions._
- Without this property, a vector is just a meaningless list of numbers
  - _"dog"_ and _"puppy"_ -> vectors pointing **roughly the same direction**
  - _"dog"_ and _"golden retriever"_ -> also close
  - _"dog"_ and _"calculator"_ -> vectors pointing in **very different directions**

### The killer use case - semantic search

- Consider two phrases:
  - Phrase A: _"the bank approved my loan"_
  - Phrase B: _"the financial institution accepted my application"_
- These share **zero exact keywords**. A keyword search system (BM25, classic ES term matching) would treat them as completely unrelated documents
- Embedding-based search treats them as **high similar** because the underlying vectors point in nearly the same direction
- The model has learned, from training on huge text corpora, that "bank" and "financial institution" cluster together in meaning-space
- This is what makes "semantic search" a different category of tool from keyword search - and it is the foundation of RAG, recommendation systems, and most modern AI retrieval

### How semantic search actually works (mechanism)

1. **Index time:** every doc gets embedded → vector stored in a vector store (e.g., pgvector, Pinecone)
2. **Query time:** the query gets embedded with the **same model** → `V_query`
3. **Match step:** compute cosine similarity between `V_query` and every stored `V_doc` (or use an ANN index for speed — see chunk 3)
4. **Return:** the top-K docs by similarity score

- **GOTCHA — embeddings are passage-level, NOT word-level.** The query _"how do I reset my password"_ produces ONE 1536-dim vector for the whole sentence — NOT seven word vectors. This is the modern transformer-based approach. (Older techniques like word2vec DO operate per-word, but that's not what modern embedding models do.)

### Two properties worth remembering

1. **Deterministic** - same input text -> same vector (every time, from the same model version)
2. **Model-incompatible** - an embedding from OpenAI's model and an embedding from Cohere's model for the same string live in **different vector spaces**. You cannot compare them. Switching models = re-embedding everything from your store

## How Embedding Models Work (High Level)

### What an embedding model actually is

- An embedding model is a **neural network** — specifically a **transformer-based model**. Same family of architecture as GPT, Claude, BERT.
- **Input:** text (a string, up to the model's token limit) — **variable length**
- **Output:** a vector of floats — **FIXED dimensions, determined by the model, NOT by the input**
    - `"cat"` → 1536 floats
    - `"The quick brown fox jumps over the lazy dog"` → 1536 floats
    - A 500-word product description → 1536 floats
    - All identical output shape from `text-embedding-3-small`. The input length does NOT change the output dimensions.
- **Why this is the whole point:** the model maps *variable-length text → fixed-size vector*. This is what makes cosine similarity, nearest-neighbor search, and vector store indexing possible — every vector lives in the SAME dimensional space and can be compared.
- **Text in, vector out.**

### What's a "neural network" (one sentence)

- A neural network is a **function** that maps inputs to outputs by passing them through layers of weighted math operations, where the **weights are learned from data during training** rather than hand-coded by a programmer.
- The weights ARE the model's knowledge. **Training** = adjusting weights until the function produces useful outputs. **Inference** = feeding inputs through the now-fixed weights to get outputs.

### What's a "transformer" (one sentence)

- A transformer is a specific neural network **architecture** (introduced in the 2017 paper *"Attention Is All You Need"*) that processes entire sequences at once using a mechanism called **self-attention** — each position in the input "looks at" every other position and figures out how relevant they are to each other.
- **Why this matters for embeddings:** self-attention is exactly what lets the model understand WHOLE-SEQUENCE meaning (the passage-level-not-word-level gotcha from chunk 1). Older architectures (RNNs, LSTMs) processed sequences one token at a time and lost information across long inputs. Transformers see the whole thing at once — which is why modern embedding models capture nuanced meaning that pre-2018 models couldn't.

### How the model learned to do this

- Trained on **billions of words**. The training objective rewards the model for producing vectors where **semantically similar text -> similar vectors** and dissimilar text -> distinct vectors. Different models use different training approaches but the *result* is always the same: a function that maps text -> meaningful geometry
- **Interview-level summary:** *trained on a huge text corpus with a similarity preserving objective*

### In practice - what API calls look like

- You make a request (or run a local model) and get back a vector:

    # Pseudo-code shape — modern OpenAI SDK (v1.x, instance-based)
    from openai import OpenAI
    client = OpenAI()  # auto-reads OPENAI_API_KEY from env

    response = client.embeddings.create(
        model="text-embedding-3-small",
        input="how do I reset my password"
    )

    vector = response.data[0].embedding   # [0.012, -0.084, ..., 0.043]  (1536 floats)

    # NOTE: pre-2023 tutorials show `openai.embeddings.create(...)` — that's the legacy v0.x
    # module-based API and DOES NOT work in modern SDKs. Always use a client instance.

- 3 practical things to know:
    - **You pay per token**
    - **Latency**: typically 50-300ms per call. **Batching** multiple inputs in one API call is the big speedup
    - **Token limit:** every embedding model has a max input length, typically in the low thousands of tokens. Long docs must be chunked first (which is why "chunking strategies" is a whole sub-topic in RAG architecture).
        - *Reference (Tier 3): text-embedding-3-small caps at 8191 tokens (~6000 words). Look up your model's specific limit when you actually need it.*

### Cosine similarity 

- **Cosine similarity** = the metric that scores how close two embeddings are in meaning. 
  - Output is a single number
  - Higher number = more similar 
- It measures **direction alignment** between two vectors, which is why a one-word query and a long document about the same topic still score as similar
- It is what powers **top-k retrieval:** embed the query, score it against every stored vector, return the highest-scoring docs

### Dimensionality

- **Dimensionality** = how many numbers are in each vector (text-embedding-3-small = 1536, large = 3072)
- The one mental model that matters:
  - **More dimensions = more capacity to capture nuance, but more storage + slower search + higher cost**
  - Fewer dimensions = cheaper and faster, but coarser meaning
  - It's a **knob**: bigger isn't automatically better - you pick based on whether your task needs fine semantic distinctions or just rough topical matching 

- **Interview takeaway:** more dimensions cost more to store and search; you match the model to the precision the task actually needs 

### Common embedding models & trade-offs

- **Hosted API** (OpenAI) vs, **open-source self-hosted** (sentence-transformers, BGE, E5)
  - Hosted = simple, pay per token, data leaves your network
  - Self-hosted = free per call + data stays in-house, but you run the infra
- **Axes you trade on:** quality / cost / latency/ dimensions / max input tokens / data privacy
- Switching models = **Re-embedding your entire corpus**

- **Interview takeaway:** *"Start hosted (OpenAI) for simplicity; move to self-hosted open-source when cost at scale, latency, or data-privacy requirements justify running your own*

