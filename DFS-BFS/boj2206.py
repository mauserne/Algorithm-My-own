"""
벽 부수고 이동하기
https://www.acmicpc.net/problem/2206
190340 KB     6296ms
"""

from collections import deque
import sys


input = sys.stdin.readline

N, M = map(int, input().split())


visited = [ [ [0]*2 for _ in range(M) ]for _ in range(N)]

matrix = []
for _ in range(N):
    matrix.append(list(map(int,input().rstrip())))

dx = [-1,0,0,1]
dy = [0,-1,1,0]

def bfs():
    q = deque()
    q.append((0,0,0))
    visited[0][0][0] = 1
    while q:
        x, y, z = q.popleft()
        if x == N-1 and y == M-1:
            return visited[x][y][z]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if matrix[nx][ny] == 1 and z == 0:
                    visited[nx][ny][1] = visited[x][y][0] + 1
                    q.append((nx,ny,1))
                elif matrix[nx][ny] == 0 and visited[nx][ny][z] == 0:
                    visited[nx][ny][z] = visited[x][y][z] + 1
                    q.append((nx,ny,z))
    return -1

print(bfs())