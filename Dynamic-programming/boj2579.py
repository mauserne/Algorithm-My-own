"""
계단 오르기
https://www.acmicpc.net/problem/2579
"""
import sys

n = int(input())

stair = [0] * 301
#각 계단의 점수 저장

for i in range(1,n+1):
    stair[i] = int(sys.stdin.readline().rstrip())

dp = [0] * 301
#각 계단까지 이동했을떄의 점수 저장

dp[1] = stair[1]
dp[2] = dp[1] + stair[2]

for i in range(3,n+1):
    dp[i] = max(dp[i-3]+stair[i-1]+stair[i], dp[i-2]+stair[i])

print(dp[n])