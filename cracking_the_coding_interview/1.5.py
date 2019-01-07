One Away: There are three types of edits that can be performed on strings: insert a character,
remove a character, or replace a character. Given two strings, write a function to check if they are
one edit (or zero edits) away.
EXAMPLE
pale, ple -> true
pales, pale -> true
pale, bale -> true
pale, bake -> false

def oneAway(str1, str2):
    list1, list2 = list(str1), list(str2)
    if len(list1) - len(list2) > 1:
        return False
    elif len(list1) - len(list2) < -1:
        return False

    dict = {}
    for el in list1:
        if el not in dict:
            dict[el] = 0
        else:
            dict[el] += 1

    diff = 0
    for el in list2:
        if el not in dict:
            diff += 1

    return diff <= 1
