Given an integer matrix, find the length of the longest increasing path.

From each cell, you can either move to four directions: left, right, up or down.
 You may NOT move diagonally or move outside of the boundary (i.e. wrap-around is not allowed).

Example 1:

Input: nums =
[
  [9,9,4],
  [6,6,8],
  [2,1,1]
]
Output: 4
Explanation: The longest increasing path is [1, 2, 6, 9].
Example 2:

Input: nums =
[
  [3,4,5],
  [3,2,6],
  [2,2,1]
]
Output: 4
Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.



class Solution:
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if not matrix: return 0
        self.directions = [(1,0), (-1,0), (0,-1), (0,1)]
        m = len(matrix)
        n = len(matrix[0])
        dp = [[-1 for _ in range(n)] for _ in range(m)]
        res = 1

        for i in range(m):
          for j in range(n):
            temp = self.dfs(matrix, i, j, m, n, dp)
            res = max(res, temp)

        return res


    def dfs(self, matrix, i, j, m, n, dp):
        if dp[i][j] != -1: return dp[i][j]
        res = 1
        for dir in self.directions:
          x, y = i + dir[0], j + dir[1]
          if x < 0 or x >= m or y < 0 or y >= n or matrix[x][y] <= matrix[i][j]:
            continue
          length = 1 + self.dfs(matrix, x, y, m, n, dp)
          res = max(res, length)

        dp[i][j] = res

        return res
