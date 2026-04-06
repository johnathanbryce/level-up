def first_unique(s: str) -> str:

    if not s:
        return ""

    char_count_map = {}
    # loop over str and count each char in a hash map

    for char in s:

        # add char to map with value of 1
        if char in char_count_map:
            char_count_map[char] += 1
        else:
            char_count_map[char] = 1

    # second loop go over the char hash map and find the first char with count == 1
    # if char count <= 1 return that char as the value
    # if all chars > 1 return empty str

    for key, value in char_count_map.items():
        if value == 1:
            return key
    return ""


# first_unique("aabcbd")
# first_unique("aabbcc")
first_unique("abcabc")
