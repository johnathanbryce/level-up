def pair_sums_loop(nums: list[int], target: int) -> list[tuple[int, int]]:

    # tracking arr
    unique_pairs = []

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                unique_pairs.append((nums[i], nums[j]))
    return unique_pairs


nums = [1, 2, 3, 4, 5]
target = 5

# pair_sums_loop(nums, target)

# nums = [1, 2, 3, 4, 5],  target = 5
# Output: [(1, 4), (2, 3)]

# Input:  nums = [3, 3, 5, 1],  target = 6
# Output: [(3, 3)]

# Input:  nums = [1, 2, 3],  target = 10
# Output: []


def pair_sums_list_comp(nums: list[int], target: int):

    return [
        (nums[i], nums[j])
        for i in range(len(nums))
        for j in range(i + 1, len(nums))
        if nums[i] + nums[j] == target
    ]


print(pair_sums_list_comp(nums, target))
