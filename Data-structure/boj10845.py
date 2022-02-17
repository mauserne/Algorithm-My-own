"""
큐
https://www.acmicpc.net/problem/10845
time spent : 29min
"""

from collections import deque
import sys

n = int(input())

queue = deque()
for _ in range(n):
    command = sys.stdin.readline().split()
    if command[0] =='push':
        queue.append(command[1])
    if command[0] == 'size':
        print(len(queue))
    if command[0] == 'pop':
        if len(queue) <= 0:
            print(-1)
        else:
            print(queue.popleft())
        #큐 가장앞 제거
    if command[0] == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    if command[0] == 'front':
        if len(queue) <= 0:
            print(-1)
        else:
            print(queue[0])
    if command[0] == 'back':
        if len(queue) <= 0:
            print(-1)
        else: 
            print(queue[-1])


# 출력해야하는 명령이 주어질 때마다, 한 줄에 하나씩 출력한다.