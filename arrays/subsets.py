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
    ans = [""]
    for num in nums:
        for i in range(len(ans)):
            ans.append(ans[i] + str(num))

    return ans


def s(nums):
    ans = [[]]
    for num in nums:
        for i in range(len(ans)):
            ans.append(ans[i] + [num])

    return ans


print(subsets([1, 2, 3]))
print(s([1, 2, 3]))
