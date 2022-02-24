"""
GCD 합
https://www.acmicpc.net/problem/9613
"""

import sys

t = int(input())

def gcd(x,y):
    while y > 0 :
        x = x%y
        x,y = y,x
    return x

for _ in range(t):
    result = 0
    n = list(map(int,sys.stdin.readline().split()))

    for i in range(1,n[0]):
        for j in range(i+1, n[0]+1):
            result += gcd(n[i],n[j])
    print(result)