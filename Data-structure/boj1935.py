"""
후위 표기식2
https://www.acmicpc.net/problem/1935
"""

n = int(input())
#숫자를 스택에 넣고 연산자 만나면 pop
formula = input()
stack = []

number = [] 
for _ in range(n):
    number.append(int(input()))

for i in formula:
    if 'A' <= i <= 'Z' :
        stack.append(number[ord(i)-ord('A')])
    else:
        tmp2 = stack.pop()
        tmp1 = stack.pop()

        if i == '*':
            stack.append(tmp1*tmp2)
        if i == '/':
            stack.append(tmp1/tmp2)
        if i == '+':
            stack.append(tmp1+tmp2)
        if i == '-':
            stack.append(tmp1-tmp2)

print('%.2f'%stack[0])