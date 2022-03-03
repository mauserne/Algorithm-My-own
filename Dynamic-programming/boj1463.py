"""
1로 만들기
https://www.acmicpc.net/problem/1463
time spent : 1hour 3min
"""

dp = [0] * 1000001

dp[1] = 0
dp[2] = 1
dp[3] = 1

n = int(input())

for i in range(4,n+1):
    dp[i] = dp[i-1]+1
    if i % 3 == 0:
        dp[i] = min(dp[i],dp[i//3]+1)
    if i % 2 == 0:
        dp[i] = min(dp[i],dp[i//2]+1)

print(dp[n])