"""
1, 2, 3 더하기
https://www.acmicpc.net/problem/9095

"""

import sys

dp = [0] * 11

dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in range(4,11):
    dp[i] = dp[i-3] + dp[i-2] + dp[i-1]

t = int(input())

for _ in range(t):
    n = int(sys.stdin.readline().rstrip())
    if 3 > n:
        print(dp[n])
    else:
        print(dp[n])