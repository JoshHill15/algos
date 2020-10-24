class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        node = head
        while k:
            while node.next and node.next.next:
                node = node.next

            new_head = node.next
            if not new_head:
                return head
            node.next = None
            new_head.next = head
            node = new_head
            head = node
            k -= 1

        return new_head


head = ListNode(1)
# head.next = ListNode(2)
# head.next.next = ListNode(3)
# head.next.next.next = ListNode(4)
# head.next.next.next.next = ListNode(5)


x = Solution().rotateRight(head, 1)

while x:
    print(x.val)
    x = x.next
