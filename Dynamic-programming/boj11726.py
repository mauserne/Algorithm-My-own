"""
2xn 타일링
https://www.acmicpc.net/problem/11726

"""


n = int(input())

dp = [0] * (n+1)

if n == 1:
    print(1)
elif n == 2:
    print(2)
else:
    dp[1] = 1
    dp[2] = 2

    for i in range(3,n+1):
        dp[i] = dp[i-1] + dp[i-2]

    print(dp[n]%10007)