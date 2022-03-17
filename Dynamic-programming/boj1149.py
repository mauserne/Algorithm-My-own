"""
RGB 거리
https://www.acmicpc.net/problem/1149
"""

import sys



n = int(input())

arr = []
for _ in range(n):
    arr.append(list(map(int,sys.stdin.readline().split())))

for i in range(1,n):
    arr[i][0] = min(arr[i-1][1] , arr[i-1][2]) + arr[i][0]
    arr[i][1] = min(arr[i-1][0] , arr[i-1][2]) + arr[i][1]
    arr[i][2] = min(arr[i-1][0] , arr[i-1][1]) + arr[i][2]

print(min(arr[i][0] , arr[i][1] , arr[i][2]))