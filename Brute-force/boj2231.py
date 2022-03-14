"""
분해합
https://www.acmicpc.net/problem/2231

time spent : 25min
"""


n = int(input())

for i in range(1,n+1):
    result = i
    a = str(i)
    for j in a:
        result += int(j)
    if n == result:
        print(i)
        break
    elif i == n:
        print(0)