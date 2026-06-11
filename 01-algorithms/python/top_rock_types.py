"""
A field geologist hands you a flat list of rock-type labels — one entry per
sample logged during a drill program. You want to know which rock types show
up most often.

Write a function that returns the `k` most frequently occurring rock types,
ordered from most common to least common.

  - If two rock types tie on count, either order between them is fine.
  - Assume `k` is always <= the number of distinct rock types.
  - Return a list of just the rock-type strings (not the counts).

Examples:
  top_rock_types(["granite", "basalt", "granite", "shale", "basalt", "granite"], 2)
      -> ["granite", "basalt"]        # granite x3, basalt x2, shale x1

  top_rock_types(["shale"], 1)
      -> ["shale"]

  top_rock_types(["a", "b", "c", "a", "b", "a"], 1)
      -> ["a"]
"""


def top_rock_types(rock_types: list[str], k: int) -> list[str]:
    # 1 count each rock type into a hash map
    rocks = {}
    for rock in rock_types:
        # if rock doesn't exit, add it to rock dict with key-val pair of rock: 1
        rocks[rock] = rocks.get(rock, 0) + 1
    # 2. rank keys by their count (descending), then take the top k
    sorted_rocks = sorted(rocks, key=lambda r: rocks[r], reverse=True)[:k]
    return sorted_rocks


# --- test cases ---
print(top_rock_types(["granite", "basalt", "granite", "shale", "basalt", "granite"], 2))
print(top_rock_types(["shale"], 1))
print(top_rock_types(["a", "b", "c", "a", "b", "a"], 1))
print(top_rock_types(["x", "x", "y", "y", "z"], 3))
