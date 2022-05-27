#https://programmers.co.kr/learn/courses/30/lessons/42583

from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 1
    q = deque(truck_weights)
    onboard = deque([0 for _ in range(bridge_length)])
    
    onweight = q.popleft()
    onboard.append(onweight)
    onboard.popleft()
    
    while onweight:
        if onboard.popleft():
            onweight = sum(onboard)
        if q:
            if onweight + q[0] <= weight:
                onboard.append(q.popleft())
                onweight = sum(onboard)
            else:
                onboard.append(0)
        answer += 1

    return answer

print('출력',solution(2,10,[7,4,5,6]))

"""
정확성  테스트
테스트 1 〉	통과 (0.40ms, 10.3MB)
테스트 2 〉	통과 (6.38ms, 10.4MB)
테스트 3 〉	통과 (0.02ms, 10.3MB)
테스트 4 〉	통과 (11.39ms, 10.3MB)
테스트 5 〉	통과 (88.36ms, 10.4MB)
테스트 6 〉	통과 (31.94ms, 10.2MB)
테스트 7 〉	통과 (0.32ms, 10.2MB)
테스트 8 〉	통과 (0.08ms, 10.3MB)
테스트 9 〉	통과 (1.89ms, 10.2MB)
테스트 10 〉	통과 (0.09ms, 10.2MB)
테스트 11 〉	통과 (0.01ms, 10.2MB)
테스트 12 〉	통과 (0.16ms, 10.2MB)
테스트 13 〉	통과 (0.55ms, 10.2MB)
테스트 14 〉	통과 (0.02ms, 10.2MB)

채점 결과
정확성: 100.0
합계: 100.0 / 100.0
"""

# 처음 코드(시간초과)

def solution(bridge_length, weight, truck_weights):
    answer = 0
    q = deque(truck_weights)
    onboard = deque([0 for _ in range(bridge_length)])

    while q or sum(onboard) != 0:	# 다리 건너기를 기다리는 트럭이 없거나, 다리에 올라간 트럭이 없으면 종료하는 while문
        onboard.popleft()
        if q:
            if sum(onboard) + q[0] <= weight:
                onboard.append(q.popleft())
            else:
                onboard.append(0)
        else:
            onboard.append(0)
        answer += 1

    return answer

"""
정확성  테스트
테스트 1 〉	통과 (24.41ms, 10.2MB)
테스트 2 〉	통과 (1950.99ms, 10.3MB)
테스트 3 〉	통과 (0.04ms, 10.2MB)
테스트 4 〉	통과 (372.07ms, 10.4MB)
테스트 5 〉	실패 (시간 초과)
테스트 6 〉	통과 (1803.24ms, 10.4MB)
테스트 7 〉	통과 (8.24ms, 10.2MB)
테스트 8 〉	통과 (0.24ms, 10.1MB)
테스트 9 〉	통과 (5.07ms, 10.2MB)
테스트 10 〉	통과 (0.50ms, 10.3MB)
테스트 11 〉	통과 (0.01ms, 10.3MB)
테스트 12 〉	통과 (0.25ms, 10.3MB)
테스트 13 〉	통과 (1.87ms, 10.2MB)
테스트 14 〉	통과 (0.09ms, 10.1MB)

채점 결과
정확성: 92.9
합계: 92.9 / 100.0
"""

# 성공 코드 리팩토링

def solution(bridge_length, weight, truck_weights):
    answer = 1
    onboard = deque([0]*bridge_length)	# << 조금 더 짧게 표현
    
    # q = deque(truck_weights) 없앰
    onweight = truck_weights.pop(0)
    onboard.append(onweight)
    onboard.popleft()
    
    while onweight:
        if onboard.popleft():
            onweight = sum(onboard)
        if truck_weights:
            if onweight + truck_weights[0] <= weight:
                onboard.append(truck_weights.pop(0))
                onweight = sum(onboard)
            else:
                onboard.append(0)
        answer += 1

    return answer