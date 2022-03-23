"""
섬의 개수
https://www.acmicpc.net/problem/4963
"""

import sys
sys.setrecursionlimit(10000)



dx = [-1, 0, 1]
dy = [-1, 0, 1]

def dfs(x,y):
    matrix[x][y] = 2 
    for i in dx:
        for j in dy:
            nx = x + i
            ny = y + j

            if (nx,ny) == (0,0) or nx<0 or nx>=h or ny<0 or ny>=w:
                continue
            if matrix[nx][ny] == 1:
                dfs(nx,ny)

result = []
while True:
    w, h = map(int,input().split())
    if (w,h) == (0,0):
        break
    matrix = []

    for i in range(h):
        matrix.append(list(map(int,input().split())))

    count =0

    for i in range(h):
        for j in range(w):
            if matrix[i][j] == 1:
                dfs(i,j)
                count += 1
    result.append(count)

for i in result:
    print(i)