n = int(input())

arr = list(map(int,input().split()))

dp = [1] * n
# 수열이 i까지일떄 증가하는 부분수열의 길이 

for i in range(n):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i],dp[j]+1)

dpmax = max(dp)

result = []
count = dpmax
dp = dp[::-1]
arr = arr[::-1]

while count > 0:
    for i in range(n):
        if dp[i] == count:
            result.append(arr[i])
            count -= 1

print(dpmax)
print(' '.join(map(str,result[::-1])))