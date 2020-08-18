class LinkedListNode(object):

    def __init__(self, value):
        self.value = value
        self.next = None


head = LinkedListNode(3)
head.next = LinkedListNode(5)
head.next.next = LinkedListNode(6)
head.next.next.next = LinkedListNode(9)
f = LinkedListNode(100)


def rev(node):
    prev = None

    while node:
        nxt = node.next
        node.next = prev
        prev = node
        node = nxt

    return prev


a = head
a = rev(head)

while a:
    print(a.value)
    a = a.next
