#https://programmers.co.kr/learn/courses/30/lessons/42577


# 참고 블로그 https://coding-grandpa.tistory.com/86

def solution(phone_book):
    for idx1, val in enumerate(phone_book):
        for idx2, num in enumerate(phone_book):
            if idx1 == idx2:
                break
            if val.startswith(num):
                return False
            if num.startswith(val):
                return False
    return True

"""
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.3MB)
테스트 2 〉	통과 (0.01ms, 10.2MB)
테스트 3 〉	통과 (0.01ms, 10.1MB)
테스트 4 〉	통과 (0.01ms, 10.1MB)
테스트 5 〉	통과 (0.01ms, 10.1MB)
테스트 6 〉	통과 (0.00ms, 10.1MB)
테스트 7 〉	통과 (0.00ms, 9.99MB)
테스트 8 〉	통과 (0.01ms, 10MB)
테스트 9 〉	통과 (0.00ms, 10.1MB)
테스트 10 〉	통과 (0.00ms, 10.1MB)
테스트 11 〉	통과 (0.01ms, 10.1MB)
테스트 12 〉	통과 (0.00ms, 10.2MB)
테스트 13 〉	통과 (0.00ms, 10.1MB)
테스트 14 〉	통과 (103.95ms, 10.2MB)
테스트 15 〉	통과 (187.32ms, 10.1MB)
테스트 16 〉	통과 (302.91ms, 10.3MB)
테스트 17 〉	통과 (431.91ms, 10.3MB)
테스트 18 〉	통과 (626.16ms, 10.2MB)
테스트 19 〉	통과 (606.47ms, 10.3MB)
테스트 20 〉	통과 (910.44ms, 10.4MB)
효율성  테스트
테스트 1 〉	통과 (0.02ms, 10.8MB)
테스트 2 〉	통과 (0.02ms, 10.8MB)
테스트 3 〉	실패 (시간 초과)
테스트 4 〉	실패 (시간 초과)
"""

## 나의 최종코드

def solution(phone_book):
    dic = set(phone_book)

    for i in dic:
        tmp = ''
        for j in i:
            tmp += j
            print(tmp,i)
            if tmp in dic and tmp != i:
                return False
    return True

print('출력',solution(["123","12"]	))

"""
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.1MB)
테스트 2 〉	통과 (0.01ms, 10.1MB)
테스트 3 〉	통과 (0.01ms, 10.1MB)
테스트 4 〉	통과 (0.01ms, 10.3MB)
테스트 5 〉	통과 (0.01ms, 10.2MB)
테스트 6 〉	통과 (0.01ms, 10.1MB)
테스트 7 〉	통과 (0.01ms, 10.2MB)
테스트 8 〉	통과 (0.01ms, 10.2MB)
테스트 9 〉	통과 (0.01ms, 10.3MB)
테스트 10 〉	통과 (0.01ms, 10.3MB)
테스트 11 〉	통과 (0.01ms, 10.2MB)
테스트 12 〉	통과 (0.01ms, 10.2MB)
테스트 13 〉	통과 (0.01ms, 10.2MB)
테스트 14 〉	통과 (2.04ms, 10.2MB)
테스트 15 〉	통과 (1.49ms, 10.4MB)
테스트 16 〉	통과 (5.76ms, 10.3MB)
테스트 17 〉	통과 (6.49ms, 10.3MB)
테스트 18 〉	통과 (6.52ms, 10.3MB)
테스트 19 〉	통과 (1.10ms, 10.3MB)
테스트 20 〉	통과 (4.41ms, 10.4MB)

효율성  테스트
테스트 1 〉	통과 (0.97ms, 11.4MB)
테스트 2 〉	통과 (1.08ms, 11.2MB)
테스트 3 〉	통과 (444.18ms, 41.4MB)
테스트 4 〉	통과 (33.22ms, 39.2MB)
"""