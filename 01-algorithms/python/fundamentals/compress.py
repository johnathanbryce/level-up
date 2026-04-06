def compress(s: str) -> str:
    if not s:
        return ""
    # loop through the string and count the number of times each character appears in order

    current_char = s[0]
    curr_chat_count = 0
    new_str = ""

    for char in s:
        if char == current_char:
            curr_chat_count += 1

        else:
            if curr_chat_count == 1:
                new_str += current_char
            else:

                new_str += f"{current_char}{curr_chat_count}"
            current_char = char
            curr_chat_count = 1

    if curr_chat_count == 1:
        new_str += current_char
    else:
        new_str += f"{current_char}{curr_chat_count}"
    print(new_str)

    return new_str


# compress("aaabbc")
compress("abcd")
# compress("aaa")
