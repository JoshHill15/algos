# Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

# Note:

# The number of elements initialized in nums1 and nums2 are m and n respectively.
# You may assume that nums1 has enough space(size that is greater or equal to m + n) to hold additional elements from nums2.
# Example:

# Input:
# nums1 = [1, 2, 3, 0, 0, 0], m = 3
# nums2 = [2, 5, 6],       n = 3

# Output: [1, 2, 2, 3, 5, 6]


def merge(nums1, m, nums2, n):
    """
    :type nums1: List[int]
    :type m: int
    :type nums2: List[int]
    :type n: int
    :rtype: None Do not return anything, modify nums1 in-place instead.
    """
    if len(nums1) == 0 or len(nums2) == 0:
        return
    limit = n+m
    a = 0
    i = 0
    while i < limit:
        if nums1[i] == 0 and a < len(nums2):
            nums1[i] = nums2[a]
            a += 1
        i += 1
    nums1.sort()


nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3
print(nums1)
merge(nums1, m, nums2, n)
print(nums1)