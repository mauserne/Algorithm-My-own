"""
피보나치 수 2
https://www.acmicpc.net/problem/2748
time spent : 3.5min
"""

dp = [0] * 91

dp[0] = 0
dp[1] = 1

n = int(input())

for i in range(2,n+1):
    dp[i] = dp[i-1] + dp[i-2]

print(dp[n])