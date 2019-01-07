# Is Unique: Implement an algorithm to determine
# if a string has all unique characters. What if
#  you cannot use additional data structures?



def isUnique(str):
    if len(str) > 128:
        return False

    list = [False for _ in range(128)]
    for char in str:
        val = ord(char)
        if list[val]: return False
        list[val] = True
    return True

def isUnique0(str):
    dict = {}
    for char in str:
        if char not in dict:
            dict[char] = True
        else:
            return False
    return True 
