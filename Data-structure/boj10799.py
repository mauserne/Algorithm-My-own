"""
쇠막대기
https://www.acmicpc.net/problem/10799
time spent : 39 min
"""

# ()는 레이저
#(는 개행 )는 폐행

n = input()


output = 0
#레이저 맞을떄마다 파이프 조각 1증가
pipe = []
for i in range(len(n)):
    if n[i] == '(' and n[i+1] == ')':
        #레이저
        #pipe 모든 파이프에 1더함
        output += len(pipe)
    elif n[i] == '(':
        #개행
        pipe.append(1)
    elif n[i] == ')' and not n[i-1] == '(':
        #마지막에 열린 행 닫힘
        output += pipe.pop()


print(output)