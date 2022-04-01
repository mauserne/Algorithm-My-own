"""
여행 가자
https://www.acmicpc.net/problem/1976
"""

import sys

input = sys.stdin.readline


N = int(input())
M = int(input())

parents = [0] * (N+1)

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parents[b] = a
    else:
        parents[a] = b


for i in range(1, N+1):
    parents[i] = i

for i in range(1, N+1):
    arr = list(map(int, input().split()))
    for j in range(N):
        if arr[j]:
            union_parent(parents, i, j+1)

plan = list(map(int, input().split()))

tmp = find_parent(parents,plan[0])
for i in plan:
    if tmp != find_parent(parents,i):
        print('NO')
        exit(0)

print('YES')