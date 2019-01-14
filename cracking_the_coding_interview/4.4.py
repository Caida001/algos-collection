Check Balanced: Implement a function to check if a binary tree is balanced. For the purposes of
this question, a balanced tree is defined to be a tree such that the heights of the two subtrees of any
node never differ by more than one.


# definition for a binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def helper(bt):
    if not bt: return 0
    return max(helper(bt.left), helper(bt.right)) + 1

def checkBalanced(bt):
    if not root: return True
    if abs(helper(bt.left) - helper(bt.right)) <= 1:
        return checkBalanced(bt.left) and checkBalanced(bt.right)
    else:
        return False 
