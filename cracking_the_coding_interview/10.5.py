Sparse Search: Given a sorted array of strings that is interspersed with empty strings, write a
method to find the location of a given string.


def sparseSearch(lst, target):
    low, high = 0, len(lst) - 1
    mid = (low + high) // 2 

    if lst[mid] == "":
        left, right = mid - 1, mid + 1 
        while True:
            if left < low and right > high:
                return -1 
            elif right <= high and lst[right]:
                mid = right 
                break 
            elif left >= low and lst[left]:
                mid = left 
                break 

            right += 1 
            left -= 1 

    while low <= high:
        if target == lst[mid]:
            return mid 
        elif lst[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1 















      