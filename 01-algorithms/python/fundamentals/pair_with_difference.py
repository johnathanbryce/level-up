def pair_with_difference_k(nums: list[int], k: int) -> bool:
    seen_nums = set()

    for num in nums:
        smaller_candidate = num - k
        larger_candidate = num + k

        if smaller_candidate in seen_nums or larger_candidate in seen_nums:
            return True

        # Add AFTER check — set must only hold numbers from previous iterations
        seen_nums.add(num)

    return False


print(pair_with_difference_k([1, 5, 3, 8], 2))  # True  (5 - 3 = 2)
print(pair_with_difference_k([1, 5, 3, 8], 10))  # False
print(pair_with_difference_k([4, 4, 4], 0))  # True  (two different 4s)
print(pair_with_difference_k([1, 2, 3], 5))  # False
print(pair_with_difference_k([7, 1, 5, 9, 2], 6))  # True  (7 - 1 = 6)
