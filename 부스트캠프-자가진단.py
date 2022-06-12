"""
자연수가 들어있는 배열 arr가 매개변수로 주어집니다. 
배열 arr안의 숫자들 중에서 앞에 있는 숫자들부터 
뒤에 중복되어 나타나는 숫자들 중복 횟수를 계산해서 배열로 return 하도록 
solution 함수를 완성해주세요. 
만약 중복되는 숫자가 없다면 배열에 -1을 채워서 return 하세요.
"""

from collections import Counter


def solution(arr):
    arr = sorted(Counter(arr).items())
    answer = []
    for i in arr:
        if i[1] > 1:
            answer.append(i[1])

    if answer:
        return answer
    else:
        return [-1]

print(solution(   [3, 5, 7, 9, 1]   ))