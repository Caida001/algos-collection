Sorted Merge: You are given two sorted arrays, A and B, where A has a large enough buffer at the
end to hold B. Write a method to merge B into A in sorted order.


def sortedMerge(a, b):
    n = len(a)
    m = len(b)
    i, j = n - 1, m - 1
    lastIdx = n + m - 1 
    while j >= 0:
        if i >= 0 and a[i] > b[j]:
            a[lastIdx] = a[i]
            i -= 1 
        else:
            a[lastIdx] = b[j]
            j -= 1 
        lastIdx -= 1 