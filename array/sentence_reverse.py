You are given an array of characters arr that consists of sequences of characters separated by space characters. Each space-delimited sequence of characters defines a word.

Implement a function reverseWords that reverses the order of the words in the array in the most efficient manner.

Explain your solution and analyze its time and space complexities.

Example:

input:  arr = [ 'p', 'e', 'r', 'f', 'e', 'c', 't', '  ',
                'm', 'a', 'k', 'e', 's', '  ',
                'p', 'r', 'a', 'c', 't', 'i', 'c', 'e' ]

output: [ 'p', 'r', 'a', 'c', 't', 'i', 'c', 'e', '  ',
          'm', 'a', 'k', 'e', 's', '  ',
          'p', 'e', 'r', 'f', 'e', 'c', 't' ]





def reverse_words(arr):
  helper(arr, 0, len(arr)-1)

  start = None
  for i in range(len(arr)):
    if arr[i] == " ":
      if start is not None:
        helper(arr, start, i-1)
        start = None
    elif i == len(arr)-1:
      if start is not None:
        helper(arr, start, i)
    else:
      if start is None:
        start = i

  return arr



def helper(arr, start, end):
  while start < end:
    temp = arr[start]
    arr[start] = arr[end]
    arr[end] = temp
    start += 1
    end -= 1 
