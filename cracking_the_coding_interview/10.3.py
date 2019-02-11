Search in Rotated Array: Given a sorted array of n integers that has been rotated an unknown
number of times, write code to find an element in the array. You may assume that the array was
originally sorted in increasing order.
EXAMPLE
Input:findSin{lS, 16, 19, 2a, 25, 1, 3,4,5,7, la, 14}
Output: 8 (the index of 5 in the array)


def search(lst, target):
    l, r = 0, len(lst)-1
    
    while l < r:
        mid = (l + r) // 2 
        if lst[mid] == target:
            return mid
        # if lst[l...mid] is sorted 
        elif lst[l] <= lst[mid]:
            # as this subarray is sorted, we can check if target lies in which half 
            if target >= lst[l] and target <= lst[mid]:
                r = mid-1
            else:
                l = mid + 1 
        else:
            if target >= lst[mid] and target <= lst[r]:
                l = mid + 1 
            else:
                r = mid - 1 
            
    return -1
