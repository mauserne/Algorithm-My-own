"""
플로이드
https://www.acmicpc.net/problem/11404
32976KB     776ms
"""


import sys
import math

input = sys.stdin.readline

N = int(input())
M = int(input())

graph = [[math.inf]*(N+1) for _ in range(N+1)]

for i in range(1, N+1):
    graph[i][i] = 0

for _ in range(M):
    a,b,c = map(int, input().split())
    if graph[a][b] > c:
        graph[a][b] = c

for k in range(1, N+1):
    for a in range(1, N+1):
        for b in range(1, N+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for a in range(1, N+1):
    for b in range(1, N+1):
        if graph[a][b] == math.inf:
            print(0, end = ' ')
        else:
            print(graph[a][b], end=' ')
    print()