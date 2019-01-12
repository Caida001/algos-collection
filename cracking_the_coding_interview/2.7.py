Intersection: Given two (singly) linked lists, determine if the two lists intersect. Return the inter-
secting node. Note that the intersection is defined based on reference, not value. That is, if the kth
node of the first linked list is the exact same node (by reference) as the jth node of the second
linked list, then they are intersecting.


def intersection(l1, l2):
    head1, head2 = l1, l2;
    len1, len2 = 0, 0;
    while head1:
        len1 += 1
        head1 = head1.next
    while head2:
        len2 += 1
        head2 = head2.next

    if len1 > len2:
        while len1 > len2:
            l1 = l1.next
            len1 -= 1
    elif len2 > len1:
        while len2 > len1:
            l2 = l2.next
            len2 -= 1

    while l1 and l2:
        if l1 == l2:
            return True
        else:
            l1 = l1.next
            l2 = l2.next

    return False
