"""
embeddings_demo.py — make the abstract "text in, vector out" concrete.

Goals (reinforces chunk 1 + chunk 2):
  1. Make ONE embedding API call and inspect the result
  2. Batch multiple inputs in a SINGLE API call
  3. Confirm determinism — same input → same vector
"""

from openai import OpenAI
from dotenv import load_dotenv, find_dotenv

# Auto-find the .env by walking up the directory tree from this script's location
# (your .env is at the project root: /Users/johnbryce/dev/level-up/.env)
load_dotenv(find_dotenv())

# OpenAI client auto-reads OPENAI_API_KEY from the environment after load_dotenv()
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
# TODO 1 — Single embedding
# ---------------------------------------------------------------
# Make ONE API call to embed a single sentence (use SENTENCES[0]).
# Print:
#   - the length of the returned vector (should match the model's dimensions)
#   - the first 10 floats of the vector
# Hint: look at the pseudo-code in your notes (chunk 2, "In practice — API calls").
def single_embedding():
    # TODO
    response = client.embeddings.create(model=MODEL, input=SENTENCES[0])

    vector = response.data[0].embedding
    vector_len = len(vector)
    first_10_floats = [num for num in vector[:10]]
    return {"vector_leng": vector_len, "first_10_floats": first_10_floats}


# ---------------------------------------------------------------
# TODO 2 — Batched embeddings
# ---------------------------------------------------------------
# Make ONE API call that embeds ALL of SENTENCES in a single request.
# (Hint: the `input` parameter can be a list, not just a string.)
# Print:
#   - how many embeddings came back (should equal len(SENTENCES))
#   - the length of the first embedding
#   - confirm each embedding has the same length (loop + assert)
def batched_embeddings():
    response = client.embeddings.create(model=MODEL, input=SENTENCES)
    vector = response.data
    # 1.
    if len(SENTENCES) == len(vector):
        print(f"{len(vector)} embeddings")
    # 2.
    len_first_embedding = len(vector[0].embedding)
    print(len_first_embedding)
    # 3.
    for i, embedding in vector:
        print(f"EMBEDDING {i}: {embedding}")
    pass


# ---------------------------------------------------------------
# TODO 3 — Determinism
# ---------------------------------------------------------------
# Embed the SAME sentence twice in two SEPARATE API calls.
# Compare the two returned vectors — confirm they are exactly equal.
# (Hint: Python's `==` on lists of floats does element-wise comparison.)
def determinism_check():
    # TODO
    pass


if __name__ == "__main__":
    print("=== TODO 1: single embedding ===")
    single_embedding()
    print()

    print("=== TODO 2: batched embeddings ===")
    batched_embeddings()
    print()

    print("=== TODO 3: determinism ===")
    determinism_check()
