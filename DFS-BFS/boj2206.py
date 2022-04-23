from collections import deque



N, M = map(int, input().split())

matrix = []
matrix.append([0] * (M+1))

for i in range(N):
    arr = [0]
    a = input()
    for j in a:
        if j == '0':
            arr.append(0)
        else:
            arr.append(-1)
    matrix.append(arr)

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

result = []

def wallbfs(a,b,z):
    q2 = deque()
    q2.append((a,b))
    submatrix = list(matrix)

    print('1번',matrix[a][b])
    print('2번',submatrix[a][b])

    submatrix[a][b] = z
    print('3번',submatrix[a][b])
    print('4번',matrix[a][b])

    while q2:
        x,y = q2.popleft()
        
        if (x,y) == (N,M):
            result.append(submatrix[x][y])
            return
        
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if 1 <= nx <= N and 1<=ny<=M:
                if submatrix[nx][ny] == 0:
                    submatrix[nx][ny] = submatrix[x][y] + 1
                    q2.append((nx,ny))

q1 = deque()
q1.append((1,1))
matrix[1][1] = 1
while q1:
    x,y = q1.popleft()
    
    if (x,y) == (N,M):
        result.append(matrix[x][y])
    
    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y
        if 1 <= nx <= N and 1<=ny<=M:
            if matrix[nx][ny] == 0:
                matrix[nx][ny] = matrix[x][y] + 1
                q1.append((nx,ny))
            elif matrix[nx][ny] == -1:
                wallbfs(nx,ny,matrix[x][y]+1)
                matrix[nx][ny] = -2

if result:
    print(min(result))
else:
    print(-1)