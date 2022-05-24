#https://programmers.co.kr/learn/courses/30/lessons/42586
"""
정확성  테스트

테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.34ms, 10.1MB)
테스트 3 〉	통과 (0.46ms, 10.1MB)
테스트 4 〉	통과 (0.18ms, 10.1MB)
테스트 5 〉	통과 (0.02ms, 10.2MB)
테스트 6 〉	통과 (0.04ms, 10.1MB)
테스트 7 〉	통과 (0.86ms, 10.3MB)
테스트 8 〉	통과 (0.06ms, 10.2MB)
테스트 9 〉	통과 (0.29ms, 10.1MB)
테스트 10 〉	통과 (0.33ms, 10.1MB)
테스트 11 〉	통과 (0.01ms, 10.2MB)

채점 결과
정확성: 100.0
합계: 100.0 / 100.0
"""
from collections import deque

def solution(progresses, speeds):
    answer = []
    prog = deque(progresses)
    spd = deque(speeds)

    while prog:
        for i in range(len(prog)):
            prog[i] += spd[i]

        tmp = 0
        try:
            while prog[0] >= 100:
                tmp += 1
                prog.popleft()
                spd.popleft()
        except:
            pass

        if tmp > 0:
            answer.append(tmp)

    return answer

print(solution([1, 1, 1,1],[5, 10, 10,1]))