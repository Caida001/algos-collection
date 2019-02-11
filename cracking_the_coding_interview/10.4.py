Sorted Search, No Size: You are given an array-like data structure Listy which lacks a size
method. It does, however, have an elementAt (i) method that returns the element at index i in
0(1) time. If i is beyond the bounds of the data structure, it returns -1. (For this reason, the data
structure only supports positive integers.) Given a Listy which contains sorted, positive integers,
find the index at which an element x occurs. If x occurs multiple times, you may return any index.


def search(listy, target):
    idx = 1
    while listy.elementAt(idx) != -1 and listy.elementAt(idx) < target:
        idx *= 2 
    return binarySearch(listy, target, idx//2, idx)

def binarySearch(listy, target, low, high):
    while low <= high:
        mid = (low+high) // 2
    
        if listy.elementAt(mid) > target or listy.elementAt(mid) == -1:
            high = mid - 1 
        elif listy.elementAt(mid) < target:
            low = mid + 1 
        else:
            return mid 

    return -1 