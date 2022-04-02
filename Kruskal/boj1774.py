import sys
import math


input = sys.stdin.readline

def find_parent(x):
    if parents[x] != x:
        parents[x] = find_parent(parents[x])
    return parents[x]

def union_parent(x,y):
    x = find_parent(x)
    y = find_parent(y)
    if x < y:
        parents[y] = x
    else:
        parents[x] = y



N, M = map(int, input().split())

parents = [0] * (N+1)

for i in range(1, N+1):
    parents[i] = i

cord = [0] * (N+1)

for i in range(1, N+1):
    a,b = map(int, input().split())
    cord[i] = (a,b)

for _ in range(M):
    a,b = map(int, input().split())
    union_parent(a,b)

edge = []

for i in range(1,N):
    a,b = cord[i]
    for j in range(i+1, N+1):
        edge.append((math.sqrt((cord[j][0] - cord[i][0])**2 + (cord[j][1] - cord[i][1])**2),i,j))

edge.sort()
result = 0

for i in edge:
    cost, a, b = i
    if find_parent(a) != find_parent(b):
        union_parent(a,b)
        result += cost

print('%.2f' %(result))