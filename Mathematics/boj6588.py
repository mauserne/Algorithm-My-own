"""
골드바흐의 추측
https://www.acmicpc.net/problem/6588
"""
#https://velog.io/@dding_ji/%EB%B0%B1%EC%A4%80-6588.-%EA%B3%A8%EB%93%9C%EB%B0%94%ED%9D%90%EC%9D%98-%EC%B6%94%EC%B8%A1-Python-%EC%97%90%EB%9D%BC%ED%86%A0%EC%8A%A4%ED%85%8C%EB%84%A4%EC%8A%A4%EC%9D%98-%EC%B2%B4

import sys

array = [True for i in range(1000001)]

for i in range(2,1001):
    if array[i]:
        for j in range(i + i, 1000001, i):
            array[j] = False

while True:
    n = int(sys.stdin.readline().rstrip())

    if n == 0:
        break

    for i in range(3, len(array)):
        if array[i] and array[n-i]:
            print(n,'=',i,'+',n-i)
            break