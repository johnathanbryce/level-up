# Pattern: Frequency Counting (count-then-inspect)
# Challenge: Concert Headliner Vote Counter
#
# You work for a music festival. Fans have been submitting votes for which
# band should headline the main stage. A band earns a headliner slot if they
# receive at least k votes.
#
# Given a list of votes and a minimum vote threshold k, return a list of all
# bands that qualified (received >= k votes), sorted alphabetically.
# If no band qualifies, return an empty list.
#
# Examples:
#   votes = ["radiohead", "arcade fire", "radiohead", "lcd soundsystem",
#            "arcade fire", "radiohead", "lcd soundsystem", "arcade fire"]
#   k = 3
#   → ["arcade fire", "radiohead"]
#     (radiohead: 3 ✓, arcade fire: 3 ✓, lcd soundsystem: 2 ✗)
#
#   votes = ["band_a", "band_b", "band_a"]
#   k = 5
#   → []
#
#   votes = ["tame impala"]
#   k = 1
#   → ["tame impala"]
#
# Constraints:
#   - votes is a non-empty list of strings
#   - k >= 1
#   - Band names are lowercase strings, may contain spaces
#   - Output must be sorted alphabetically (A → Z)
#   - Do NOT use list.count() — target O(n)

from collections import Counter


def headliner_votes(votes, k):

    counts = Counter(votes)
    bands = []

    for band, count in counts.items():

        if count >= k:
            bands.append(band)

    bands.sort()
    return bands


print(
    headliner_votes(
        [
            "radiohead",
            "arcade fire",
            "radiohead",
            "lcd soundsystem",
            "arcade fire",
            "radiohead",
            "lcd soundsystem",
            "arcade fire",
        ],
        3,
    )
)  # → ["arcade fire", "radiohead"]

print(headliner_votes(["band_a", "band_b", "band_a"], 5))  # → []

print(headliner_votes(["tame impala"], 1))  # → ["tame impala"]

print(
    headliner_votes(["muse", "muse", "blur", "blur", "muse", "blur"], 2)
)  # → ["blur", "muse"]
