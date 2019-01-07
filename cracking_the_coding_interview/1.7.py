Rotate Matrix: Given an image represented by an NxN matrix, where each pixel in the image is 4
bytes, write a method to rotate the image by 90 degrees. (an you do this in place?


from copy import deepcopy

def rotateMatrix(matrix):
    res = deepcopy(matrix)
    for i in range(len(matrix)):
        for j in range(len(matrix)-1, -1, -1):
            res[i][len(matrix) - j - 1] = matrix[j][i]

    return res 
