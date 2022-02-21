"""
후위 표기식
https://www.acmicpc.net/problem/1918
"""

formula = input()

#괄호는 어케할거야

output = ''

stack = []
for i in formula:
    if 'A' <= i <='Z':
        output += i
    else:
        if i == '(':
            stack.append(i)
        elif i == '*' or i == '/':
            while stack and (stack[-1] == '*' or stack[-1] =='/'): 
                output += stack.pop() 
            stack.append(i)
        elif i == '+' or i == '-':
            while stack and stack[-1] != '(': 
                output += stack.pop() 
            stack.append(i)
        elif i == ')':
            while stack and stack[-1] != '(':
                output += stack.pop()
            stack.pop()

while stack:
    output += stack.pop()

print(output)