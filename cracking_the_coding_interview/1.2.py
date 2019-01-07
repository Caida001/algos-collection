Check Permutation: Given two strings, write a
method to decide if one is a permutation of the
other.

def checkPermutation(str1, str2):
    if len(str1) != len(str2): return False 
    if sorted(list(str1)) == sorted(list(str2)): return True
    return False
