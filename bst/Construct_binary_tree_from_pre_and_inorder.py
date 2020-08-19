class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def buildTree(preorder, inorder):
    if inorder:
        ind = inorder.index(preorder.pop(0))
        root = TreeNode(inorder[ind])
        root.left = buildTree(preorder, inorder[0:ind])
        root.right = buildTree(preorder, inorder[ind+1:])
        return root


def in_order_print(root):
    if root:
        in_order_print(root.left)
        print(root.val)
        in_order_print(root.right)


preorder = [3, 9, 20, 15, 7]
inorder = [9, 3, 15, 20, 7]

in_order_print(buildTree(preorder, inorder))
