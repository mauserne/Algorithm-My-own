"""
괄호
https://www.acmicpc.net/problem/9012
time spent : 15min
"""

n = int(input())
for _ in range(n):
    bracket = input()
    while True:
        if '()' not in bracket and len(bracket)==0:
            print('YES')
            break 
        elif '()' not in bracket and len(bracket) > 0:
            print('NO')
            break
        bracket = bracket.replace('()','')