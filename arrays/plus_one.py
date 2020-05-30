# Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

# The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

# You may assume the integer does not contain any leading zero, except the number 0 itself.

# Example 1:

# Input: [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.
# Example 2:

# Input: [4,3,2,1]
# Output: [4,3,2,2]
# Explanation: The array represents the integer 4321.


def plusOne(digits):
    s = ""
    for d in digits:
        s += str(d)

    s = int(s)
    new_num = s+1
    string_num = str(new_num)
    return list(string_num)


print(plusOne([1, 2, 3]))
