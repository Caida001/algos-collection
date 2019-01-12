Loop Detection: Given a circular linked list, implement an algorithm that returns the node at the
beginning of the loop.
DEFINITION
Circular linked list: A (corrupt) linked list in which a node's next pointer points to an earlier node, so
as to make a loop in the linked list.
EXAMPLE
Input: A -) B -) C -) 0 -) E - ) C[thesameCasearlierl
Output: C

def circular(l):
    p1 = p2 = l

    while p2 and p2.next:
        p1 = p1.next
        p2 = p2.next.next
        if p1 is p2: break

    if p2 is None or p2.next is None: return None

    p1 = l
    while p1 != p2:
        p1 = p1.next
        p2 = p2.next

    return p1
