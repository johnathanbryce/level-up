def valid_anagram_sorted_approach(str1: str, str2: str) -> bool:
    # sort each string, if they equal each other True if not False
    sorted_str_one = "".join(sorted(str1))
    sorted_str_two = "".join(sorted(str2))

    return sorted_str_one == sorted_str_two


# print(valid_anagram_sorted_approach("listen", "silent"))  # true
# print(valid_anagram_sorted_approach("rat", "car"))  # false
# print(valid_anagram_sorted_approach("", ""))


def valid_anagram_manual_dict(str1: str, str2: str) -> bool:

    # accumulate and count letters in str1
    str_one_map = {}
    for char in str1:
        if char in str_one_map:
            str_one_map[char] += 1
        else:
            str_one_map[char] = 1

    # accumulate and count letters in str2
    str_two_map = {}
    for char in str2:
        if char in str_two_map:
            str_two_map[char] += 1
        else:
            str_two_map[char] = 1

    # letters and their counts (i.e. key-value pairs) must equal the same from both
    return str_one_map == str_two_map


# print(valid_anagram_manual_dict("listen", "silent"))  # true
# print(valid_anagram_manual_dict("aabccc", "cccbaa"))  # true
# print(valid_anagram_manual_dict("rat", "car"))  # false
# print(valid_anagram_manual_dict("", ""))


# stdlib version one-liner
from collections import Counter


def valid_anagram(s, t):
    return Counter(s) == Counter(t)


# print(valid_anagram("listen", "silent"))  # true
# print(valid_anagram("aabccc", "cccbaa"))  # true
# print(valid_anagram("rat", "car"))  # false
# print(valid_anagram("", ""))
