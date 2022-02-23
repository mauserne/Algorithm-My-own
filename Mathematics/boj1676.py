"""
팩토리얼 0의 개수
https://www.acmicpc.net/problem/1676
time spent : 15min
"""

n = int(input())

output = 1
for i in range(1,n+1):
    output *= i

output = str(output)
result = 0
for i in output[::-1]:
    if i == '0':
        result += 1
    else:
        break
print(result)