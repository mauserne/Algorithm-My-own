import sys

input = sys.stdin.readline

T = int(input())

for i in range(1, T+1):
    a,b = map(int, input().split())
    print('Case #{idx}: {num1} + {num2} = {ans}'.format(num1 = a, num2 = b, idx = i ,ans = a+b))