"""
가장 긴 증가하는 부분 수열
https://www.acmicpc.net/submit/11053
https://steadily-worked.tistory.com/638
"""


n = int(input())

arr = list(map(int,(input().split())))

dp = [1]*n

for i in range(1,n):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i],dp[j]+1)

print(max(dp))