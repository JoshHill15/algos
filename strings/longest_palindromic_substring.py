# Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

# Example 1:

# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
# Example 2:

# Input: "cbbd"
# Output: "bb"
# Accepted
# 931,128
# Submissions
# 3,180,675


def isPalin(window):
    reverse = window[::-1]
    return window == reverse


def sw(a, left, right):
    while right <= len(a):
        window = a[left:right]
        if isPalin(window):
            return window

        right += 1
        left += 1

    return ""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = ""

        if len(s) == 1 or not s:
            return s

        a = list(s)

        for i in range(len(a), 0, -1):
            ans = sw(a, 0, i)

            if ans:
                return "".join(ans)

        return ans


s = Solution()
print(s.longestPalindrome("babad"))
