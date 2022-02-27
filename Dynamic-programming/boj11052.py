"""
카드 구매하기
https://www.acmicpc.net/problem/11052
"""

n = int(input())

arr = [0] + list(map(int,input().split()))

dp = [0] * (n+1)

for i in range(1,n+1):
    print(i,'개의 카드 선택')
    dp[i] = arr[i]
    for j in range(1,i+1):
        dp[i] = max(dp[i],dp[i-j]+dp[j])
        print(dp[i])

print(dp[n])