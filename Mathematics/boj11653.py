"""
소인수분해
https://www.acmicpc.net/problem/11653
time spent : 8min
"""

n = int(input())

for i in range(2, int(n**0.5)+1):
    while n % i == 0:
        print(i)
        n //= i
if n != 1:
    print(n)
