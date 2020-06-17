# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

# Example 1:

# Input: ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
# Note:

# All given inputs are in lowercase letters a-z.


def longestCommonPrefix(strs):
    minL = min(map(len, strs)) if strs else 0
    for i in range(minL):
        for j in range(1, len(strs)):
            if strs[j][i] != strs[0][i]:
                return strs[0][:i]
    return strs[0][:minL] if minL else ""


a = ["flower", "flow", "flight"]
b = ["dog", "racecar", "car"]
c = ["cat", "cat", "cat"]
print(longestCommonPrefix(c))
