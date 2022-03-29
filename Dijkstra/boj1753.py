"""
최단경로
https://www.acmicpc.net/problem/1753
"""


import sys
import math
import heapq

input = sys.stdin.readline

#노드 개수 V, 간선 개수 E, 시작노드 K
V, E = map(int, input().split())
K = int(input())

graph = [[] for _ in range(V+1)]
distance = [math.inf] * (V+1)


for _ in range(E):
    u,v,w = map(int, input().split())
    graph[u].append((v,w))

def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(K)

for i in range(1, V+1):
    if distance[i] == math.inf:
        print('INF')
    else:
        print(distance[i])