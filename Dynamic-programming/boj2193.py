"""
이친수
https://www.acmicpc.net/problem/2193
"""
# 직접 푼 dp 문제 !!

n = int(input())

dp = [[0,0] for i in range(n+1)]

dp[1][1] = 1

for i in range(2,n+1):
    for j in range(2):
        if j == 0:
            dp[i][0] = dp[i-1][j]
            dp[i][1] = dp[i-1][j]
        else:
            dp[i][0] += dp[i-1][j]

print(sum(dp[n]))