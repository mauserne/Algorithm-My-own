"""
좌표 압축
https://www.acmicpc.net/problem/18870
"""


N = int(input())

arr = list(map(int, input().split()))

set1 = sorted(set(arr))

dic1 = dict()
for i in range(len(set1)):
    dic1[set1[i]] = i

for i in arr:
    print(dic1[i], end = ' ')