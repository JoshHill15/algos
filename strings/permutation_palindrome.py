# Write an efficient function that checks whether any permutation ↴ of an input string is a palindrome. ↴

# You can assume the input string only contains lowercase letters.

# Examples:

# "civic" should return True
# "ivicc" should return True
# "civil" should return False
# "livci" should return False
# "But 'ivicc' isn't a palindrome!"

# If you had this thought, read the question again carefully.
#  We're asking if any permutation of the string is a palindrome.
# Spend some extra time ensuring you fully understand the question before starting.
# Jumping in with a flawed understanding of the problem doesn't look good in an interview.


def permuation_palindrome(s):
    hm = {}
    single_letter = 0

    for letter in s:
        if letter not in hm:
            hm[letter] = 0

        hm[letter] += 1

    for key in hm:
        if hm[key] % 2 != 0:
            single_letter += 1

    even = True if len(s) % 2 == 0 else False

    if single_letter and even:
        return False

    elif not single_letter and even:
        return True

    return True if single_letter == 1 else False


print(permuation_palindrome("iicvc"))  # True
print(permuation_palindrome("civic"))  # True
print(permuation_palindrome("civil"))  # False
print(permuation_palindrome("livci"))  # False
print(permuation_palindrome("abba"))  # True
