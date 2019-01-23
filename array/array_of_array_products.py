Given an array of integers arr, you’re asked to calculate for each index i the
product of all integers except the integer at that index (i.e. except arr[i]).
Implement a function arrayOfArrayProducts that takes an array of integers and returns an array of the products.

Solve without using division and analyze your solution’s time and space complexities.

Examples:

input:  arr = [8, 10, 2]
output: [20, 16, 80] # by calculating: [10*2, 8*2, 8*10]

input:  arr = [2, 7, 3, 4]
output: [84, 24, 56, 42] # by calculating: [7*3*4, 2*3*4, 2*7*4, 2*7*3]



def array_of_array_products(arr):
  if len(arr) <= 1: return []
  res = [1]
  for i in range(len(arr)-1):
    res.append(res[-1] * arr[i])

  temp = 1
  for j in range(len(arr)-2, -1, -1):
    temp *= arr[j+1]
    res[j] *= temp


  return res


  """

  arr=           [2, 3, 4, 5]
  left_product = [1, 2, 2*3, 2*3*4]
                      20   5  1
         ans =   [3*4*5, 2*4*5, 2*3*5, 2*3*4]
  product[i] = product of all elements to left of i * products of all element to right of i
  """
