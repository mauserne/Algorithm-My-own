"""
IF문 좀 대신 써줘
https://www.acmicpc.net/problem/19637
"""

from bisect import bisect_left
import sys


input = sys.stdin.readline

n, m = map(int, input().split())


tag= []
level = []
for _ in range(n):
    a, b = input().split()
    tag.append(a)
    level.append(int(b))

result = []
for _ in range(m):
    result.append(bisect_left(level, int(input())))

for i in result:
    print(tag[i])