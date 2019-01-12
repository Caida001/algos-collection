Partition: Write code to partition a linked list around a value x, such that all nodes less than x come
before all nodes greater than or equal to x . lf x is contained within the list, the values of x only need
to be after the elements less than x (see below) . The partition element x can appear anywhere in the
"right partition"; it does not need to appear between the left and right partitions.
EXAMPLE
Input: 3 -> 5 -> 8 -> 5 - > 10 -> 2 -> 1 [partition = 5)
Output: 3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head, x):

        l1, l2 = ListNode(None), ListNode(None)
        head1, head2 = l1, l2
        while head:
          if head.val >= x:
            l2.next = ListNode(head.val)
            l2 = l2.next
            head = head.next
          else:
            l1.next = ListNode(head.val)
            l1 = l1.next
            head = head.next

        l1.next = head2.next

        return head1.next
