"""
소수 구하기
https://www.acmicpc.net/problem/1929
"""
#에라토스테네스의 체
#소수 판별 알고리즘

m, n = map(int,input().split())

output = [True] * n+1

def isPrime(num):
    if num == 1:
        output[num] = False
    else:
        for i in range(2, int(num**0.5)+1):
            if num % i ==0:
                return False
        return True


for i in range(m,n+1):
    if isPrime(i):
        print(i)