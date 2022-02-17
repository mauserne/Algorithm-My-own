"""
스택 수열
https://www.acmicpc.net/problem/1874
문제 이해 못해서 구글링함
"""

import sys

n = int(input())

output = []

stack=[]
count = 0
for _ in range(n):
    number = int(sys.stdin.readline().rstrip())
    
    while True:
        if number > count :
            count += 1
            stack.append(count)
            output.append('+')
        elif stack[-1] == number : 
            del stack[-1]
            output.append('-')
            break
        else:
            print('NO')
            sys.exit()


print('\n'.join(output))


"""
스택 자료구조에 대한 이해가 더 필요할듯
"""