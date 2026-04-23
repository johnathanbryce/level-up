def pair_products(nums: list[int], target: int) -> list[list[int]]:

    seen_nums = set()
    pairs = []
    for n in nums:
        complement = target // n

        if complement in seen_nums:
            pairs.append([complement, n])
            pass

        seen_nums.add(n)

    return pairs


# return all unique pairs [a, b] where a * b == target.

print(pair_products([2, 3, 4, 6, 8, 12], 24))  # [[2, 12], [3, 8], [4, 6]]
print(pair_products([5, 5, 24], 25))  # [[5, 5]]
print(pair_products([1, 2, 3], 10))  # []
