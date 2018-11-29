// Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).
//
// For example:
// Given binary tree [3,9,20,null,null,15,7],
//     3
//    / \
//   9  20
//     /  \
//    15   7
// return its level order traversal as:
// [
//   [3],
//   [9,20],
//   [15,7]
// ]

/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number[][]}
 */
var levelOrder = function(root) {
  let res = [];
  dfs(root, 0, res);
  return res;

};

function dfs(node, level, res) {
  if(node == null) return;
  if(level >= res.length) res.push([]);
  res[level].push(node.val);
  dfs(node.left, level+1, res);
  dfs(node.right, level + 1, res);
}

class Solution:
    def levelOrder(self, root):
        if root is None: return []
        q = [[root]]

        for level in q:
          temp = []
          for node in level:
            if node.left: temp.append(node.left)
            if node.right: temp.append(node.right)
          if temp: q.append(temp)

        return [[x.val for x in level] for level in q]
