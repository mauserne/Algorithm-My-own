import math
import sys

input = sys.stdin.readline

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

n = int(input())


parents = [0] * n

for i in range(n):
    parents[i] = i

arr = []

for _ in range(n):
    a,b = map(float, input().split())
    arr.append((a,b))

edges = []

for i in range(n):
    for j in range(i + 1, n):
        edges.append(((math.sqrt(((arr[i][0] - arr[j][0])**2)+(arr[i][1] - arr[j][1])**2)), i , j))

edges.sort()
    
result = 0

for i in edges:
    cost, a, b = i

    if find_parent(parents, a) != find_parent(parents, b):
        union_parent(parents, a, b)
        result += cost


print('%.2f' %(result))