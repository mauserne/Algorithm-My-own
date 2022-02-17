"""
스택
https://www.acmicpc.net/problem/10828
time spent : 38min
"""
import sys

n = int(sys.stdin.readline())

stack = []
for _ in range(n):
    a = sys.stdin.readline().split()
    print(a)
    if a[0] == 'push':
        stack.append(int(a[1]))

    elif a[0] == 'pop':
        if len(stack) == 0:
            print(-1)
        else: 
            print(stack[-1])
            del stack[-1]

    elif a[0] == 'size':
        print(len(stack))

    elif a[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)

    elif a[0] == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])