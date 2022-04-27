"""
로봇 청소기
https://www.acmicpc.net/problem/14503
"""


import sys

input = sys.stdin.readline


N, M = map(int, input().split())
r,c,d = map(int, input().split())
#둘째 줄에 로봇 청소기가 있는 칸의 좌표 (r, c)와 바라보는 방향 d가 주어진다. 
#d가 0인 경우에는 북쪽을, 1인 경우에는 동쪽을, 2인 경우에는 남쪽을, 3인 경우에는 서쪽을 바라보고 있는 것이다.
matrix = []
for _ in range(N):
    matrix.append(list(map(int,input().split())))

dx = [-1,0,1,0]
dy = [0,1,0,-1]

count = 1
x = r
y = c

while True:
    foundway = False
    matrix[x][y] = 2 # 현재위치를 청소한다

    for _ in range(4):
        d = (d+3)%4
        nx = x + dx[d]
        ny = y + dy[d]

        if 0 < nx < N and 0 < ny < M:
            if matrix[nx][ny] == 0:
                x = nx
                y = ny
                foundway = True
                count += 1
                break
        
    if not foundway:
        nx = x + dx[(d+2)%4]
        ny = y + dy[(d+2)%4]
        if matrix[nx][ny] == 1:
            print(count)
            exit()
        else:
            x = nx
            y = ny
        