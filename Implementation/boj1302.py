"""
베스트셀러
https://www.acmicpc.net/problem/1302
time spent : 18min
"""


import sys

input = sys.stdin.readline


N = int(input())

dic = dict()

for _ in range(N):
    a = input().rstrip()
    if not a in dic:
        dic[a] = 1
    else:
        dic[a] += 1

maxval = 1
maxbooks = []

for key, value in dic.items():  #dic.items()는 뭘까
    if value == maxval:
        maxbooks.append(key)
    elif value > maxval:
        maxval = value
        maxbooks = [key]

print(sorted(maxbooks)[0])
#람다도 공부해야할듯~