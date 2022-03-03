import sys

dp = [0] * 11

dp[1] = 1
dp[2] = 2
dp[3] = 4


t = int(input())
for _ in range(t):
    n = int(sys.stdin.readline().rstrip())
    if dp[n] != 0 :
        print(dp[n])
        continue
    for i in range(4,n+1):
        dp[i] = dp[i-3] + dp[i-2] + dp[i-1]
    print(dp[n])