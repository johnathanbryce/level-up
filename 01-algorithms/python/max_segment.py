"""
Problem: Max Segment Sum

Given an array of integers (which can be positive, negative, or zero),
find the contiguous segment with the LARGEST sum. Return that sum.

A "segment" is a non-empty slice of consecutive elements.

Constraints:
  - 1 <= len(arr) <= 10^5
  - -10^4 <= arr[i] <= 10^4
  - At least one element is guaranteed.

Examples:
  max_segment([-2, 1, -3, 4, -1, 2, 1, -5, 4])  -> 6      # segment [4, -1, 2, 1]
  max_segment([1])                                -> 1
  max_segment([5, 4, -1, 7, 8])                   -> 23     # the whole array
  max_segment([-1, -2, -3])                       -> -1     # best is the single largest negative
  max_segment([-5, -1, -2])                       -> -1

Aim for O(n) time and O(1) extra space.

Hint (no spoilers): same pattern family as best_trade.py — apply the
running-state mental model. But the running state here behaves differently
from "running min." Ask yourself: what's the ONE piece of state I need
from the past to decide my answer at the current position?
"""

from typing import List


def max_segment(arr):
    running_sum = arr[0]  # start the segment at the first element
    max_sum = arr[0]  # the best we've seen is AT LEAST arr[0]

    for num in arr[1:]:
        # extend OR restart, whichever is better
        running_sum = max(num, running_sum + num)

        # update the best segment-sum seen so far
        max_sum = max(max_sum, running_sum)

    return max_sum


if __name__ == "__main__":
    print(max_segment([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # expected: 6
    # print(max_segment([1]))                                # expected: 1
    # print(max_segment([5, 4, -1, 7, 8]))                   # expected: 23
    # print(max_segment([-1, -2, -3]))                       # expected: -1
    # print(max_segment([-5, -1, -2]))                       # expected: -1
