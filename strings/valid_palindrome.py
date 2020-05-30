# Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

# Note: For the purpose of this problem, we define empty string as valid palindrome.

# Example 1:

# Input: "A man, a plan, a canal: Panama"
# Output: true
# Example 2:

# Input: "race a car"
# Output: false


import re


def isPalindrome(s: str) -> bool:

    s = re.sub('[^0-9a-zA-Z]+', '', s)
    left = 0
    right = len(s) - 1

    while left < right:
        val1 = s[left].lower()
        val2 = s[right].lower()
        if val1 != val2:
            return False
        left += 1
        right -= 1

    return True


print(isPalindrome("A man, a plan, a canal: Panama"))
