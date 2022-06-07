import heapq
import math

def solution(jobs):
    answer, now, i = 0, 0, 0
    start = -1 
    heap = []
    
    while i < len(jobs):
        # 현재 시점에서 처리할 수 있는 작업을 heap에 저장
        for j in jobs:
            if start < j[0] <= now:
                heapq.heappush(heap, [j[1], j[0]])
                print(heap)
        
        if len(heap) > 0: # 처리할 작업이 있는 경우
            cur = heapq.heappop(heap)
            print(cur)
            start = now
            now += cur[0]
            answer += now - cur[1] # 작업 요청시간부터 종료시간까지의 시간 계산
            i +=1
        else: # 처리할 작업이 없는 경우 다음 시간을 넘어감
            now += 1
                
    return answer // len(jobs)

def solution(jobs):
    length = len(jobs)
    jobs.sort(key=lambda x:x[1])
    time = 0
    answer = 0

    while jobs:
        close = 0
        for i in range(len(jobs)):
            if jobs[i][0] <= time:
                answer += time - jobs[i][0] + jobs[i][1]
                time += jobs[i][1]
                jobs.pop(i)
                break
        else:
            tmp = min(jobs)
            answer += tmp[1]
            time = sum(tmp)
            jobs.remove(tmp)
    return answer//length
        

print('출력',solution([[0, 3], [1, 9], [2, 6], [1,6]]	))

"""
테스트 1 〉	통과 (0.38ms, 10.2MB)
테스트 2 〉	통과 (0.31ms, 10.3MB)
테스트 3 〉	통과 (0.31ms, 10.2MB)
테스트 4 〉	통과 (0.46ms, 10.2MB)
테스트 5 〉	통과 (0.32ms, 10.4MB)
테스트 6 〉	통과 (0.02ms, 10.4MB)
테스트 7 〉	통과 (0.41ms, 10.2MB)
테스트 8 〉	통과 (0.20ms, 10.3MB)
테스트 9 〉	통과 (0.08ms, 10.2MB)
테스트 10 〉	통과 (0.40ms, 10.2MB)
테스트 11 〉	통과 (0.01ms, 10.1MB)
테스트 12 〉	통과 (0.01ms, 10.1MB)
테스트 13 〉	통과 (0.01ms, 10.3MB)
테스트 14 〉	통과 (0.01ms, 10.2MB)
테스트 15 〉	통과 (0.01ms, 10.2MB)
테스트 16 〉	통과 (0.01ms, 10.1MB)
테스트 17 〉	통과 (0.01ms, 10.2MB)
테스트 18 〉	통과 (0.02ms, 10.2MB)
테스트 19 〉	통과 (0.01ms, 10.3MB)
테스트 20 〉	통과 (0.01ms, 10.4MB)
"""