# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Example:

# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(l1, l2):
    dummy = cur = ListNode(0)
    carry = 0
    while l1 or l2 or carry:
        if l1:
            carry += l1.val
            l1 = l1.next
        if l2:
            carry += l2.val
            l2 = l2.next
        cur.next = ListNode(carry % 10)
        cur = cur.next
        carry //= 10

    return dummy.next


a = ListNode(2)
a.next = ListNode(4)
a.next.next = ListNode(3)

b = ListNode(5)
b.next = ListNode(6)
b.next.next = ListNode(4)

node = addTwoNumbers(a, b)
while node:
    print(node.val)
    node = node.next


def addTwoNumbers2(self, l1: ListNode, l2: ListNode) -> ListNode:
    a = ""
    b = ""
    while l1 or l2:
        if l1:
            a = str(l1.val) + a
            l1 = l1.next
        if l2:
            b = str(l2.val) + b
            l2 = l2.next

    a = int(a)
    b = int(b)
    total = a+b
    total = str(total)
    i = len(total)-1

    final = temp = ListNode()
    while i >= 0:
        temp.next = ListNode(total[i])
        temp = temp.next
        i -= 1

    return final.next
