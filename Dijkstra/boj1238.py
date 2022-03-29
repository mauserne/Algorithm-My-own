"""
파티
https://www.acmicpc.net/problem/1238
35044KB     1352ms
time spent : 26min
"""



import heapq
import sys
import math

input = sys.stdin.readline

N, M, X = map(int, input().split())
#N명의 학생, M개의 도로, 파티장소 X
#집에서 X에 갔다가 다시 집으로 가는 최단시간중 최대값?


graph = [[]for _ in range(N+1)]

for _ in range(M):
    # 시작점, 끝점, 소요시간
    a,b,c = map(int, input().split())
    graph[a].append((b,c))

#for 문 돌려서, x에 도착시키고, x부터 집으로 함수실행하고 최대값 찾기?
time = [0] * (N+1)

def dijkstra(start):
    cost = [math.inf] * (N+1)
    q = []
    heapq.heappush(q,(0,start))
    cost[start] = 0
    while q:
        time, now = heapq.heappop(q)
        if time > cost[now]:
            continue
        for i in graph[now]:
            if cost[i[0]] > i[1] + time:
                cost[i[0]] = i[1] + time
                heapq.heappush(q,(cost[i[0]],i[0]))
    return cost


for i in range(1,N+1):
    toparty = dijkstra(i)
    time[i] = toparty[X]

# 파티끝나고 각자 집으로

tohome = dijkstra(X)
for i in range(1,N+1):
    time[i] = time[i] + tohome[i]

print(max(time))