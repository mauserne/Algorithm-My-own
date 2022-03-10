n = int(input())

arr = list(map(int,input().split()))


dp = [] * 1001
for i in range(1001):
    for j in range(i):
        if dp[i-1] and dp[j]:
            dp[i] = max(dp[i], dp[j] + dp[i-1])

print(max(dp))