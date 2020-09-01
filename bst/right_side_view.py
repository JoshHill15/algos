class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def rightSideView(root):
    def collect(node, depth):
        if node:
            if depth == len(view):
                view.append(node.val)
            collect(node.right, depth+1)
            collect(node.left, depth+1)
    view = []
    collect(root, 0)
    return view


root = TreeNode(1)
root.left = TreeNode(2)
# root.left.right = TreeNode(5)
# root.right = TreeNode(3)
# root.right.right = TreeNode(4)

print(rightSideView(root))
