"""
접미사 배열
https://www.acmicpc.net/problem/11656
"""
s = input()
stack = []

count = 0
for i in range(len(s)):
    stack.append(s[i:])
    count += 1

stack.sort()
for i in stack:
    print(i)