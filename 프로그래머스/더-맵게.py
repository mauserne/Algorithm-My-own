#https://programmers.co.kr/learn/courses/30/lessons/42626
import heapq

def solution(scoville, K):
    answer = 0
    
    if all(0==i for i in scoville):
        return -1

    hq = []
    for i in scoville:
        heapq.heappush(hq,i)

    while any(K>num for num in hq):

        least1 = heapq.heappop(hq)
        if hq:
            least2 = heapq.heappop(hq)
        else:
            return -1
        
        heapq.heappush(hq, least1 + (least2 * 2))
        answer += 1

    return answer

#리팩토링
def solution1(scoville, K):
    answer = 0
    
    heapq.heapify(scoville)

    while any(K>num for num in scoville):

        least1 = heapq.heappop(scoville)
        if scoville:
            least2 = heapq.heappop(scoville)
        else:
            return -1
        
        heapq.heappush(scoville, least1 + (least2 * 2))
        answer += 1

    return answer

print('출력',solution1([1, 2, 3, 9, 10, 12],7))

"""
정확성  테스트
테스트 1 〉	통과 (0.05ms, 10.1MB)
테스트 2 〉	통과 (0.05ms, 10.3MB)
테스트 3 〉	통과 (0.04ms, 10.1MB)
테스트 4 〉	통과 (0.04ms, 10.1MB)
테스트 5 〉	통과 (0.01ms, 10.1MB)
테스트 6 〉	통과 (0.61ms, 10.2MB)
테스트 7 〉	통과 (0.73ms, 10.3MB)
테스트 8 〉	통과 (0.08ms, 10.1MB)
테스트 9 〉	통과 (0.07ms, 10.2MB)
테스트 10 〉	통과 (0.46ms, 10.1MB)
테스트 11 〉	통과 (0.36ms, 10.2MB)
테스트 12 〉	통과 (0.95ms, 10.2MB)
테스트 13 〉	통과 (0.54ms, 10.2MB)
테스트 14 〉	통과 (0.02ms, 10.2MB)
테스트 15 〉	통과 (0.70ms, 10.2MB)
테스트 16 〉	통과 (0.01ms, 10.1MB)

효율성  테스트
테스트 1 〉	통과 (210.66ms, 18.6MB)
테스트 2 〉	통과 (481.68ms, 27MB)
테스트 3 〉	통과 (2106.50ms, 63.9MB)
테스트 4 〉	통과 (178.08ms, 17MB)
테스트 5 〉	통과 (1994.34ms, 71.3MB)

채점 결과
정확성: 76.2
효율성: 23.8
합계: 100.0 / 100.0
"""