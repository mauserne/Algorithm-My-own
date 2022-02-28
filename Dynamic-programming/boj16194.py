"""
카드 구매하기2
https://www.acmicpc.net/problem/16194
47
"""

n = int(input())
arr = [0] + list(map(int,input().split()))

#dp 테이블에 각 카드 갯수마다 최소값 저장
dp = [0]*(n+1)

for i in range(n+1):
    dp[i] = arr[i]
    for j in range(1,i+1):
        dp[i] = min(dp[i-j]+dp[j] , dp[i])

print(dp[i])
