"""
퇴사 2
https://www.acmicpc.net/problem/15486
https://dogsavestheworld.tistory.com/m/142
https://ojt90902.tistory.com/475
"""

n = int(input())

dp = [0]*(n+1)
t = [0]*n
p = [0]*n

for i in range(n):
  t[i],p[i] = map(int, input().split())

for i in range(n):
    if t[i] <= n - i:
        dp[i + t[i]] = max(dp[i] + p[i], dp[i+t[i]])
    dp[i+1] = max(dp[i+1], dp[i])

print(max(dp))