URLify: Write a method to replace all spaces in a string with '%20: You may assume that the string
has sufficient space at the end to hold the additional characters, and that you are given the "true"
length of the string. (Note: If implementing in Java, please use a character array so that you can
perform this operation in place.)
EXAMPLE
Input:  "Mr John Smith    ", 13
Output: "Mr%20John%20Smith"


def urlify(str, n):
  strarr = list(str)
  j = len(strarr) - 1
  i = n - 1
  while i >= 0:
    if strarr[i] != ' ':
      strarr[j] = strarr[i]
      i -= 1
      j -= 1
    else:
      strarr[j] = '0'
      strarr[j-1] = '2'
      strarr[j-2] = '%'
      j -= 3
      i -= 1
  return ''.join(strarr)
