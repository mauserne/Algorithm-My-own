"""
움직이는 미로 탈출
https://www.acmicpc.net/problem/16954
"""

from collections import deque


dx = [-1,-1,-1,0,0,0,1,1,1]
dy = [-1,0,1,-1,0,1,-1,0,1]

def bfs():
    queue = deque()
    queue.append((7,0))
    time = 0

    while queue:
        visited = [[False]*8 for _ in range(8)]

        for _ in range(len(queue)):
            a, b = queue.popleft()
            #print(time, (a,b))
            if matrix[a][b] == -1:
                continue
            if (a,b) == (0,7):
                return 1

            for i in range(9):
                nx = dx[i] + a
                ny = dy[i] + b

                if not (0 <= nx < 8 and 0 <= ny < 8):
                        continue
                if matrix[nx][ny] == -1 or visited[nx][ny]:
                        continue
                visited[nx][ny] = True
                queue.append((nx,ny))
        
        matrix.pop()
        matrix.appendleft([0]*8)

        time += 1
        if time == 9:
            return 1
    return 0

matrix = deque([[]for _ in range(8)])
for i in range(8):
    for j in input():
        if j == '.':
            matrix[i].append(0)
        else:
            matrix[i].append(-1)

print(bfs())