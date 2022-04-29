"""
이분 그래프
https://www.acmicpc.net/problem/1707
"""

import sys
from collections import deque

input = sys.stdin.readline


K = int(input())

def bfs(start, group):
    q = deque()
    q.append(start)
    visited[start] = group
    while q:
        x = q.popleft()

        for i in graph[x]:
            if not visited[i]:
                q.append(i)
                visited[i] = -1 * visited[x]
            elif visited[i] == visited[x]:
                return False
    return True

for _ in range(K):
    V, E = map(int,input().split())

    graph = [[]for _ in range(V+1)]
    visited = [False] * (V+1)
    for _ in range(E):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    
    for i in range(1, V+1):
        if not visited[i]:
            result = bfs(i, 1)
            if not result:
                break
    
    print(visited)
    print('YES' if result else 'NO')