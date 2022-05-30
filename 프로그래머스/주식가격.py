#https://programmers.co.kr/learn/courses/30/lessons/42584

from collections import deque

def solution(prices):
    answer = []
    q = deque(prices)

    while q:
        count = 0
        now = q.popleft()
        
        for i in q:
            count += 1
            if i < now:
                break

        answer.append(count)

    return answer

print('출력',solution([1,2,3,2,3]))


"""
정확성  테스트
테스트 1 〉	통과 (0.00ms, 9.91MB)
테스트 2 〉	통과 (0.03ms, 10.1MB)
테스트 3 〉	통과 (0.27ms, 10MB)
테스트 4 〉	통과 (0.29ms, 10MB)
테스트 5 〉	통과 (0.59ms, 10.2MB)
테스트 6 〉	통과 (0.03ms, 9.81MB)
테스트 7 〉	통과 (0.31ms, 10MB)
테스트 8 〉	통과 (0.20ms, 10.2MB)
테스트 9 〉	통과 (0.02ms, 10.1MB)
테스트 10 〉	통과 (0.36ms, 9.98MB)

효율성  테스트
테스트 1 〉	통과 (59.04ms, 18.8MB)
테스트 2 〉	통과 (45.99ms, 17.6MB)
테스트 3 〉	통과 (74.19ms, 19.5MB)
테스트 4 〉	통과 (52.91ms, 18.2MB)
테스트 5 〉	통과 (35.24ms, 16.8MB)
"""