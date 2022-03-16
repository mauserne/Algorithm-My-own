"""
RGB 거리
https://www.acmicpc.net/problem/1149
"""

#2차원 dp??

import sys



n = int(input())

arr = []
for _ in range(n):
    arr.append(list(map(int,sys.stdin.readline().split())))


dp = [] * n

for i in range(n):
    dp[i] = min(dp[i],)
