import heapq
import math

def solution(n, costs):
    answer = 0

    graph = [[]for _ in range(n)]
    distance = [math.inf]*n

    for i in costs:
        graph[i[0]].append((i[2],i[1]))
        graph[i[1]].append((i[2],i[0]))

    q = [(0,0)]
    distance[0] = 0

    while q:
        cost, now = q.pop()

        if distance[now] < cost:
            continue

        for i in graph[now]:
            ncost = cost + i[0]
            if ncost < distance[i[1]]:
                distance[i[1]] = ncost
                q.append((ncost,i[1]))
    print(distance)

        

    return answer

print(solution(4,[[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]))