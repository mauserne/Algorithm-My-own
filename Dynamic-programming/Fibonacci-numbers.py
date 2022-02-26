dp = [0] * 101
# 0부터 100까지의 dp 테이블

dp[0] = 1
dp[1] = 1

#2부터 100번째까지 피보나치 수열 구하기
for i in range(2,101):
    dp[i] = dp[i-1] + dp[i-2]

n = int(input())

print('피보나치 수열 %s번째 값 :'%n,dp[n])