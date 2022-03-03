"""
가장 긴 증가하는 부분 수열 4
https://www.acmicpc.net/problem/14002
https://my-coding-notes.tistory.com/266
"""
n = int(input())

dp = [0] * n

arr = list(map(int,input().split()))

for i in range(n):
    for j in range(i):
        if arr[i] > arr[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += 1


tmp = dp.index(max(dp))
result = []

for i in range(tmp,-1,-1):
    if dp[i] == 1:
        result.append(arr[i])
        break
    result.append(arr[i])

result.sort()
print(max(dp))
print(' '.join(map(str,result)))