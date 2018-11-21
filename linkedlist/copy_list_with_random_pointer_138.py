A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.

# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None


class Solution(object):
  def __init__(self):
    self.visited = {}

  def getClonedNode(self, node):
    if node:
      if node in self.visited:
        return self.visited[node]
      else:
        self.visited[node] = RandomListNode(node.label)
        return self.visited[node]

    return None


  def copyRandomList(self, head):
      """
      :type head: RandomListNode
      :rtype: RandomListNode
      """
      if not head:
        return head

      old_node = head
      new_node = RandomListNode(old_node.label)
      self.visited[old_node] = new_node

      while old_node != None:
        new_node.random = self.getClonedNode(old_node.random)
        new_node.next = self.getClonedNode(old_node.next)

        old_node = old_node.next
        new_node = new_node.next

      return self.visited[head]


# second Solution


# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None


class Solution(object):
  def copyRandomList(self, head):
    if not head:
      return head

    ptr = head
    while ptr:
      new_node = RandomListNode(ptr.label)
      new_node.next = ptr.next
      ptr.next = new_node
      ptr = new_node.next

    ptr = head

    while ptr:
      ptr.next.random = ptr.random.next if ptr.random else None
      ptr = ptr.next.next

    ptr_old_list = head
    ptr_new_list = head.next
    head_old = head.next
    while ptr_old_list:
      ptr_old_list.next = ptr_old_list.next.next
      ptr_new_list.next = ptr_new_list.next.next if ptr_new_list.next else None
      ptr_old_list = ptr_old_list.next
      ptr_new_list = ptr_new_list.next
    return head_old
