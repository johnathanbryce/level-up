"""
Coupon Combo Finder

You're a backend engineer on a promo-codes service. When a customer stacks
two coupons, the promo engine multiplies their rates together to produce
the final multiplier.

Given a list of coupon rates (integers) and a target rate, return the
indexes [i, j] of two coupons whose rates multiply to exactly the target.

Rules
- Each coupon can only be used once — you can't pair an index with itself.
- Return any one valid pair (the first you find is fine).
- If no such pair exists, return an empty list [].

Examples
- rates=[2, 4, 3, 6],  target=12  ->  [0, 3]   (2 * 6 = 12)
- rates=[5, 2, 8, 1],  target=10  ->  [0, 1]   (5 * 2 = 10)
- rates=[1, 2, 3],     target=100 ->  []
- rates=[4, 4],        target=16  ->  [0, 1]   (4 * 4 = 16, different indexes)

Think about
- What happens if a rate doesn't divide cleanly into the target?
- What if rates contains 0?
"""


def coupon_combo(rates: list[int], target: int) -> list[int]:
    # track rates in a map with key-value pair of rate: index
    seen_rates = {}

    # what is the difference between the target / curr_num?
    # does it exist in rates? if so, find it
    for i, rate in enumerate(rates):
        complement = target / rate

        # have I previously seen a rate that, multiplied by the current one, equals the target?
        if complement in seen_rates:
            return [seen_rates[complement], i]

        if (
            complement.is_integer()
        ):  # do not add floats (rates that don't divide cleanly into target)
            seen_rates[rate] = i

    return []


print(coupon_combo([2, 4, 3, 6], 12))  # expect [1, 2]
print(coupon_combo([5, 2, 8, 1], 10))  # expect [0, 1]
print(coupon_combo([1, 2, 3], 100))  # expect []
print(coupon_combo([4, 4], 16))  # expect [0, 1]
