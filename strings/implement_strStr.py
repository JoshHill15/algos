# Implement strStr().

# Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

# Example 1:

# Input: haystack = "hello", needle = "ll"
# Output: 2
# Example 2:

# Input: haystack = "aaaaa", needle = "bba"
# Output: -1
# Clarification:

# What should we return when needle is an empty string? This is a great question to ask during an interview.

# For the purpose of this problem, we will return 0 when needle is an empty string.
# This is consistent to C's strstr() and Java's indexOf().


def strStr(haystack: str, needle: str) -> int:
    needle_len = len(needle)
    if len(needle) < 1:
        return 0

    if len(haystack) < 1:
        return -1

    i = 0
    while needle_len <= len(haystack):
        sliding_window = haystack[i:needle_len]
        if sliding_window == needle:
            return i

        i += 1
        needle_len += 1

    return -1


haystack = "hello"
needle = "ll"

print(strStr(haystack, needle))
