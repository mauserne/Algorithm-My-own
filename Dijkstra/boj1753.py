"""
최단경로
https://www.acmicpc.net/problem/1753
"""


import sys
import math

input = sys.stdin.readline

V, E = map(int, input().split())
K = int(input())

graph = [[] for _ in range(V+1)]
visited = [False] * (V+1)
distance = [math.inf] * (V+1)


for _ in range(E):
    u,v,w = map(int, input().split())
    graph[u].append((v,w))

def get_smallest_node():
    min_value = math.inf
    index = 0
    for i in range(1, V+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index

def dijkstra(start):
    distance[start] = 0
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1]
    for _ in range(V - 1):
        now = get_smallest_node()
        visited[now] = True
        for i in graph[now]:
            cost = distance[now] + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost

dijkstra(K)

for i in range(1, V+1):
    if distance[i] == math.inf:
        print('INF')
    else:
        print(distance[i])