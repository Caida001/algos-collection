Validate BST: Implement a function to check if a binary tree is a binary search tree.

def validateBst(bst, lowerBound = float('-inf'), upperBound = float('inf')):
    if not bst: return True

    if bst.val >= upperBound or bst.val <= lowerBound: return False
    return validateBst(bst.left, lowerBound, bst.val) and validateBst(bst.right, bst.val, upperBound)
