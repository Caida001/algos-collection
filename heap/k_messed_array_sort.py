Given an array of integers arr where each element is at most k places away from
its sorted position, code an efficient function sortKMessedArray that sorts arr.
For instance, for an input array of size 10 and k = 2, an element belonging to
index 6 in the sorted array will be located at either index 4, 5, 6, 7 or 8 in the input array.

Analyze the time and space complexities of your solution.

Example:

input:  arr = [1, 4, 5, 2, 3, 7, 8, 6, 10, 9], k = 2

output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


import heapq

def sort_k_messed_array(arr, k):
  if len(arr) <= 1: return arr
  heap = []

  for i in range(k+1):
    heapq.heappush(heap, arr[i])
  i = k + 1
  while i < len(arr):
    arr[i-k-1] = heapq.heappop(heap)
    heapq.heappush(heap, arr[i])
    i += 1

  for j in range(len(arr)-k-1, len(arr)):
    arr[j] = heapq.heappop(heap)


  return arr
