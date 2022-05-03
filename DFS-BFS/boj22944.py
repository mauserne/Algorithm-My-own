#맨해탄 거리 ??

from collections import deque
import sys

input = sys.stdin.readline


N, H, D = map(int, input().split())

matrix = []
for _ in range(N):
    matrix.append(input().rstrip())
# 각 좌표별로 거리 구하고 성공할수있는지 찾기

cord = []

#매트릭스 돌면서 좌표 수집
for i in range(N):
    for j in range(N):
        cursor = matrix[i][j]

        if cursor == 'S':
            start = (i,j)
        elif cursor != '.':
            cord.append((i,j))
            if cursor == 'E':
                end = (i,j)

visited = [[0,0]for _ in range(len(cord))]

x, y = start
q = deque()
q.append((x,y,H,0,0))
count = 0
print('end',end)
result = []
while q:
    print(q)
    x,y,health,umb,cnt = q.popleft()
    #health 현재 체력
    #umb 현재 우산 내구도
    #cnt 지금까지의 이동 횟수
    for i in range(len(cord)):
        #각 지점과 현재위치 사이의 맨해탄 거리
            mattdist = abs(x-cord[i][0])+abs(y-cord[i][1])
            print(cnt,x,y,cord[i],mattdist)
            if health + umb >= mattdist:
                next_health = health
                if umb == 0:
                    next_health = health - mattdist +1
                elif umb - mattdist < 0:
                    next_health = health + umb - mattdist+1
                    print(health,umb,mattdist,next_health,cord[i])
                if cord[i] == end:  # E 탐색 성공
                    result.append(cnt+mattdist)
                    continue
                if next_health <= 0:    # 체력이 0 이하로 떨어지면 ㅃ
                    continue
                if visited[i][0] < next_health:    # 이전 방문보다 높은 체력으로 방문해서 더 멀리갈 수 있다면 append
                    q.append((cord[i][0],cord[i][1], next_health , D-1 , cnt+mattdist))
                    visited[i][0] = next_health
if result:
    #최소 이동으로 E에 방문할때를 출력
    print(min(result))
else:
    print(-1) # 탐색 실패