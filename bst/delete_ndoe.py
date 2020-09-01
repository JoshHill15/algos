from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""
            5
           / \
          3   6
         / \   \
     ls 2rs 4   7

"""


def in_order_print(node):
    if node:
        in_order_print(node.left)
        print(node.val)
        in_order_print(node.right)


def delete_node(node, key):
    if not node:
        return

    if node.val == key:
        print(node.val)
        if node.left:
            left = node.left

        if node.right:
            node = node.right

        print(node.val)
        if left:
            node.left = left

        return

    delete_node(node.left, key)
    delete_node(node.right, key)


class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root or root.val == key:
            return None

        node = root
        delete_node(node, key)
        return root


root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(6)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right.right = TreeNode(7)

# in_order_print(Solution().deleteNode(root, 3))


def buildtree(nums, left, right):
    if left > right:
        return None

    mid = left + (right-left) // 2
    v = nums[mid]
    root = TreeNode(v)
    root.left = buildtree(nums, left, mid-1)
    root.right = buildtree(nums, mid+1, right)
    return root


class Solution1:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return

        left, right = 0, len(nums)-1
        return buildtree(nums, left, right)


# Solution1().sortedArrayToBST([-10, -3, 0, 5, 9])

"""
    0
   / \
  3 
 /  
10    

"""


class Solution2:
    def romanToInt(self, s):

        romans = {'M': 1000, 'D': 500, 'C': 100,
                  'L': 50, 'X': 10, 'V': 5, 'I': 1}

        prev_value = running_total = 0

        for i in range(len(s)-1, -1, -1):
            int_val = romans[s[i]]
            if int_val < prev_value:
                running_total -= int_val
            else:
                running_total += int_val
            prev_value = int_val

        return running_total


# print(Solution2().romanToInt("VI"))


def expand(s, l, r):
    while l >= 0 and r < len(s) and s[l] == s[r]:
        l -= 1
        r += 1

    return s[l+1:r]


class Solution3:
    def longestPalindrome(self, s):
        res = ""
        for i in range(len(s)):
            res = max(res, expand(s, i, i), expand(s, i, i+1), key=len)

        return res


print(Solution3().longestPalindrome("babad"))
