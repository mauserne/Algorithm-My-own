"""
제곱수의 합
https://www.acmicpc.net/problem/1699
https://lakelouise.tistory.com/61
"""

n = int(input())

dp = [i for i in range(n+1)]

for i in range(1,n+1):
    for j in range(1, i):
        if j**2 > i :
            break
        if dp[i] > dp[i - j**2] + 1:
            dp[i] = dp[i - j**2] + 1

print(dp[n])