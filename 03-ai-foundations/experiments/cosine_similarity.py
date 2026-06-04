"""
cosine_similarity.py — watch "meaning becomes geometry" with your own data.

Reuses the 5 sentences from embeddings_demo.py. Computes cosine similarity for
every unique pair and prints the scores. Expectation:
  - bank/loan  (SENTENCES[0] & [1])  -> HIGH  (same meaning, zero shared keywords)
  - dog/puppy  (SENTENCES[2] & [3])  -> HIGH
  - anything vs the flour recipe       -> LOW
"""

import math
from openai import OpenAI
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
client = OpenAI()

MODEL = "text-embedding-3-small"

SENTENCES = [
    "The bank approved my loan",
    "The financial institution accepted my application",
    "The dog chased the ball through the park",
    "My puppy ran after the toy in the garden",
    "The recipe calls for two cups of flour",
]


# ---------------------------------------------------------------
# PROVIDED — cosine similarity (Tier 3 math, no need to memorize)
# ---------------------------------------------------------------
# Direction alignment of two vectors, ignoring their length:
#   dot product of a & b, divided by (magnitude of a * magnitude of b).
# Output is a single float: higher = more similar in meaning.
def cosine_similarity(a, b):
    dot = sum(x * y for x, y in zip(a, b))
    mag_a = math.sqrt(sum(x * x for x in a))
    mag_b = math.sqrt(sum(x * x for x in b))
    return dot / (mag_a * mag_b)


# ---------------------------------------------------------------
# TODO 1 — Embed all sentences
# ---------------------------------------------------------------
# Make ONE batched API call to embed every sentence in SENTENCES.
# Return a clean list of vectors (List[List[float]]) — strip the OpenAI
# wrapper like you did in embeddings_demo.py (the `[d.embedding for d in ...]` trick).
def embed_all():
    response = client.embeddings.create(model=MODEL, input=SENTENCES)
    vector_list = response.data
    embeddings = [d.embedding for d in vector_list]

    return embeddings


# ---------------------------------------------------------------
# TODO 2 — Pairwise comparison
# ---------------------------------------------------------------
# Given the list of vectors, compare every UNIQUE pair (don't compare a
# sentence to itself, and don't print both A-B and B-A).
# For each pair, print the two sentences and their cosine similarity score.
# Hint: a nested loop where the inner index starts ahead of the outer one
#   (for i ... for j in range(i + 1, len(...))) gives you unique pairs.
def compare_all(vectors):
    for i in range(len(vectors)):
        for j in range(i + 1, len(vectors)):
            score = cosine_similarity(vectors[i], vectors[j])
            print(f"{score:.3f}  |  {SENTENCES[i]!r}  vs  {SENTENCES[j]!r}")


if __name__ == "__main__":
    vectors = embed_all()
    compare_all(vectors)
