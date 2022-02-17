"""
2트
요세푸스 문제
https://www.acmicpc.net/problem/1158
time spent : 22min
"""


from collections import deque

n, k = map(int,input().split())

queue1 = deque()

output = []

for i in range(1,n+1):
    queue1.append(i)

while len(queue1) != 0:
    for _ in range(k-1):
        queue1.append(queue1.popleft())
    output.append(queue1.popleft())

print('<%s>' %', '.join(map(str, output)))