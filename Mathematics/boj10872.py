"""
팩토리얼
https://www.acmicpc.net/problem/10872
time spent : 2m 30s
"""


n = int(input())

output = 1
for i in range(1,n+1):
    output *= i
print(output)