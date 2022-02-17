"""
덱
https://www.acmicpc.net/problem/10866
time spent : 18min
"""

import sys
from collections import deque

n = int(input())

deque1 = deque() 

for _ in range(n):
    command = sys.stdin.readline().split()
    if command[0] == 'push_front':
        deque1.appendleft(command[1])

    if command[0] == 'push_back':
        deque1.append(command[1])

    if command[0] == 'pop_front':
        if len(deque1) == 0:
            print(-1)
        else:
            print(deque1.popleft())

    if command[0] == 'pop_back':
        if len(deque1) == 0:
            print(-1)
        else:
            print(deque1.pop())

    if command[0] == 'size':
        print(len(deque1))

    if command[0] == 'empty':
        if len(deque1) == 0:
            print(1)
        else:
            print(0)

    if command[0] == 'front':
        if len(deque1) == 0:
            print(-1)
        else:
            print(deque1[0])
            
    if command[0] == 'back':
        if len(deque1) == 0:
            print(-1)
        else:
            print(deque1[-1])