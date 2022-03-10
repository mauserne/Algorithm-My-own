"""
피보나치 수 5
https://www.acmicpc.net/problem/10870
time spent : 6min
"""

n = int(input())

def fibo(x):
    if x == 0:
        return 0
    if x == 1:
        return 1
    return fibo(x-1) + fibo(x-2)

print(fibo(n))