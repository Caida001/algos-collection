Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

Example 1:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:

Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]



class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix: return matrix
        m = len(matrix)
        n = len(matrix[0])
        top, right, bottom, left = 0, n-1, m-1, 0 
        res = []
        
        while len(res) < len(matrix[0]) * len(matrix):
          for i in range(left, right+1):
            res.append(matrix[top][i])
          top += 1 
          
          for i in range(top, bottom+1):
            res.append(matrix[i][right])
          right -= 1 
          
          for i in range(right, left-1, -1):
            res.append(matrix[bottom][i])
          bottom -= 1 
          
          for i in range(bottom, top-1, -1):
            res.append(matrix[i][left])
          left += 1 
          
        return res