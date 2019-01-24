Description
An abbreviation of a word follows the form . Below are some examples of word abbreviations:

a) it                      --> it    (no abbreviation)

     1
b) d|o|g                   --> d1g

              1    1  1
     1---5----0----5--8
c) i|nternationalizatio|n  --> i18n

              1
     1---5----0
d) l|ocalizatio|n          --> l10n
Assume you have a dictionary and given a word, find whether its abbreviation is
unique in the dictionary. A word's abbreviation is unique if no other word from
the dictionary has the same abbreviation.

Have you met this question in a real interview?
Example
Given dictionary = [ "deer", "door", "cake", "card" ]
isUnique("dear") // return false
isUnique("cart") // return true
isUnique("cane") // return false
isUnique("make") // return true


class ValidWordAbbr:
    """
    @param: dictionary: a list of words
    """

    def __init__(self, dictionary):
        self.dict = {}
        for string in dictionary:
            n = len(string)
            abbr = string[0] + str(n) + string[n-1]
            self.dict[abbr] = string

    """
    @param: word: a string
    @return: true if its abbreviation is unique or false
    """
    def isUnique(self, word):
        # write your code here
        n = len(word)
        abbr = word[0] + str(n) + word[n-1]
        return self.dict[abbr].count(word) == len(self.dict[abbr])  
