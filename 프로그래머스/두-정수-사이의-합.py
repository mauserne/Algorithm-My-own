#https://programmers.co.kr/learn/courses/30/lessons/12912

def solution(a, b):
    answer = a+b
    if a > b:
        for i in range(b+1,a):
            answer += i
    elif a < b:
        for i in range(a+1,b):
            answer += i
    else:
        answer = a
    return answer