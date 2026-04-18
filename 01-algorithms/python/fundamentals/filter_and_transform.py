def filter_and_transform(nums: list[int]) -> list[int]:

    return [num**2 for num in nums if num % 2 == 0]


input1 = [1, 2, 3, 4, 5, 6, 7, 8]
# Output: [4, 16, 36, 64]

input2 = [11, 13, 15]
# Output: []

input3 = [2]
# Output: [4]

print(filter_and_transform(input1))


def filter_and_transform_loop(nums: list[int]) -> list[int]:

    transformed = []
    for num in nums:
        if num % 2 == 0:
            squared_num = num**2
            transformed.append(squared_num)

    return transformed


print(filter_and_transform_loop(input1))
