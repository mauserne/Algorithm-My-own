import math
import sys

t = int(input())

# n의 최대값인 1000000의 에라토스테네스의 체
arr = [True for _ in range(1000000+1)]
for i in range(2,int(math.sqrt(1000000))+1): #1000000의 제곱근 1000+1
    if arr[i]:
        for j in range(i + i , 1000000+1, i): #소수 판별된 수의 배수는 소수 아님
            arr[j] = False
            
#t번 반복해서 정수 n 입력받고 골드바흐 판별
for _ in range(t):
    result = 0
    n = int(sys.stdin.readline().rstrip())

    for i in range(2,n//2+1):
        if arr[i] and arr[n-i]:
            result += 1
    print(result)