#https://programmers.co.kr/learn/courses/30/lessons/42746

from itertools import permutations

def solution(numbers):
    answer = 0

    snums = [str(i) for i in numbers]

    arr = list(permutations(snums, len(snums)))

    for i in arr:
        answer = max(answer, int(''.join(i)))

    return str(answer)

print('출력',solution([3, 30, 34, 5, 9]))


def solution(numbers):
    numbers = [str(i) for i in numbers]     # numbers 요소 문자열화
    numbers.sort(key=lambda x: x*3, reverse=True)   # 
    return str(int(''.join(numbers)))