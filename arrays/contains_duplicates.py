# Given an array of integers, find if the array contains any duplicates.

# Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

# Example 1:

# Input: [1,2,3,1]
# Output: true
# Example 2:

# Input: [1,2,3,4]
# Output: false
# Example 3:

# Input: [1,1,1,3,3,4,3,2,4,2]
# Output: true


def containsDuplicate(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    if nums is None or len(nums) < 1:
        return False

    hm = {}
    for num in nums:
        if num in hm:
            hm[num] = False
        else:
            hm[num] = True

    for key in hm:
        if hm[key] == False:
            return True

    return False


print(containsDuplicate([1, 2, 3, 1]))
