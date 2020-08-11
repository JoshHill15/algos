# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        l = self.maxDepth(root.left)
        r = self.maxDepth(root.right)

        if l > r:
            return l+1
        else:
            return r+1


node = TreeNode(3)
node.left = TreeNode(9)
node.right = TreeNode(20)
node.right.right = TreeNode(7)
node.right.left = TreeNode(15)

print(Solution().maxDepth(node))
