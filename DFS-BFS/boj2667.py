#DFS
"""
단지번호붙이기
https://www.acmicpc.net/problem/2667
"""

import sys



n = int(input())

graph = []

for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().rstrip())))

house = 0

def dfs(x,y):
    global house
    if x<0 or x>=n or y<0 or y>=n:
        return False

    if graph[x][y] == 1:
        graph[x][y] = 0
        house += 1
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y-1)
        dfs(x,y+1)
        return True
    return False

result = []
for i in range(n):
    for j in range(n):
        if dfs(i,j):
            result.append(house)
            house = 0

print(len(result))
result.sort()
for i in result:
    print(i)

#각 단지에 속하는 집의 수를 오름차순으로 정렬후 출력