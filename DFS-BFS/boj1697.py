from collections import deque


N, K = map(int, input().split())

def bfs():
    q = deque()
    q.append(N)
    while q:
        x = q.popleft()
        if x == K:
            print(time[x])
            return
        for nx in (x-1, x+1, x*2):
            if 0 <= nx <= MAX and not time[nx]:
                time[nx] = time[x] + 1
                q.append(nx)

MAX = 10**5 
time = [0] * (MAX +1)

bfs()