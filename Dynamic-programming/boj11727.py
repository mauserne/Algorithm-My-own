"""
2xn 타일링 2
https://www.acmicpc.net/problem/11727

"""

n = int(input())

dp = [0] * 1001

dp[1] = 1
dp[2] = 3

for i in range(3,n+1):
    dp[i] = dp[i-1] + dp[i-2]*2

print(dp[n]%10007)

#방법이 한가지있고, 반복하던지 해서 가짓수나 결과를 출력해라 -> 그리디
#방법이 여러가지 있는데, 최적의 방법 가짓수를 출력해라 (모든 방법 계산) -> dp