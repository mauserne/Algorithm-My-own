"""
피보나치 수열
https://www.codeup.kr/problem.php?id=2601
"""


dp = [0] * (41)

dp[1] = 1
dp[2] = 1

n = int(input())

for i in range(3,n+1):
    dp[i] = dp[i-1] + dp[i-2]

print(dp[n])
