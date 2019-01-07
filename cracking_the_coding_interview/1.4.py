Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palin-
drome. A palindrome is a word or phrase that is the same forwards and backwards. A permutation
is a rea rrangement of letters. The palindrome does not need to be limited to just dictionary words.
EXAMPLE
Input: Tact Coa
Output: True (permutations: "taco cat". "atco cta". etc.)

def pPerm(str):
    arr = list(''.join(str.lower().split(' ')))
    dict = {}
    for el in arr:
        if el not in dict:
            dict[el] = 1
        else:
            dict[el] += 1

    newarr = dict.values()
    odd = 0

    for val in newarr:
        if val % 2 == 1: odd += 1

    if odd > 1: return False
    return True
