# 우산의 갯수는 0 이상 10 이하
# 현재위치 Start 와 안전지대 End 를 제외한 모든 곳에 죽음의 비가 내린다.
# 우산의 내구도는 D로 동일하다. 우산을 획득하는 순간 비에 맞아 내구도가 1 감소
# 새로운 우산을 획득하면 가지고 있던 우산은 버린다.
# 맨몸으로 비를 맞으면 체력이 1감소, 우산이 비에 대신 맞으면 내구도 1감소
# 우산 내구도가 0이 되면 파괴, 체력이 0이 되면 사망

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
    #현재 좌표 x,y
    #health 현재 체력
    #umb 현재 우산 내구도
    #cnt 현재 이동횟수

    enddist = abs(x-end[0])+abs(y-end[1]) # 현재 위치로부터 End 사이의 맨해탄거리
    if health + umb >= enddist: # 현재 체력과 우산으로 End까지 갈 수 있다면
        result = min(cnt+enddist, result) # Start에서 End까지 이동하는 최소 이동거리 저장
        continue

    for i in range(len(cord)): # 우산들 좌표 확인하기
        mattdist = abs(x-cord[i][0])+abs(y-cord[i][1]) # 현재 위치로부터 우산들 사이의 맨해탄거리
        if health + umb >= mattdist: # 현재 체력과 우산으로 다음 우산까지 갈 수 있다면
            next_health = health    # 이동 후 체력 임시 저장
            if umb == 0:    # 우산이 없다면
                next_health = health - mattdist +1 # 이동 후 체력은 현재 체력 - 거리 +1
            elif umb - mattdist < 0: # 이동 중에 우산이 파괴된다면 
                next_health = health + umb - mattdist+1 # 이동 후 체력은 현재 체력 + 우산 - 거리 +1
                # 거리 +1 인 이유는 우산이 있는 곳은 우산이 대신 비를 맞기 때문
                
            if next_health <= 0: # 이동 후 체력이 0 이하인 경우의 수는 제외
                continue
            if visited[i] < next_health: # 이전 방문 보다 높은 체력으로 방문한다면 더 멀리 이동 할 수 있다.
                q.append((cord[i][0],cord[i][1], next_health , D-1 , cnt+mattdist))
                # (이동 후 좌표x,y, 이동 후 체력, 우산 내구도, 이동횟수)
                # 우산은 획득하는 순간 비에 맞으므로 내구도D-1
                # 디음 이동횟수는 지금까지의 이동횟수 + 거리
                visited[i] = next_health    # 방문기록에 이동 후 체력 저장
if result != sys.maxsize:
    print(result)   # End 탐색 성공
else:
    print(-1) # 탐색 실패