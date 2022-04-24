from collections import deque


N, M = map(int, input().split())
r,c,d = map(int, input().split())
#둘째 줄에 로봇 청소기가 있는 칸의 좌표 (r, c)와 바라보는 방향 d가 주어진다. 
#d가 0인 경우에는 북쪽을, 1인 경우에는 동쪽을, 2인 경우에는 남쪽을, 3인 경우에는 서쪽을 바라보고 있는 것이다.
matrix = []
for _ in range(N):
    matrix.append(list(map(int,input().split())))

def bfs():
    clean = 1
    q = deque()
    q.append((r,c,d))
    while q:
        print(q)
        x0,y0,d0 = q.popleft()
        matrix[x0][y0] = 2
        for i in matrix:
            print(i)
        if d0 == 0:
            if matrix[x0-1][y0] == 0:
                q.append((x0-1,y0,0))
                clean += 1
            else:
                d0 += 1
        elif d0 == 1:
            if matrix[x0][y0-1] == 0:
                q.append((x0,y0-1,1))
                clean += 1
            else:
                d0 += 1
        elif d0 == 2:
            if matrix[x0+1][y0] == 0:
                q.append((x0+1,y0,2))
                clean += 1
            else:
                d0 += 1
        elif d0 == 3:
            if matrix[x0][y0+1] == 0:
                q.append((x0,y0+1,3))
                clean += 1
            else:
                d0 += 1
        elif d0 == 4:
            if matrix[x0-1][y0] == 0:
                q.append((x0-1,y0,0))
                clean += 1
            else:
                d0 += 1
        elif d0 == 5:
            if matrix[x0][y0-1] == 0:
                q.append((x0,y0-1,1))
                clean += 1
            else:
                d0 += 1
        elif d0 == 6:
            if matrix[x0+1][y0] == 0:
                q.append((x0+1,y0,2))
                clean += 1
            else:
                d0 += 1
        elif d0 == 7:
            if matrix[x0][y0+1] == 0:
                q.append((x0,y0+1,3))
                clean += 1
            else:
                d0 += 1
        
        
    return clean


print(bfs())