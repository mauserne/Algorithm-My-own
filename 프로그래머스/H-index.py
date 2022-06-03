#https://programmers.co.kr/learn/courses/30/lessons/42747


def solution(citations):
    answer = 0

    for i in range(1,len(citations)+1):
        cnt = 0
        for j in citations:
            if j >= i:
                cnt += 1
                if cnt == i:
                    break
        if answer >= cnt:
            return answer
        answer = cnt

    return answer

def solution(citations):
    citations = sorted(citations)
    l = len(citations)
    for i in range(l):
        print(i,citations[i],'>=',l-i)
        if citations[i] >= l-i:
            return l-i
    return 0

print('출력',solution([3,3,6,7,9,9]))



"""
정확성  테스트
테스트 1 〉	통과 (5.83ms, 10.2MB)
테스트 2 〉	통과 (14.24ms, 10.1MB)
테스트 3 〉	통과 (13.36ms, 10.3MB)
테스트 4 〉	통과 (9.29ms, 10.3MB)
테스트 5 〉	통과 (15.29ms, 10.1MB)
테스트 6 〉	통과 (21.00ms, 10.3MB)
테스트 7 〉	통과 (5.44ms, 10.3MB)
테스트 8 〉	통과 (0.13ms, 10MB)
테스트 9 〉	통과 (0.36ms, 10MB)
테스트 10 〉	통과 (4.54ms, 10.3MB)
테스트 11 〉	통과 (35.17ms, 10.4MB)
테스트 12 〉	통과 (0.88ms, 10.2MB)
테스트 13 〉	통과 (20.33ms, 10.2MB)
테스트 14 〉	통과 (17.13ms, 10.3MB)
테스트 15 〉	통과 (20.72ms, 10.2MB)
테스트 16 〉	통과 (0.00ms, 9.94MB)
"""