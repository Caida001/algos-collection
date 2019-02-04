Random Node: You are implementing a binary tree class from scratch which, in addition to
insert, find, and delete, has a method getRandomNode() which returns a random node
from the tree. All nodes should be equally likely to be chosen. Design and implement an algorithm
for getRandomNode, and explain how you would implement the rest of the methods.




import random 
class Solution:
    def __init__(self, root):
        self.root = root 

    def getRandomNode(self):
        array = self.inOrderTraversal(self.root, [])
        idx = random.randint(len(array))
        return array[idx]

    def inOrderTraversal(self, node, array):
        if not node: return array 
        if node is not None:
            inOrderTraversal(node.left, array)
            array.append(node)
            inOrderTraversal(node.right, array)

        return array