from collections import deque
import sys

input = sys.stdin.readline


N, H, D = map(int,input().split())
# 한변 길이, 체력, 우산내구도

#우산 사용 시작떄부터 내구도 감소

#u우산 현재s 도착 e 빈칸 
visited = [[0]*N for _ in range(N)]
matrix = []
for _ in range(N):
    matrix.append(input().rstrip())

dx = [-1,0,0,1]
dy = [0,-1,1,0]

def bfs(a,b):
    global H
    q = deque()
    q.append((a,b))
    visited[a][b] = 1
    while q:
        H -= 1
        for _ in range(len(q)):
            x,y = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < N and 0 <= ny < N:
                    if matrix[nx][ny] == 'E':
                        return visited[x][y]
                    if visited[nx][ny] == 0:
                        if matrix[nx][ny] == 'U':
                            H += D
                            visited[nx][ny] = visited[x][y] + 1
                            q.append((nx,ny))
                        else:
                            visited[nx][ny] = visited[x][y] + 1
                            q.append((nx,ny))
                    elif visited[nx][ny] < visited[x][y]:
                        visited[nx][ny] = visited[x][y] + 1
                        q.append((nx,ny))
        if H == 0:
            return -1
        
        for i in visited:
            print(i)
        print()
        

for i in range(N):
    for j in range(N):
        if matrix[i][j] == 'S':
            print(bfs(i,j))
            break