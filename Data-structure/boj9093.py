"""
단어 뒤집기
https://www.acmicpc.net/problem/9093
time spent : 15min
"""

n = int(input())

for _ in range(n):
    sentence = input().split()

    contro = []
    for i in sentence:
        contro.append(i[::-1])
    print(' '.join(contro))