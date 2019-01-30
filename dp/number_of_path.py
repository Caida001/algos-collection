You’re testing a new driverless car that is located at the Southwest (bottom-left)
corner of an n×n grid. The car is supposed to get to the opposite, Northeast (top-right),
corner of the grid. Given n, the size of the grid’s axes, write a function
numOfPathsToDest that returns the number of the possible paths the driverless car can take.

For convenience, let’s represent every square in the grid as a pair (i,j).
The first coordinate in the pair denotes the east-to-west axis, and the second
coordinate denotes the south-to-north axis. The initial state of the car is (0,0), and the destination is (n-1,n-1).

The car must abide by the following two rules: it cannot cross the diagonal border.
In other words, in every step the position (i,j) needs to maintain i >= j. See
the illustration above for n = 5. In every step, it may go one square North (up),
or one square East (right), but not both. E.g. if the car is at (3,1), it may go to (3,2) or (4,1).

Explain the correctness of your function, and analyze its time and space complexities.
Example:

input:  n = 4

output: 5 # since there are five possibilities:
          # “EEENNN”, “EENENN”, “ENEENN”, “ENENEN”, “EENNEN”,
          # where the 'E' character stands for moving one step
          # East, and the 'N' character stands for moving one step
          # North (so, for instance, the path sequence “EEENNN”
          # stands for the following steps that the car took:
          # East, East, East, North, North, North)
Constraints:

[time limit] 5000ms

[input] integer n

1 ≤ n ≤ 100
[output] integer


# recursive solution

def num_of_paths_to_dest(n):
  # allocate a 2d array for memoization
  # the memoization array is initialized with -1 to indicate uncalculated squares
  memo = [[-1 for _ in range(n)] for _ in range(n)]

  return helper(n-1, n-1, memo)

# i, j - a pair of non-negative integer coordinates
# number of paths from (0, 0) to the (i, j)

def helper(i, j, memo):
  if i < 0 or j < 0:
    return 0
  elif i < j:
    memo[i][j] = 0
  elif memo[i][j] != -1:
    memo[i][j]
  elif i == 0 and j == 0:
    memo[i][j] = 1
  else:
    memo[i][j] = helper(i, j-1, memo) + helper(i-1, j, memo)

  return memo[i][j]


# iterative solution
def num_of_paths_to_dest(n):
  if n == 1: return 1

  lastRow = [1 for _ in range(n)]
  curRow = [1 for _ in range(n)]

  for j in range(1, n):
    for i in range(j, n):
      if i == j:
        curRow[i] = lastRow[i]
      else:
        curRow[i] = curRow[i-1] + lastRow[i]
    lastRow = curRow

  return curRow[n-1]
