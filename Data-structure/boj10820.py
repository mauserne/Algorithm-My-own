"""
문자열 분석
https://www.acmicpc.net/problem/10820
"""

import sys


while True:
    output = [0]* 4
    line = sys.stdin.readline().rstrip('\n')
    if not line:
        break

    for i in line :
        if 'a' <= i <= 'z':
            output[0] += 1
        if 'A' <= i <= 'Z':
            output[1] += 1
        if '0' <= i <= '9':
            output[2] += 1
        if i == ' ':
            output[3] += 1

    print(' '.join(map(str,output)))
