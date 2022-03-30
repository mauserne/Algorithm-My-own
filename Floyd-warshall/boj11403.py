"""
경로찾기
https://www.acmicpc.net/problem/11403
"""

import sys


input = sys.stdin.readline


N = int(input())

graph = []

for _ in range(N):
    graph.append(list(map(int, input().split())))

for k in range(N):
    for i in range(N):
        for j in range(N): 
            if graph[i][j] == 1 or (graph[i][k] == 1 and graph[k][j] == 1):
                graph[i][j] = 1
                print()
                print(i,k,j)
                for z in graph:
                    print(z)

for row in graph:
    for col in row:
        print(col, end = " ")
    print()
 