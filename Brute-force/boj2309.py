"""
일곱 난쟁이
https://www.acmicpc.net/problem/2309
"""


nanjang = []
for _ in range(9):
    nanjang.append(int(input()))

nansum = sum(nanjang)

detect = False

for i in range(9):
    if detect:
        break
    for j in range(i):
        if nansum - nanjang[i] - nanjang[j] == 100:
            nanjang[i] = 0
            nanjang[j] = 0
            detect = True

nanjang.sort()

for i in nanjang:
    if i == 0 :
        continue
    print(i)
