# Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

# Examples:

# s = "leetcode"
# return 0.

# s = "loveleetcode",
# return 2.
# Note: You may assume the string contain only lowercase letters.


def firstUniqChar(s: str) -> int:
    hm = {}
    smallest = float("inf")
    for i, char in enumerate(s):
        if char not in hm:
            hm[char] = i
        else:
            hm[char] = "dup"

    for key in hm:
        if hm[key] != "dup" and hm[key] < smallest:
            smallest = hm[key]

    return smallest if smallest != float("inf") else -1


print(firstUniqChar("loveleetcode"))
