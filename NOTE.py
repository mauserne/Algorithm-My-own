n = int(input())

dp = [0] + [1] * n



arr = [0] + list(map(int,input().split()))

for i in range(1,n+1):
    for j in range(i):
        if arr[i] < arr[j]:
            dp[i] = max(dp[i], dp[j]+1)
    print(dp)
print(max(dp))