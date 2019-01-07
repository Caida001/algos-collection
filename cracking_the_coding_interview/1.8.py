Zero Matrix: Write an algorithm such that if an element in an MxN matrix is 0, its entire row and
column are set to O.

from copy import deepcopy

def zeroMatrix(matrix):
    res = deepcopy(matrix)
    M = len(matrix)
    N = len(matrix[0])

    for i in range(M):
        for j in range(N):
            if matrix[i][j] == 0:
                for x in range(M):
                    res[x][j] = 0
                for y in range(N):
                    res[i][y] = 0

    return res
