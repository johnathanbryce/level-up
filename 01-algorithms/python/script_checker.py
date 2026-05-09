"""
A code formatter tool needs to validate submitted scripts before formatting them.
Check whether all bracket characters in the script string are properly matched and closed.

Return True if every opening bracket has a corresponding closing bracket in the
correct order, False otherwise. Only (, ), [, ], {, } matter — ignore all other characters.

Constraints:
- 0 <= len(script) <= 10,000
- Input can contain any characters (letters, spaces, punctuation) — only brackets count
"""


# Pattern: Stack (LIFO — push openers, pop + match on closers)
def is_valid_script(script: str) -> bool:

    brackets_map = {"(": ")", "[": "]", "{": "}"}
    brackets_stack = []

    for bracket in script:
        opening_brackets = brackets_map.keys()
        if bracket in opening_brackets:
            brackets_stack.append(bracket)
        elif bracket in brackets_map.values():
            if len(brackets_stack) == 0:
                return False
            top_of_bracket = brackets_stack.pop()
            if brackets_map[top_of_bracket] != bracket:
                return False

    return len(brackets_stack) == 0


# --- tests ---
print(is_valid_script("([]{})") == True)  # all matched, nested
print(is_valid_script("([)]") == False)  # wrong close order
print(is_valid_script("{[]}") == True)  # nested curly
print(is_valid_script("(((") == False)  # never closed
print(is_valid_script("") == True)  # empty string
print(is_valid_script("a+b*(c-d)") == True)  # non-bracket chars ignored
print(is_valid_script("]") == False)  # close with nothing open
