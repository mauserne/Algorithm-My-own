#https://programmers.co.kr/learn/courses/30/lessons/92335

def sosu(x):
    if x <= 1:
        return False
    for i in range(2,int(x**0.5)+1):
        if x%i == 0:
            return False
    return True

def solution(n, k):
    answer = 0
    kbase = ''
    while n:
        kbase += str(n%k)
        n //= k
    kbase = kbase[::-1].split('0')
    kbase = [int(i) for i in kbase if i != '']
    
    print(type(kbase[0]))
    # 소수찾기 알고리즘
    for i in kbase:
        if sosu(i):
            answer += 1
    
    return answer

print(solution(797161,3))