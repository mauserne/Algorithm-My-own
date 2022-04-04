"""
문제집
https://www.acmicpc.net/problem/1766
39596KB     236ms
"""


import heapq
import sys

input = sys.stdin.readline


N, M = map(int, input().split())


graph = [[]for _ in range(N+1)]
indegree = [0] * (N+1)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

result = []

def tsort():
    q = []
    for i in range(1,N+1):
        if indegree[i] == 0:
            heapq.heappush(q,i)

    while q:
        index = heapq.heappop(q)
        result.append(index)
        for i in graph[index]:
            indegree[i] -= 1
            if indegree[i] == 0:
                heapq.heappush(q, i)

tsort()
for i in result:
    print(i, end=' ')