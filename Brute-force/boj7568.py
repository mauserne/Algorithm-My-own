"""
덩치
https://www.acmicpc.net/problem/7568
"""

n = int(input())

list = []
for i in range(n):
    list.append([])

for i in range(n):
    w, h = map(int,(input().split()))
    list[i].append(w)
    list[i].append(h)


for i in list:
    rank = 1
    for j in list:
        if i[0] < j[0] and i[1] < j[1]:
                rank += 1
    print(rank, end = " ")