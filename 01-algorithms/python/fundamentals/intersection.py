def intersection(nums1: list[int], nums2: list[int]) -> list[int]:
    # count through each array and identify shared numbers

    seen_nums = set()
    similar_nums = set()  # build this for matching nums

    # loop through nums1 and build a set for each number in nums1
    for num in nums1:
        seen_nums.add(num)

    # loop through nums2 and if the corresponding number exists, append it to the similar_nums arr
    for num in nums2:
        if num in seen_nums:
            similar_nums.add(num)

    return list(similar_nums)


# print(intersection([1, 2, 2, 1], [2, 2]))  # [2]
# print(intersection([4, 9, 5], [9, 4, 9, 8, 4]))  # [9, 4] (any order)
# intersection([1, 2, 3], [4, 5, 6])  # []


# one-liner
def intersection_one_liner(nums1, nums2):
    return list(
        set(nums1) & set(nums2)
    )  # --> this is the same as writing set(nums1).intersection(set(nums2))


print(intersection_one_liner([1, 2, 2, 1], [2, 2]))
