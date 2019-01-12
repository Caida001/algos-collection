Sum Lists: You have two numbers represented by a linked list, where each node contains a single
digit. The digits are stored in reverse order, such that the 1 's digit is at the head of the list. Write a
function that adds the two numbers and returns the sum as a linked list.
EXAMPLE
Input: (7-) 1 -) 6) + (5 -) 9 -) 2) .Thatis,617 + 295.
Output: 2 -) 1 -) 9. That is, 912.
FOLLOW UP
Suppose the digits are stored in forward order. Repeat the above problem.
EXAMPLE
Input: (6 -) 1 -) 7) + (2 -) 9 -) 5) . Thatis,617 + 295 .
Output: 9 -) 1 -) 2. That is, 912.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
  def addTwoNumbers(self, l1, l2):
    carry = 0
    head = res = ListNode(None)

    while l1 or l2:
      x = l1.val if l1 else 0
      y = l2.val if l2 else 0

      sum = x + y + carry
      carry = sum // 10
      res.next = ListNode(sum%10)
      res = res.next
      if l1: l1 = l1.next
      if l2: l2 = l2.next

    if carry > 0: res.next = ListNode(1)

    return head.next

# follow up
def sum_lists(l1, l2):

    length1, length2 = 0, 0
    pointer1, pointer2 = l1, l2
    while pointer1:
        length1 += 1
        pointer1 = pointer1.next
    while pointer2:
        length2 += 1
        pointer2 = pointer2.next

    if length1 < length2:
        for i in range(length2 - length1):
            head1 = ListNode(0)
            head1.next = l1
            l1 = head1
    else:
        for i in range(length1 - length2):
            head2 = ListNode(0)
            head2.next = l2
            l2 = head2

    res = 0
    while l1 and l2:
        res = res * 10 + l1.val + l2.val
        l1 = l1.next
        l2 = l2.next

    head = ListNode(0)
    i = 0
    while i < len(str(res)):
        head.next = listNode(res[i])
        i += 1
    return head.next 
