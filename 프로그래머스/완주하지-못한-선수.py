#https://programmers.co.kr/learn/courses/30/lessons/42576
"""
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.01ms, 10.2MB)
테스트 3 〉	통과 (0.19ms, 10.2MB)
테스트 4 〉	통과 (0.65ms, 10.3MB)
테스트 5 〉	통과 (0.60ms, 10.3MB)

효율성  테스트
테스트 1 〉	통과 (28.50ms, 21.7MB)
테스트 2 〉	통과 (40.36ms, 25.2MB)
테스트 3 〉	통과 (44.95ms, 27.6MB)
테스트 4 〉	통과 (61.26ms, 33.9MB)
테스트 5 〉	통과 (57.18ms, 33.8MB)

채점 결과
정확성: 50.0
효율성: 50.0
합계: 100.0 / 100.0
"""
# 제출 코드
def solution(participant, completion):
    partc = dict()
    for runner in participant:
        if not runner in partc:
            partc[runner] = 1
        else:
            partc[runner] += 1
    for runner in completion:
        partc[runner] -= 1
        if partc[runner] == 0:
            partc.pop(runner)

    return list(partc.keys())[0]

print(solution(["mislav", "stanko", "mislav", "ana"],["stanko", "ana", "mislav"]))

###
# 오답코드
def solution1(participant, completion):
    participant = set(participant)
    comp = set(completion)
    return list(participant - comp)[0]

print(solution1(["marina", "josipa", "nikola", "vinko", "filipa"],["josipa", "filipa", "marina", "nikola"]))

#####
### 다른 풀이
import collections

def solution3(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]

print(solution3(["mislav", "stanko", "mislav", "ana"],["stanko", "ana", "mislav"]))
