"""
1, 2, 3 더하기 3
https://www.acmicpc.net/problem/15988
"""

import sys


n = int(input())


dp = [0] * 1000001

dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in range(4,1000001):
    dp[i] = dp[i-1] % 1000000009 + dp[i-2] % 1000000009 + dp[i-3] % 1000000009

for _ in range(n):
    t = int(sys.stdin.readline().rstrip())
    print(dp[t] % 1000000009)