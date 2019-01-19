The deletion distance of two strings is the minimum number of characters you
need to delete in the two strings in order to get the same string. For instance,
the deletion distance between "heat" and "hit" is 3:

By deleting 'e' and 'a' in "heat", and 'i' in "hit", we get the string "ht" in both cases.
We cannot get the same string from both strings by deleting 2 letters or fewer.
Given the strings str1 and str2, write an efficient function deletionDistance
that returns the deletion distance between them. Explain how your function works,
and analyze its time and space complexities.

Examples:

input:  str1 = "dog", str2 = "frog"
output: 3

input:  str1 = "some", str2 = "some"
output: 0

input:  str1 = "some", str2 = "thing"
output: 9

input:  str1 = "", str2 = ""
output: 0


def deletion_distance(str1, str2):
  len1, len2 = len(str1), len(str2)
  memo = [[0] * (len2+1) for _ in range(len1+1)]

  for i in range(len1+1):
    for j in range(len2+1):
      if i == 0:
        memo[i][j] = j
      elif j == 0:
        memo[i][j] = i
      elif str1[i-1] == str2[j-1]:
        memo[i][j] = memo[i-1][j-1]
      else:
        memo[i][j] = 1 + min(memo[i-1][j], memo[i][j-1])

  return memo[len1][len2] 
