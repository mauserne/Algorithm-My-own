"""
안전영역
https://www.acmicpc.net/problem/2468
"""

import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline


N = int(input())

matrix = []
for _ in range(N):
  matrix.append(list(map(int, input().split())))

maxpart = 0
level = 0

dx = [-1,0,0,1]
dy = [0,-1,1,0]

def dfs(a,b):
  visited[a][b] = True
  for i in range(4):
    nx = dx[i] + a
    ny = dy[i] + b
    if 0<=nx<N and 0<=ny<N:
      if not visited[nx][ny] and matrix[nx][ny] > level:
        dfs(nx,ny)
  

while True:
  visited = [[False]*(N) for _ in range(N)]
  land = 0
  for i in range(N):
    for j in range(N):
      if not visited[i][j] and matrix[i][j] > level:
        dfs(i,j)
        land += 1
  if land == 0:
    break
  maxpart = max(land,maxpart)
  level += 1

print(maxpart)
