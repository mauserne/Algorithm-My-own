"""
빙산
https://www.acmicpc.net/problem/2573
"""
from collections import deque
import sys
sys.setrecursionlimit(10**4)

input = sys.stdin.readline



N, M = map(int, input().split())

matrix = []

for _ in range(N):
    matrix.append(list(map(int, input().split())))

year = 0
# dfs 반복, arr에 녹을곳 저장, 빙산분리 확인하고 재반복
# dfs 0번 >> 다 녹았음 >> 0 출력
# dfs 1번 >> 빙산이 1개임 >> 반복
# dfs 2번 이상 >> years 출력

dx = [-1,0,0,1]
dy = [0,-1,1,0]

def bfs(a,b):
    q = deque()
    q.append((a,b))
    visited[a][b] = True
    while q:
        x,y = q.popleft()

        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if 0 <= nx < N and 0 <= ny < M:
                if not visited[nx][ny] and matrix[nx][ny] < 1:
                    matrix[x][y] -= 1
                if not visited[nx][ny] and matrix[nx][ny] >0:
                    visited[nx][ny] = True
                    q.append((nx,ny))



"""
def dfs(a,b):


    visited[a][b] = True

    for i in range(4):
        nx = dx[i] + a
        ny = dy[i] + b

        if 0 <= nx < N and 0 <= ny < M:
            if not visited[nx][ny] and matrix[nx][ny] < 1:
                matrix[a][b] -= 1
            if not visited[nx][ny] and matrix[nx][ny] > 0:
                dfs(nx,ny)

"""


while True:
    part = 0
    visited = [[False]*M for _ in range(N)]

    for i in range(1,N-1):
        for j in range(1,M-1):
            if not visited[i][j] and matrix[i][j] > 0:
                part += 1
                if part >= 2:
                    print(year)
                    exit()
                bfs(i,j)
    
    if part == 0:
        print(0)
        break
    year += 1