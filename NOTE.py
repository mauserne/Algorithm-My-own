from collections import deque


n, m, v = map(int, input().split())

graph = [[]for _ in range(n+1)]
visited = [False] * (n+1)


for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1,n+1):
    graph[i].sort()

def dfs(x):
    visited[x] = True
    print(x, end = ' ')
    for i in graph[x]:
        if not visited[i]:
            dfs(i)

def bfs(x):
    visited[x] = True
    queue = deque([x])
    while queue:
        x = queue.popleft()
        print(x, end=' ')
        for i in graph[x]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True  

dfs(v)

visited = [False] * (n+1)
print()
bfs(v)