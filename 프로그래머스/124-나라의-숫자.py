#https://programmers.co.kr/learn/courses/30/lessons/12899

def solution(n):
    answer = ''
    while n:
        if n % 3 == 0:
            n = n // 3 - 1
            answer += '4'
        else:
            answer += str(n%3)
            n //= 3
    return answer[::-1]