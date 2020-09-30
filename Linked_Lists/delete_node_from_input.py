class LinkedListNode(object):

    def __init__(self, value):
        self.value = value
        self.next = None


a = LinkedListNode('A')
b = LinkedListNode('B')
c = LinkedListNode('C')

a.next = b
b.next = c


def delete_node(node_to_delete):
    # Get the input node's next node, the one we want to skip to
    next_node = node_to_delete.next

    if next_node:
        # Replace the input node's value and pointer with the next
        # node's value and pointer. The previous node now effectively
        # skips over the input node
        node_to_delete.value = next_node.value
        node_to_delete.next = next_node.next
    else:
        # Eep, we're trying to delete the last node!
        raise Exception("Can't delete the last node with this technique!")


delete_node(b)


while a:
    print(a.value)
    a = a.next
