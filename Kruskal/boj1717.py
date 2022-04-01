"""
집합의 표현
https://www.acmicpc.net/problem/1717
"""


import sys
sys.setrecursionlimit(100000)

input = sys.stdin.readline


n, m = map(int, input().split())

parents = [0] * (n+1)

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


for i in range(1, n+1):
    parents[i] = i

for _ in range(m):
    a,b,c = map(int, input().split())
    if a:
        if find_parent(parents, c) == find_parent(parents, b):
            print('YES')
        else:
            print('NO')
    else:
        union_parent(parents, b, c)