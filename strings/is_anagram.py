# Given two strings s and t , write a function to determine if t is an anagram of s.

# Example 1:

# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:

# Input: s = "rat", t = "car"
# Output: false
# Note:
# You may assume the string contains only lowercase alphabets.

# Follow up:
# What if the inputs contain unicode characters? How would you adapt your solution to such case?


def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    s = list(s)
    t = list(t)
    s.sort()
    t.sort()

    for i in range(len(s)):
        if s[i] != t[i]:
            return False

    return True


print(isAnagram("anagram", "nagaram"))
