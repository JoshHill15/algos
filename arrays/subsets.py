# Given a set of distinct integers, nums, return all possible subsets (the power set).

# Note: The solution set must not contain duplicate subsets.

# Example:

# Input: nums = [1,2,3]
# Output:
# [
#   [3],
#   [1],
#   [2],
#   [1,2,3],
#   [1,3],
#   [2,3],
#   [1,2],
#   []
# ]


def subsets(nums):
    ans = [[]]

    if not nums:
        return ans[0]

    for i in range(1, len(nums)+1):
        left = 0
        right = i
        while right <= len(nums):
            sl = nums[left:right]
            ans.append(sl)
            right += 1
            left += 1

    return ans


def s(nums):
    ans = [[]]
    for num in nums:
        for i in range(len(ans)):
            ans.append(ans[i] + [num])


print(subsets([1, 2, 3]))
print(s([1, 2, 3]))
