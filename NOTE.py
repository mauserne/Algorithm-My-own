from collections import deque
import sys

input = sys.stdin.readline


N, H, D = map(int, input().split())

matrix = []
for _ in range(N):
    matrix.append(input().rstrip())

cord = []

#매트릭스 돌면서 좌표 수집
for i in range(N):
    for j in range(N):
        cursor = matrix[i][j]

        if cursor == 'S':
            start = (i,j)
        elif cursor == 'U':
            cord.append((i,j))
        elif cursor == 'E':
            end = (i,j)

visited = [False]*len(cord)

x, y = start
q = deque()
q.append((x,y,H,0,0))
count = 0
result = sys.maxsize
while q:
    x,y,health,umb,cnt = q.popleft()
    # 현재 좌표 xy
    #health 현재 체력
    #umb 현재 우산 내구도
    #cnt 지금까지의 이동 횟수
    
    #현재 위치와 End 사이의 맨해탄 거리
    enddist = abs(x-end[0])+abs(y-end[1])
    
    if health + umb >= enddist: # 현재 체력과 우산으로 End까지 갈 수 있다면
        result = min(cnt+enddist, result)    # 최소 이동으로 End 도착하는 경우를 저장
        continue

    for ux, uy in cord:
        mattdist = abs(x-ux)+abs(y-uy) 
        if health + umb >= mattdist:
            next_health = health
            if umb == 0:
                next_health = health - mattdist +1
            elif umb - mattdist < 0:
                next_health = health + umb - mattdist+1
                
            if next_health <= 0:
                continue
            if visited[i] < next_health:
                q.append((ux,uy, next_health , D-1 , cnt+mattdist))
                visited[i] = next_health
if result != sys.maxsize:
    print(result)
else:
    print(-1) # 탐색 실패