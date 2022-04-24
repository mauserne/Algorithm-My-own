"""
맥주 마시면서 걸어가기
https://www.acmicpc.net/problem/9205
"""
import sys
from collections import deque

input = sys.stdin.readline


t = int(input())
for _ in range(t):
    ways = []

    n = int(input())
    visited = [False] * (n+1)

    a,b = map(int, input().split())
    now = (a,b)

    for _ in range(n):
        a, b = map(int,input().split())
        ways.append((a,b))
    a, b = map(int,input().split())
    ways.append((a,b))
    goal = (a,b)

    def search(now):
        q = deque()
        q.append(now)
        while q:
            x0, y0 = q.popleft()
            for i in range(n+1):
                if not visited[i]:
                    x1,y1 = ways[i]
                    if abs(x0-x1) + abs(y0-y1) <= 1000:
                        visited[i] = True
                        q.append((x1,y1))
                        if (x1,y1) == goal:
                            return 'happy'
        return 'sad'
    
    print(search(now))