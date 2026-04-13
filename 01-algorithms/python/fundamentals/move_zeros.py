# naive approach
def move_zeros(nums: list[int]) -> None:
    result = []
    zeros_arr = []
    for num in nums:
        if num == 0:

            zeros_arr.append(num)
        else:
            result.append(num)

    result.extend(zeros_arr)
    nums[:] = result
    return


nums = [0, 1, 0, 3, 12]
move_zeros(nums)
# print(nums)  # [1, 3, 12, 0, 0]


# 2 pointer approach
def move_zeros_two_pointer(nums: list[int]) -> None:
    writer = 0
    # phase 1: shift non-zeros forward
    for reader in range(len(nums)):
        if nums[reader] != 0:
            nums[writer] = nums[reader]
            writer += 1
    # phase 2: fill the tail with zeros
    for i in range(writer, len(nums)):
        nums[i] = 0
    return


nums = [0, 1, 0, 3, 12]
move_zeros_two_pointer(nums)
