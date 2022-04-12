"""
동전 0
https://www.acmicpc.net/problem/11047
"""

N, k = map(int, input().split())

arr = []
for _ in range(N):
    arr.append(int(input()))

count = 0
for i in arr[::-1]:
    if k // i:
        count += k//i
        k = k%i

print(count)