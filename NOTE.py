import sys



n, m = map(int,input().split())

visited = [False] * n
graph = [[]for i in range(n)]

for _ in range(m):
    a, b = map(int,sys.stdin.readline().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(index, number):
    if number == 4:
        print(1)
        exit()
    for i in graph[index]:
        if not visited[i]:
            visited[i] = True
            dfs(i, number+1)
            visited[i] = False

for i in range(n):
    visited[i] = True
    dfs(i, 0)
    visited[i] = False

print(0)