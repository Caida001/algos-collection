List of Depths: Given a binary tree, design an algorithm which creates a linked list of all the nodes
at each depth (e.g., if you have a tree with depth 0, you'll have 0 linked lists).

import queue

def listOfDepths(bt):
    lists = []
    temp = None
    q = new queue()
    nextQ = new queue()
    currNode = bt

    q.put(currNode)
    while not q.empty():
        currNode = q.get()
        newNode = new LinkedList(currNode.value)
        newNode.next = temp
        temp = newNode
        if currNode.left:
            nextQ.put(currNode.left)
        if currNode.right:
            nextQ.put(currNode.right)

        if q.empty():
            lists.append(temp)
            temp = None
            q = nextQ
            nextQ = new queue()

    return lists
