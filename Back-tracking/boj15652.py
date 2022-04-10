"""
N과 M (4)
https://www.acmicpc.net/problem/15652
"""


N, M = map(int, input().split())

s = []

def dfs():
    if len(s) == M:
        print(' '.join(map(str, s)))
        return
    
    if s:
        for i in range(s[-1], N+1):
            s.append(i)
            dfs()
            s.pop()
    else:
        for i in range(1, N+1):
            s.append(i)
            dfs()
            s.pop()

dfs()