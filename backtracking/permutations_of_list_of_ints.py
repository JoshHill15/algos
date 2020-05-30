# Given a collection of distinct integers, return all possible permutations.

# Example:

# Input: [1,2,3]
# Output:
# [
#   [1,2,3],
#   [1,3,2],
#   [2,1,3],
#   [2,3,1],
#   [3,1,2],
#   [3,2,1]
# ]


def dfs(nums, res, path):
    if len(nums) < 1:
        res.append(path)

    for i in range(len(nums)):
        dfs(nums[:i]+nums[i+1:], res, path+[nums[i]])


def permute(nums):
    res = []
    dfs(nums, res, [])
    return res


print(permute([1, 2, 3]))
