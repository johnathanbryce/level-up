def two_sum(nums: list[int], target: int) -> list[int]:

    seen_nums = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen_nums:
            # return the value of the found complement
            return [i, seen_nums[complement]]

        # seen_nums[i] = num
        seen_nums[num] = i

    return []


# Test cases
print(two_sum([2, 7, 11, 15], 9))  # expected: [0, 1]
print(two_sum([3, 2, 4], 6))  # expected: [1, 2]
print(two_sum([3, 3], 6))  # expected: [0, 1]
print(two_sum([-1, -2, -3, -4, -5], -8))  # expected: [2, 4]
