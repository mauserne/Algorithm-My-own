"""
오큰수
https://www.acmicpc.net/problem/17298
"""

n = int(input())
number = list(map(int,input().split()))

output=[-1 for _ in range(n)]

stack = [0]
for i in range(1,n):
    while stack and number[stack[-1]] < number[i]:
        output[stack.pop()] = number[i] 
    stack.append(i)

print(' '.join(map(str,output)))