#https://programmers.co.kr/learn/courses/30/lessons/12977


from itertools import combinations

def sosu(parm):
    a = [True] * parm
    a[0],a[1] = False,False
    
    for i in range(2,int(parm**(1/2))+1):
        if a[i]:
            multp = 2
            while i*multp < parm:
                a[i * multp] = False
                multp += 1
    return a

def solution(nums):
    answer = 0
    arr = list(map(sum,combinations(nums,3)))
    sosuarr = sosu(max(arr)+1)

    for i in arr:
        if sosuarr[i]:
            answer += 1

    return answer


print('출력',solution([2,4,6]))

"""
정확성  테스트
테스트 1 〉	통과 (0.43ms, 10.3MB)
테스트 2 〉	통과 (0.55ms, 10.3MB)
테스트 3 〉	통과 (0.14ms, 10.3MB)
테스트 4 〉	통과 (0.11ms, 10MB)
테스트 5 〉	통과 (0.60ms, 10.2MB)
테스트 6 〉	통과 (1.43ms, 10.5MB)
테스트 7 〉	통과 (0.55ms, 10.2MB)
테스트 8 〉	통과 (2.58ms, 10.6MB)
테스트 9 〉	통과 (0.70ms, 10.3MB)
테스트 10 〉	통과 (2.49ms, 10.4MB)
테스트 11 〉	통과 (0.10ms, 10.3MB)
테스트 12 〉	통과 (0.05ms, 10.2MB)
테스트 13 〉	통과 (0.06ms, 10.3MB)
테스트 14 〉	통과 (0.05ms, 10.2MB)
테스트 15 〉	통과 (0.04ms, 10.2MB)
테스트 16 〉	통과 (4.00ms, 10.6MB)
테스트 17 〉	통과 (4.47ms, 10.7MB)
테스트 18 〉	통과 (1.84ms, 10.3MB)
테스트 19 〉	통과 (1.92ms, 10.4MB)
테스트 20 〉	통과 (4.59ms, 10.7MB)
테스트 21 〉	통과 (4.49ms, 10.8MB)
테스트 22 〉	통과 (2.20ms, 10.4MB)
테스트 23 〉	통과 (0.02ms, 10.2MB)
테스트 24 〉	통과 (4.06ms, 10.4MB)
테스트 25 〉	통과 (3.90ms, 10.5MB)
테스트 26 〉	통과 (0.01ms, 10.2MB)
"""