def running_sum(nums: list[int]) -> list[int]:

    result = []
    running_total = 0
    for num in nums:

        running_total += num
        result.append(running_total)

    return result


print(running_sum([1, 2, 3, 4]))  # [1, 3, 6, 10]
# running_sum([1, 1, 1, 1, 1])  # [1, 2, 3, 4, 5]
# running_sum([3, -1, 4, -2])  # [3, 2, 6, 4]
