def first_unique_char(s):

    # loop over string and create a hash map (obj) counting key-value chars
    char_map = {}

    for char in s:
        # does char exist? add +1
        if char in char_map:

            curr_char_count = char_map[char]
            char_map[char] = curr_char_count + 1

        # else, add to char_map
        else:
            char_map[char] = 1
            
    # better one liner: char_map[char] = char_map.get(char,0) +1

    for i, char in enumerate(s):
        if char_map[char] == 1:
            return i

    return -1


print(first_unique_char("leetcode"))  # 0
print(first_unique_char("loveleetcode"))  # 2
print(first_unique_char("aabb"))  # -1
