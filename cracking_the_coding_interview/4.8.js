First Common Ancestor: Design an algorithm and write code to find the first common ancestor
of two nodes in a binary tree. Avoid storing additional nodes in a data structure. NOTE: This is not
necessarily a binary search tree.


var TreeNode = function(val) {
  this.val = val;
  this.left = null;
  this.right = null;
  this.parent = null;
}

TreeNode.prototype.isAncestor = function(node) {
  if(this === node) {
    return true;
  } else {
    let answer1 = false
    let answer2 = false
    if(this.left !== null) {
      answer1 = this.left.isAncestor(node)
    }
    if(this.right !== null) {
      answer2 = this.right.isAncestor(node)
    }
    return answer1 || answer2
  }
}

function firstCommonAncestor(node1, node2) {
  let currNode = node1;
  while(!currNode.isAncestor(node2)){
    if(currNode == null){
      throw Error;
    } else {
      currNode = currNode.parent;
    }
  }
  return currNode.val 
}
