#BFS
"""
미로 탐색
https://www.acmicpc.net/problem/2178
"""
from collections import deque




n, m = map(int, input().split())


dx = [0,0,-1,1]
dy = [-1,1,0,0]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx<0 or nx>=n or ny<0 or ny>=m: 
                continue
            elif matrix[nx][ny] == 1:
                matrix[nx][ny] = matrix[x][y] + 1
                queue.append((nx,ny))
    
    return matrix[n-1][m-1]


matrix = []
for i in range(n):
    matrix.append(list(map(int , input())))

print(bfs(0,0))
for i in range(n):
    print(matrix[i])