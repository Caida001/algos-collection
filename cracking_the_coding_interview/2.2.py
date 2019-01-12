Return Kth to Last: Implement an algorithm to find the kth to last element of a singly linked list.

def kthToLast(l, k):
    if l.head is None: return
    l1, l2 = l.head, l.head
    while k > 0:
        if l2 is None:
            return None
        else:
            l2 = l2.next
        k -= 1

    while l2:
        l2 = l2.next
        l1 = l1.next

    return l1
