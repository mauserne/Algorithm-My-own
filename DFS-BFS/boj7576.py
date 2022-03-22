#BFS
"""
토마토
https://www.acmicpc.net/problem/7576
"""

from collections import deque



dx = [0,0,-1,1]
dy = [-1,1,0,0]


m, n = map(int, input().split())

def bfs():
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            if matrix[nx][ny] == 0:
                matrix[nx][ny] = matrix[x][y] + 1
                queue.append((nx,ny))
        

matrix = []
for _ in range(n):
    matrix.append(list(map(int, input().split())))

queue = deque()
for i in range(n):
    for j in range(m):
        if matrix[i][j] == 1:
            queue.append((i,j))

bfs()
result = 0
for i in matrix:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    result = max(result, max(i))
print(result - 1)

for i in range(n):
    print(matrix[i])