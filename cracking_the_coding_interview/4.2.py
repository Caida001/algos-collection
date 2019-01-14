Minimal Tree: Given a sorted (increasing order) array with unique integer elements, write an algo-
rithm to create a binary search tree with minimal height.

class Node:
    def __init__(self, item):
        self.right = None
        self.left = None
        self.val = item

def helper(arr):
    return miniTree(arr, 0, len(arr) - 1)

def miniTree(arr, start, end):
    if start > end: return ''

    mid = (start + end) / 2
    root = Node(arr[mid])
    root.left = miniTree(arr, start, mid-1)
    root.right = miniTree(arr, mid+1, end)
    return root

    
