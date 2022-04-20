"""
촌수계산
https://www.acmicpc.net/problem/2644
time spent : 12min
"""

from collections import deque


n = int(input())
a, b = map(int, input().split())
m = int(input())

graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

def bfs(a):
    queue = deque()
    queue.append(a)
    
    while queue:
        x = queue.popleft()
        if x == b:
            return visited[x] 
        for i in graph[x]:
            if visited[i] == 0:
                queue.append(i)
                visited[i] = visited[x] + 1
    return -1

print(bfs(a))
