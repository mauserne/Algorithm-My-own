"""
토마토 (3차원)
https://www.acmicpc.net/problem/7569
"""

import sys
from collections import deque

input = sys.stdin.readline



M, N, H = map(int, input().split())


matrix = []

for i in range(H):
    matrix.append([])
    for j in range(N):
        matrix[i].append(list(map(int,input().split())))


dz = [-1,0,0,0,0,1]
dx = [0,-1,0,0,1,0]
dy = [0,0,-1,1,0,0]


queue = deque()

allgood = True
for i in range(H):
    for j in range(N):
        for k in range(M):
            if matrix[i][j][k] == 1:
                queue.append((i,j,k))
            elif matrix[i][j][k] == 0:
                allgood = False

if allgood:
    print(0)
    exit(0)

days = 0
while queue:
    for _ in range(len(queue)):
        a,b,c = queue.popleft()

        for i in range(6):
            nz = dz[i] + a
            nx = dx[i] + b
            ny = dy[i] + c

            if 0<=nz<H and 0<=nx<N and 0<=ny<M:
                if matrix[nz][nx][ny] == 0:
                    matrix[nz][nx][ny] = 1
                    queue.append((nz,nx,ny))
    days += 1

for i in range(H):
    for j in range(N):
        for k in range(M):
            if matrix[i][j][k] == 0:
                print(-1)
                exit(0)

print(days-1)