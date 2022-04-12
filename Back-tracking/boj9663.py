"""
N-Queen
"""

N = int(input())

matrix = [[0]*N for _ in range(N)]

def dfs():
    