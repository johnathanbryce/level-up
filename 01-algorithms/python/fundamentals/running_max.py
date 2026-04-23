def running_max(nums: list[int]) -> list[int]:
    # create a new array:
    running_max_arr = []

    curr_max = nums[0]  # the biggest number found thus far
    for num in nums:
        if num > curr_max:
            curr_max = num
            # if the curr value >= next value, "replace" the next val with the curr value
        running_max_arr.append(curr_max)

    return running_max_arr


print(running_max([3, 1, 4, 1, 5, 9, 2, 6]))  # [3, 3, 4, 4, 5, 9, 9, 9]
print(running_max([1, 2, 3, 4, 5]))  # [1, 2, 3, 4, 5]
print(running_max([5, 4, 3, 2, 1]))  # [5, 5, 5, 5, 5]
