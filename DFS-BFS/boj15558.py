"""
점프 게임
https://www.acmicpc.net/problem/15558
32476 KB 348ms
time spent : 46min
"""


from collections import deque
import sys

input = sys.stdin.readline


N, k = map(int, input().split())
# 0은 위험 1은 안전

matrix = []
for _ in range(2):
    arr = list(map(int, input().rstrip()))
    matrix.append(arr)
# matrix[0][0]부터 시작 
# N번 칸보다 더 큰 칸으로 이동하는 경우에는 게임을 클리어한 것이다.


def bfs():
    time = 0
    q = deque()
    q.append((0,0))
    while q:
        for _ in range(len(q)):
            x,y = q.popleft()
            if matrix[x][y] == 0:
                break
            if x == 0: 
                for a,b in (x,y+1),(x,y-1),(x+1,y+k):
                    if b >= N:
                        return 1 
                    elif 0 <= b:
                        if matrix[a][b] == 1:
                            matrix[a][b] = 2
                            q.append((a,b))
            elif x == 1:
                for a,b in (x,y+1),(x,y-1),(x-1,y+k):
                    if b >= N:
                        return 1
                    elif 0 <= b:
                        if matrix[a][b] == 1:
                            matrix[a][b] = 2 
                            q.append((a,b))
        for i in range(2):
            matrix[i][time] = 0

        time += 1

    return 0

print(bfs())
# 1은 통과 0는 실패