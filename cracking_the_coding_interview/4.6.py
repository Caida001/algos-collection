Successor: Write an algorithm to find the "next" node (i.e., in-order successor) of a given node in a
binary search tree. You may assume that each node has a link to its parent.

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.parent = None

def successor(node):
    successor = None
    if node.right:
        successor = node.right
        while successor.left:
            successor = successor.left
    elif node.parent:
        currNode = node
        while currNode.parent and successor == None:
            if currNode.parent.left == currNode:
                successor = currNode.parent 
            currNode = currNode.parent

    return successor
