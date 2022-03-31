"""
특정한 최단 경로
https://www.acmicpc.net/problem/1504
65828KB     688ms
time spent : 1hour
"""

#for문으로 n번 반복?

import heapq
import math
import sys

input = sys.stdin.readline


N, E = map(int, input().split())

graph = [[]for _ in range(N+1)]

for _ in range(E):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

v1, v2 = map(int, input().split())

def dijkstra(start,end):
    distance = [math.inf] * (N+1)
    q = []
    heapq.heappush(q,(0, start))
    distance[start] = 0
    while q:
        dist , node = heapq.heappop(q)
        if dist > distance[node]:
            continue
        for i in graph[node]:
            if distance[i[0]] > dist + i[1]:
                distance[i[0]] = dist + i[1]
                heapq.heappush(q,(distance[i[0]],i[0]))

    return distance[end]


result1 = 0
result2 = 0

arr1 = [(1,v1),(v1,v2),(v2,N)]
arr2 = [(1,v2),(v2,v1),(v1,N)]

for i in arr1:
    result1 += dijkstra(i[0],i[1])
for i in arr2:
    result2 += dijkstra(i[0],i[1])

resultmin = min(result1,result2)
if resultmin == math.inf:
    print(-1)
else:
    print(resultmin)
