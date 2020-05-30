# Given a 32-bit signed integer, reverse digits of an integer.

# Example 1:

# Input: 123
# Output: 321
# Example 2:

# Input: -123
# Output: -321
# Example 3:

# Input: 120
# Output: 21
# Note:
# Assume we are dealing with an environment which could only store integers
#  within the 32-bit signed integer range: [−231,  231 − 1].
#  For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.


def reverse(x: int) -> int:
    maxpos = (2**31)-1
    maxneg = -2**31

    if x >= maxpos or x <= maxneg:
        return 0

    x = str(x)
    negative = False
    if x[0] == "-":
        x = x[1:]
        negative = True

    rev = x[::-1]
    if negative:
        rev = "-" + rev
        rev = int(rev)
        return rev if rev > maxneg else 0
    else:
        rev = int(rev)
        return rev if rev < maxpos else 0


print(reverse(-123))
