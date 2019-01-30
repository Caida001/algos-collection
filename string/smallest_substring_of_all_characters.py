Given an array of unique characters arr and a string str, Implement a function
getShortestUniqueSubstring that finds the smallest substring of str containing
all the characters in arr. Return "" (empty string) if such a substring doesn’t exist.

Come up with an asymptotically optimal solution and analyze the time and space complexities.

Example:

input:  arr = ['x','y','z'], str = "xyyzyzyx"

output: "zyx"
Constraints:

[time limit] 5000ms

[input] array.character arr

1 ≤ arr.length ≤ 30
[input] string str

1 ≤ str.length ≤ 500
[output] string



def get_shortest_unique_substring(arr, str):
  dict = {}
  headIndex = 0
  result = ""
  uniqueCounter = 0

  # initialize dictionary
  for el in arr:
    dict[el] = 0


  # scan string
  for tailIndex in range(len(str)):
    char = str[tailIndex]

    # skip all characters not in arr
    if char not in dict: continue

    tailCount = dict[char]
    if tailCount == 0:
      uniqueCounter += 1
    dict[char] += 1

    # push headIndex forward
    while uniqueCounter == len(arr):
      tempLength = tailIndex - headIndex + 1
      if tempLength == len(arr):
        return str[headIndex:tailIndex+1]

      if result == "" or tempLength < len(result):
        result = str[headIndex:tailIndex+1]

      headChar = str[headIndex]

      if headChar in dict:
        dict[headChar] -= 1
        if dict[headChar] == 0:
          uniqueCounter -= 1


      headIndex += 1

  return result




"""
arr = ['x','y','z'], str = "xyyzxyyz"

arr = ['x','y','z'], str = "xyyzyzyx"


arr = ['x','y','z'], str = "xyyyyyyyyyyyxzzzzzzzyzyx"


  {x: 1 y: 1 z: 1}

"""
