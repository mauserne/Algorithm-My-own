"""
팰린드롬 만들기
https://www.acmicpc.net/problem/1213
"""

# https://my-coding-notes.tistory.com/530

import sys

input = sys.stdin.readline


string = input().rstrip()

dic = dict()
for i in string:
    if not i in dic:
        dic[i] = 1
    else:
        dic[i] += 1

center = ''
for key, value in dic.items():
    if value % 2 == 1: # 문자 갯수가 홀수이면
        if len(center) == 0:
            center = key
        else:
            print("I'm Sorry Hansoo")
            break
else: # for-else문
    part = ''
    for key, value in sorted(dic.items()):
        part += key*(value//2)
    
    print(part + center + part[::-1])