

# Merge two sorted linked lists and return it as a new sorted list. The new list should be made by splicing together the nodes of the first two lists.

# Example:

# Input: 1->2->4, 1->3->4
# Output: 1->1->2->3->4->4


def mergeTwoLists(l1, l2):
    temp = None

    if l1 is None:
        return l2
    if l2 is None:
        return l1

    if l1.val < l2.val:
        temp = l1
        temp.next = mergeTwoLists(l1.next, l2)
    else:
        temp = l2
        temp.next = mergeTwoLists(l1, l2.next)

    return temp
