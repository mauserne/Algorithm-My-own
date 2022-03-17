"""
바이러스
https://www.acmicpc.net/problem/2606
time spent : 15min
"""

import sys


n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
infected = [False] * (n+1)

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(x):
    infected[x] = True
    for i in graph[x]:
        if not infected[i]:
            dfs(i)

dfs(1)

print(infected.count(True)-1)