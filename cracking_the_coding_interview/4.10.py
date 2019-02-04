Check Subtree: Tl and T2 are two very large binary trees, with Tl much bigger than T2. Create an
algorith m to determine if T2 is a subtree of Tl .
A tree T2 is a subtree ofTi if there exists a node n in Ti such that the subtree of n is identical to T2.
That is, if you cut off the tree at node n, the two trees would be identical.

class Node(self, data):
    self.left = None 
    self.right = None 
    self.data = data 

def isIdentical(root1, root2):
    if root1 is None and root2 is None: 
        return True 

    if root1 is None or root2 is None: 
        return False 

    return root1 == root2 and isIdentical(root1.left, root2.left) and isIdentical(root1.right, root2.right)


def checkSubtree(T1, T2):
    if T2 is None:
        return True 
    
    if T1 is None:
        return False 

    if isIdentical(T1, T2):
        return True 

    return checkSubtree(T1.left, T2) or checkSubtree(T1.right, T2)