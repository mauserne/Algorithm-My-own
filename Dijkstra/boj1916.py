"""
최소비용 구하기
https://www.acmicpc.net/problem/1916

58204KB     356ms
time spent : 8 min
"""

import heapq
import math
import sys

input = sys.stdin.readline


#N 도시개수, M 버스 개수
N = int(input())
M = int(input())

graph = [[]for _ in range(N+1)]
cost = [math.inf] * (N+1)

for _ in range(M):
    #버스
    #출발, 도착, 비용
    a,b,c = map(int, input().split())
    graph[a].append((b,c))

#출발지, 도착지
start, end = map(int, input().split())

def dijstra(start):
    q = []
    heapq.heappush(q,(0,start))
    while q:
        money, now = heapq.heappop(q)
        if money > cost[now]:
            continue
        for i in graph[now]:
            if cost[i[0]] > i[1] + money:
                cost[i[0]] = i[1] + money
                heapq.heappush(q,(cost[i[0]], i[0]))

dijstra(start)

print(cost[end])