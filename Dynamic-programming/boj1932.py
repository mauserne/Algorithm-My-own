"""
정수 삼각형
https://www.acmicpc.net/problem/1932
"""

import sys



n = int(input())


arr = []
for _ in range(n):
    arr.append(list(map(int,sys.stdin.readline().split())))

for i in range(1,n):
    for j in range(len(arr[i])):
        if j == 0:
            arr[i][j] = (arr[i][j] + arr[i-1][j])
        elif j == len(arr[i]) -1:
            arr[i][j] = (arr[i][j] + arr[i-1][j-1])
        else:
            arr[i][j] = max(arr[i][j] + arr[i-1][j-1] , arr[i][j] + arr[i-1][j])

print(max(arr[n-1]))