"""
상근이의 여행
https://www.acmicpc.net/problem/9372
"""

# M-사이클 의 갯수 출력

import sys


input = sys.stdin.readline


T = int(input())

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, x, y):
    x = find_parent(parent, x)
    y = find_parent(parent, y)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y



for _ in range(T):
    N, M = map(int, input().split())
    result = M

    parents = [0] * (N+1)

    for i in range(1, N+1):
        parents[i] = i

    for _ in range(M):
        a,b = map(int, input().split())
        if find_parent(parents, a) == find_parent(parents, b):
            result -= 1
        else:
            union_parent(parents, a, b)
    print(result)