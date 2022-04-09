"""
N과 M (2)
https://www.acmicpc.net/problem/15650
"""

N, M = map(int, input().split())

s = []

def dfs(start):
    if len(s) == M:
        print(' '.join(map(str, s)))
        return
    
    for i in range(start, N+1):
        if i in s:
            continue
        s.append(i)
        dfs(i+1)
        s.pop()

dfs(1)