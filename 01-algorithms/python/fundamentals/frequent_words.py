def frequent_words(words: list[str]) -> dict[str, int]:

    words_dict = {}
    # # loop through array and create a dict (hash map) of words, store the word, if the word has been seen add +1 to it
    for word in words:
        words_dict[word] = words_dict.get(word, 0) + 1  # < -- better one-liner
        # if word in words_dict:
        #     words_dict[word] += 1
        # else:
        #     words_dict[word] = 1

    # # if the count of each word is > 1, return it in a dict
    # filtered_word_counts = {}
    # for word in words_dict:
    #     if words_dict[word] > 1:
    #         filtered_word_counts[word] = words_dict[word]
    #         pass

    filtered_word_counts = {
        word: count for word, count in words_dict.items() if count > 1
    }

    return filtered_word_counts


# Test cases
print(frequent_words(["apple", "banana", "apple", "cherry", "banana", "apple"]))
# Expected: {"apple": 3, "banana": 2}

print(frequent_words(["hello", "world"]))
# Expected: {}

print(frequent_words(["a", "a", "a", "b", "b", "c"]))
# Expected: {"a": 3, "b": 2}

print(frequent_words([]))
# Expected: {}
