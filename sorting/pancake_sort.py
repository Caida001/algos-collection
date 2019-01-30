Given an array of integers arr:

Write a function flip(arr, k) that reverses the order of the first k elements in the array arr.
Write a function pancakeSort(arr) that sorts and returns the input array. You are allowed to use only the function flip you wrote in the first step in order to make changes in the array.
Example:

input:  arr = [1, 5, 4, 3, 2]

output: [1, 2, 3, 4, 5] # to clarify, this is pancakeSort's output
Analyze the time and space complexities of your solution.

Note: it’s called pancake sort because it resembles sorting pancakes on a plate with a spatula, where you can only use the spatula to flip some of the top pancakes in the plate. To read more about the problem, see the Pancake Sorting Wikipedia page.

Constraints:

[time limit] 5000ms

[input] array.integer arr

[input] integer k

0 ≤ k
[output] array.integer


def flip(arr, k):
  arr[:k+1] = reversed(arr[:k+1])

def pancake_sort(arr):
  if len(arr) <= 1: return arr
  idx = len(arr) - 1 
  while idx > 0:
    m = findMax(arr, idx)
    if m != idx:
      flip(arr, m)
      flip(arr, idx)
    idx -= 1 
  
  return arr

def findMax(arr, idx):
  maximum = max(arr[:idx+1])
  return arr.index(maximum)
  

#
#1. Write a function flip(arr, k) that reverses the order of the first k elements in the array arr.
#input:  arr = [1, 5, 4, 3, 2]
#               0  1  2  3  4
#               s  k
#input:  arr = [5, 1, 4, 3, 2]
#               0  1  2  3  4
#               s           k
#input:  arr = [2, 3, 4, 1, 5]
#               0  1  2  3  4
#               s        k
#input:  arr = [1, 4, 3, 2, 5]
#               0  1  2  3  4
#               s  k
#input:  arr = [4, 1, 3, 2, 5]
#               0  1  2  3  4
#               s        k
#input:  arr = [2, 3, 1, 4, 5]
#               0  1  2  3  4
#               s     k
#input:  arr = [1, 3, 2, 4, 5]
#               0  1  2  3  4
#               s  k
#input:  arr = [2, 3, 1, 4, 5]
#               0  1  2  3  4
#               s     k
#input:  arr = [1, 2, 3, 4, 5]
#               0  1  2  3  4
#               s  k

#                5 1 4 3 2
#                        k
#                2 3 4 1 5
#                      k
#                1 4 3 2 5
#               [3,4,5,1,2]
     
  