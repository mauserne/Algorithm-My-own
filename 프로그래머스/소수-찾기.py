#https://programmers.co.kr/learn/courses/30/lessons/42839

import math
from itertools import permutations

def solution(numbers):
    answer = 0

    arr = [True]*10000000
    arr[0] = False
    arr[1] = False

    # 소수 9,999,999 까지 찾기
    for i in range(2, int(math.sqrt(10000000))):
        if arr[i]:
            j = 2
            while i*j <= 9999999:
                arr[i*j] = False
                j+=1

    nums = set()
    for i in range(1,len(numbers)+1):
        for j in list(permutations(numbers,i)):
            nums.add(int(''.join(j)))

    for i in nums:
        if arr[i]:
            answer += 1

    return answer

#print('출력',solution("011"))

"""
정확성  테스트
테스트 1 〉	통과 (3277.15ms, 86.1MB)
테스트 2 〉	통과 (3289.55ms, 86.8MB)
테스트 3 〉	통과 (3299.24ms, 86MB)
테스트 4 〉	통과 (3218.18ms, 86.5MB)
테스트 5 〉	통과 (3305.63ms, 87.2MB)
테스트 6 〉	통과 (3265.54ms, 85.9MB)
테스트 7 〉	통과 (3452.67ms, 85.9MB)
테스트 8 〉	통과 (3375.38ms, 87.4MB)
테스트 9 〉	통과 (3442.21ms, 85.9MB)
테스트 10 〉	통과 (3240.26ms, 86.5MB)
테스트 11 〉	통과 (3266.21ms, 86.4MB)
테스트 12 〉	통과 (3384.11ms, 86MB)

채점 결과
정확성: 100.0
합계: 100.0 / 100.0
"""

def solution1(numbers):
    answer = 0

    nums = set()
    for i in range(1,len(numbers)+1):
        for j in list(permutations(numbers,i)):
            nums.add(int(''.join(j)))

    numsmax = max(nums)

    arr = [True]*(numsmax+1)
    arr[0] = False
    arr[1] = False

    # 소수 9,999,999 까지 찾기
    for i in range(2, int(math.sqrt(numsmax)+1 )):
        if arr[i]:
            j = 2
            while i*j <= numsmax:
                arr[i*j] = False
                j+=1

    for i in nums:
        if arr[i]:
            answer += 1

    return answer

print('출력',solution1("011"))

"""
정확성  테스트
테스트 1 〉	통과 (0.60ms, 10.4MB)
테스트 2 〉	통과 (174.19ms, 15.4MB)
테스트 3 〉	통과 (0.03ms, 10.4MB)
테스트 4 〉	통과 (68.58ms, 12.6MB)
테스트 5 〉	통과 (1014.67ms, 36.6MB)
테스트 6 〉	통과 (0.03ms, 10.3MB)
테스트 7 〉	통과 (0.58ms, 10.5MB)
테스트 8 〉	통과 (1797.43ms, 53.2MB)
테스트 9 〉	통과 (0.07ms, 10.4MB)
테스트 10 〉	통과 (228.02ms, 18.1MB)
테스트 11 〉	통과 (27.46ms, 11.1MB)
테스트 12 〉	통과 (10.65ms, 10.5MB)

채점 결과
정확성: 100.0
합계: 100.0 / 100.0
"""