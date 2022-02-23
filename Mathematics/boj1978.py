"""
소수찾기
https://www.acmicpc.net/problem/1978
"""

import sys

n = int(input())

#소수는 .. 약수가 자기와 1만있지
#모든 홀수가 소수는아님
#1과 자기이외에 나눠서 나누어 떨어지는 수가 있으면 소수가 아님
# 홀수로 나누어서
result = n

a = list(map(int,sys.stdin.readline().split()))
for i in a:
    count = 3

    if i == 2:
        continue
    elif i == 1 or i%2 == 0:
        result -= 1
    else:
        while count < i :
            if i%count == 0:
                result -= 1
                break
            count += 2
            
print(result)