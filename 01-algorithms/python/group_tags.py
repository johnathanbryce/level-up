"""
Warm-up — 2026-06-10

A content platform lets users attach free-form tags to posts. Moderation
discovers that some "different" tags are actually the same letters rearranged
(e.g. "listen", "silent", "enlist") and wants them collapsed into groups.

Write group_tags(tags) that takes a list of strings and returns a list of
groups, where each group contains all tags that are rearrangements of one
another (anagrams). The order of groups, and order within a group, does not
matter for correctness.

Example:
    group_tags(["listen", "silent", "google", "enlist", "banana"])
    -> [["listen", "silent", "enlist"], ["google"], ["banana"]]

    group_tags([]) -> []
    group_tags(["abc"]) -> [["abc"]]

Constraints:
    - tags may be empty
    - tags are lowercase a-z, no spaces
    - duplicates are possible ("ab", "ab") -> they belong in the same group
"""


def group_tags(tags):

    buckets = {}

    for tag in tags:
        signature = "".join(sorted(tag))

        if signature not in buckets:
            buckets[signature] = []

        buckets[signature].append(tag)

    # # Option A — setdefault: "give me the list for this key, creating [] if absent"
    # for tag in tags:
    #     signature = "".join(sorted(tag))
    #     buckets.setdefault(signature, []).append(tag)

    # # Option B — defaultdict: the dict auto-creates an empty list on first access
    # from collections import defaultdict

    # buckets = defaultdict(list)
    # for tag in tags:
    #     buckets["".join(sorted(tag))].append(tag)

    return buckets.values()


# ---- test harness (don't edit) ----
def _normalize(groups):
    """Sort within groups and across groups so comparison is order-independent."""
    return sorted(sorted(g) for g in groups)


def _check(actual, expected):
    ok = _normalize(actual) == _normalize(expected)
    print(f"{'PASS' if ok else 'FAIL'}: got {actual}")
    if not ok:
        print(f"      expected (any order): {expected}")


if __name__ == "__main__":
    _check(
        group_tags(["listen", "silent", "google", "enlist", "banana"]),
        [["listen", "silent", "enlist"], ["google"], ["banana"]],
    )
    _check(group_tags([]), [])
    _check(group_tags(["abc"]), [["abc"]])
    _check(group_tags(["ab", "ab", "ba"]), [["ab", "ab", "ba"]])
    pass
