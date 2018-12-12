
Given a binary tree, find the length of the longest consecutive sequence path.
The path refers to any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The longest consecutive path need to be from parent to child (cannot be the reverse).
For example,
   1
    \
     3
    / \
   2   4
        \
         5
Longest consecutive sequence path is 3-4-5, so return 3.
   2
    \
     3
    /
   2
  /
 1
Longest consecutive sequence path is 2-3,not 3-2-1, so return 2.


class Solution:
  def longestConsecutive(self, root):
    if not root: return 0
    self.res = 0

    self.dfs(root, 1)
    return self.res



  def dfs(self, root, curLen):
    self.res = max(self.res, curLen)

    if root.left:
      if root.left.val == root.val+1:
        self.dfs(root.left, curLen+1)
      else:
        self.dfs(root.left, 1)

    if root.right:
      if root.right.val == root.val + 1:
        self.dfs(root.right, curLen+1)
      else:
        self.dfs(root.right, 1)
