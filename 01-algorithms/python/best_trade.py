"""
Problem: Best Trade Window

You're given an array of stock prices indexed by day, where prices[i]
is the price on day i.

You're allowed to:
  - Buy ONCE on some day.
  - Sell ONCE on a LATER day (strictly later, not the same day).

Return the MAXIMUM PROFIT you can achieve.
If no profit is possible, return 0.

Constraints:
  - 1 <= len(prices) <= 10^5
  - 0 <= prices[i] <= 10^4

Examples:
  best_trade([7, 1, 5, 3, 6, 4]) -> 5    # buy at 1, sell at 6
  best_trade([7, 6, 4, 3, 1])    -> 0    # prices only decrease, no profit
  best_trade([1, 2])             -> 1    # smallest valid case with profit
  best_trade([5])                -> 0    # only one day, can't buy + sell

Aim for O(n) time and O(1) extra space.
"""

from typing import List


def best_trade(prices: List[int]) -> int:
    if len(prices) <= 1:
        return 0

    running_state = prices[0]  # min seen so far
    running_total = 0  # max profit

    for price in prices[1:]:
        running_total = max(running_total, price - running_state)
        print(f"running total: {running_total}")
        running_state = min(running_state, price)
        print(f"optimal number: {running_state}")

    return running_total


if __name__ == "__main__":
    # Quick sanity checks while developing
    print(best_trade([7, 1, 5, 3, 6, 4]))  # expected: 5
    # print(best_trade([7, 6, 4, 3, 1]))      # expected: 0
    # print(best_trade([1, 2]))               # expected: 1
    # print(best_trade([5]))  # expected: 0
