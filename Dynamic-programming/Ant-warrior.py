# 창고갯수 3<= n <= 100
#한칸이상 떨어진데 공격
#얻을수잇는 식량의 최대값

n = int(input())

arr = list(map(int,input().split))

dp = [0] * (100)
dp[0] = arr[0] # 창고가 하나 있을때 최적의 값
dp[1] = max(arr[0],arr[1]) # 창고가 두개있으면 최대값 골라서 최적의 값 결정

for i in range(2,n):
    dp[i] = max(dp[i-1],dp[i-2]+arr[i])

print(dp[n-1])
