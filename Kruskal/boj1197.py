import sys



input = sys.stdin.readline



V, E = map(int, input().split())
# 정점, 간선

parents = [0] * (V+1)

for i in range(1, V+1):
    parents[i] = i

edge = []
result = 0

for _ in range(E):
    a,b,cost = map(int, input().split())
    edge.append((cost,a,b))

edge.sort()

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

for i in edge:
    cost, a, b = i

    if find_parent(parents, a) == find_parent(parents, b):
        continue
    else:
        union_parent(parents, a, b)
        result += cost 

print(result)