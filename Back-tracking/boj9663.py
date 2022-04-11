"""
N-Queen
"""

N = int(input())

matrix = [[0]*N for _ in range(N)]

matrix[2].append(1)
print(matrix)