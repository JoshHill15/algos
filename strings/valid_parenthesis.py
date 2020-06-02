# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Note that an empty string is also considered valid.

# Example 1:

# Input: "()"
# Output: true
# Example 2:

# Input: "()[]{}"
# Output: true
# Example 3:

# Input: "(]"
# Output: false
# Example 4:

# Input: "([)]"
# Output: false
# Example 5:

# Input: "{[]}"
# Output: true


def isValid(s: str) -> bool:
    stack = []
    if len(s) < 1:
        return True

    for paren in s:
        if paren == "(" or paren == "[" or paren == "{":
            stack.append(paren)

        elif paren == ")":
            if len(stack) == 0:
                return False

            v = stack.pop()
            if v != "(":
                return False

        elif paren == "]":
            if len(stack) == 0:
                return False
            v = stack.pop()
            if v != "[":
                return False

        elif paren == "}":
            if len(stack) == 0:
                return False
            v = stack.pop()
            if v != "{":
                return False

    return len(stack) == 0


print(isValid("([)]"))
