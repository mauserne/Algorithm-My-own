"""
숨바꼭질
https://www.acmicpc.net/problem/1697
"""


from collections import deque


N, K = map(int, input().split())

time = [0] * (10**5+1)

def bfs(n):
    queue = deque()
    queue.append(n)
    time[n] = 1
    while queue:
        x = queue.popleft()

        if x == K:
            return time[x]-1

        for i in [x-1,x+1,x*2]:
            if 0 <= i <= 10**5:
                if time[i] == 0:
                    queue.append(i)
                    time[i] = time[x] + 1

print(bfs(N))