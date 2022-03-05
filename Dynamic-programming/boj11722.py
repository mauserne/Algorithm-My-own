"""
가장 긴 감소하는 부분 수열
https://www.acmicpc.net/problem/11722
"""

n = int(input())

dp = [1] * (n+1)
    # 수열이 i개까지 있을때의 부분 수열의 최대 길이 저장

arr = [0] + list(map(int,input().split()))
    # 전체수열 입력
    
for i in range(1,n+1):
    for j in range(i):
        if arr[i] < arr[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))