"""
나이트의 이동
https://www.acmicpc.net/problem/7562
"""
from collections import deque
import sys


input = sys.stdin.readline


tcase = int(input())

dx = [-2,-2,-1,-1,1,1,2,2]
dy = [-1,1,-2,2,-2,2,-1,1]



def bfs(a,b):
    queue = deque()
    queue.append((a,b))
    matrix[a][b] = 1

    while queue:
        p, k = queue.popleft()
        if (p,k) == (x,y):
            return matrix[p][k] -1

        else:
            for i in range(8):
                nx = p + dx[i]
                ny = k + dy[i]

                if nx<0 or nx>=n or ny<0 or ny>=n:
                    continue
                if matrix[nx][ny] == 0:
                    queue.append((nx,ny))
                    matrix[nx][ny] = matrix[p][k] + 1

for _ in range(tcase):
    # 체스판 크기
    n = int(input())

    matrix = [[0]*(n) for _ in range(n)]
    # 나이트 위치
    a, b = map(int, input().split())
    x, y = map(int, input().split())

    print(bfs(a,b))
    # 목적지

    #몇번만에 이동할수 있는가?