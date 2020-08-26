from collections import Counter
import heapq


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def sums_left(self, total, node):
        if not node:
            return

        if node.left and not node.left.left and not node.left.right:
            total[0] += node.left.val

        self.sums_left(total, node.left)
        self.sums_left(total, node.right)

    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        total = [0]
        self.sums_left(total, root)
        return total[0]


root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)


# print(Solution().sumOfLeftLeaves(root))


def output(elements):
    heap = []
    element_to_frequency = Counter(elements)
    elements = []

    for element, frequency in element_to_frequency.items():
        heapq.heappush(heap, (frequency, element))

    while heap:
        frequency, element = heapq.heappop(heap)
        elements.extend([element] * frequency)
    print(elements)
    return elements


print(output([3, 4, 2, 5, 2, 3, 4, 3, 6]) == [6, 5, 4, 4, 2, 2, 3, 3, 3])
print(output([7, 7, 7, 7, 2, 2, 3, 3, 1, 1, 9, 6, 6, 6, 6])
      == [9, 3, 3, 2, 2, 1, 1, 7, 7, 7, 7, 6, 6, 6, 6])
