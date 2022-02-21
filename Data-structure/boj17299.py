"""
오등큰수
https://www.acmicpc.net/problem/17299
"""

from collections import Counter

n = int(input())

number = list(map(int,input().split()))
nums_count = Counter(number)

output = [-1 for _ in range(n)]

stack = []
for i in range(len(number)):
    while stack and nums_count[number[stack[-1]]] < nums_count[number[i]]:
        output[stack.pop()] = number[i]
    stack.append(i)

print(' '.join(map(str,output)))