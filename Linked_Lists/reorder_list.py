class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reorderList(self, head, last=None):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if head is None:
            return

        prev = ListNode()
        prev.next = node = head

        while node.next:
            prev = prev.next
            node = node.next

        prev.next = None
        last = node
        nxt = head.next
        head.next = last
        last.next = nxt

        self.reorderList(nxt, last)


node = ListNode(1)
node.next = ListNode(2)
node.next.next = ListNode(3)
node.next.next.next = ListNode(4)
node.next.next.next.next = ListNode(5)

Solution().reorderList(node)
while node:
    print(node.val)
    node = node.next
