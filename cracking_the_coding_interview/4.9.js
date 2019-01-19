BST Sequences: A binary search tree was created by traversing through an array from left to right
and inserting each element. Given a binary search tree with distinct elements, print all possible
arrays that could have led to this tree.
EXAMPLE
Input:
Output: {2, 1, 3}, {2, 3, 1}


function bstSeq(bst) {
  let seqs = []
  let recurse = function(nodes, travelled) {
    let noChild = true;
    nodes.forEach(node => {
      if(node.left !== null && travelled[node.left.val] === undefined) {
        noChild = false;
        travelled[node.left.value]
      }
    })
  }
}
