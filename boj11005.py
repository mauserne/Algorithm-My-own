# https://www.acmicpc.net/problem/11005

n, b = map(int,input().split())


answer = ''
while n:
    if n % b == 0:
        n = n // b - 1
        answer += str(b-1)+' '
    else:
        answer += str(n%b)
        n //= b
print(answer[::-1])