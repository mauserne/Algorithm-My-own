from copy import deepcopy

matrix = [[[1]],[[1]],[[1]]]

submatrix = deepcopy(matrix)

submatrix[0][0][0] =5
print(matrix)
print(submatrix)