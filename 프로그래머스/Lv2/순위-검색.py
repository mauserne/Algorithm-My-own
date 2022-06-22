def solution(info, query):
    answer = []
    info = [i.split() for i in info]
    # 점수 정수화 필요
    query = [i.replace('and','').split() for i in query]
    
    for conditions in query:
        hired = []
        for applicant,spec in enumerate(info):
            if int(conditions[4]) <= int(spec[4]):
                for i in range(4):
                    if conditions[i] == '-':    # 질문 넘어감
                        continue
                    if conditions[i] != spec[i]: # 질문 불충족시
                        break
                else:
                    hired.append(applicant)
        answer.append(len(hired))

    return answer

"""
테스트 1 〉	통과 (0.12ms, 10.5MB)
테스트 2 〉	통과 (0.12ms, 10.4MB)
테스트 3 〉	통과 (1.03ms, 10.4MB)
테스트 4 〉	통과 (10.44ms, 10.6MB)
테스트 5 〉	통과 (44.29ms, 10.6MB)
테스트 6 〉	통과 (109.75ms, 10.7MB)
테스트 7 〉	통과 (47.77ms, 11.2MB)
테스트 8 〉	통과 (232.28ms, 12.9MB)
테스트 9 〉	통과 (216.64ms, 13.2MB)
테스트 10 〉	통과 (243.65ms, 13.2MB)
테스트 11 〉	통과 (47.17ms, 10.7MB)
테스트 12 〉	통과 (116.53ms, 10.7MB)
테스트 13 〉	통과 (50.02ms, 11.1MB)
테스트 14 〉	통과 (222.99ms, 11.7MB)
테스트 15 〉	통과 (233.31ms, 11.7MB)
테스트 16 〉	통과 (44.88ms, 10.7MB)
테스트 17 〉	통과 (111.77ms, 10.6MB)
테스트 18 〉	통과 (221.56ms, 11.8MB)

효율성  테스트
테스트 1 〉	실패 (시간 초과)
테스트 2 〉	실패 (시간 초과)
테스트 3 〉	실패 (시간 초과)
테스트 4 〉	실패 (시간 초과)
"""

def solution(info, query):
    answer = []
    info = [i.split() for i in info]

    query = [i.replace('and','').split() for i in query]
    
    for conditions in query:
        hired = []
        for applicant,spec in enumerate(info):
            for i in range(4):
                if conditions[i] == '-':    # 질문 넘어감
                    continue
                if conditions[i] != spec[i]: # 질문 불충족시
                    break
            else:
                if int(conditions[4]) <= int(spec[4]):
                    hired.append(applicant)
        answer.append(len(hired))

    return answer

"""
정확성  테스트
테스트 1 〉	통과 (0.13ms, 10.4MB)
테스트 2 〉	통과 (0.11ms, 10.4MB)
테스트 3 〉	통과 (0.84ms, 10.5MB)
테스트 4 〉	통과 (8.49ms, 10.5MB)
테스트 5 〉	통과 (37.56ms, 10.7MB)
테스트 6 〉	통과 (99.42ms, 10.8MB)
테스트 7 〉	통과 (40.64ms, 11.1MB)
테스트 8 〉	통과 (189.43ms, 12.8MB)
테스트 9 〉	통과 (192.07ms, 13.2MB)
테스트 10 〉	통과 (195.65ms, 13.2MB)
테스트 11 〉	통과 (39.89ms, 10.7MB)
테스트 12 〉	통과 (99.33ms, 10.7MB)
테스트 13 〉	통과 (39.52ms, 11MB)
테스트 14 〉	통과 (199.21ms, 11.7MB)
테스트 15 〉	통과 (189.04ms, 11.8MB)
테스트 16 〉	통과 (37.27ms, 10.6MB)
테스트 17 〉	통과 (107.79ms, 10.5MB)
테스트 18 〉	통과 (201.10ms, 11.8MB)

효율성  테스트
테스트 1 〉	실패 (시간 초과)
테스트 2 〉	실패 (시간 초과)
테스트 3 〉	실패 (시간 초과)
테스트 4 〉	실패 (시간 초과)
"""



[
    "java backend junior pizza 150",
    "python frontend senior chicken 210",
    "python frontend senior chicken 150",
    "cpp backend senior pizza 260",
    "java backend junior chicken 80",
    "python backend senior chicken 50"
    ]

[
    "java and backend and junior and pizza 100",
    "python and frontend and senior and chicken 200",
    "cpp and - and senior and pizza 250",
    "- and backend and senior and - 150",
    "- and - and - and chicken 100",
    "- and - and - and - 150"
    ]



from itertools import combinations
from collections import defaultdict
from bisect import bisect_left

def solution(information, queries):
    answer = []
    dic = defaultdict(list)
    
    for info in information:
        info = info.split()
        condition = info[:-1]  
        score = int(info[-1])

        for i in range(5):
            case = list(combinations([0,1,2,3], i))
            for c in case:
                tmp = condition[:]
                for idx in c:
                    tmp[idx] = "-"
                key = ''.join(tmp)
                print(key)
                dic[key].append(score) 

    for value in dic.values():
        value.sort()   

    for query in queries:
        query = query.replace('and ', '').split()
        target_key = ''.join(query[:-1])
        target_score = int(query[-1])
        count = 0
        if target_key in dic:
            target_list = dic[target_key]
            idx = bisect_left(target_list, target_score)
            count = len(target_list) - idx
        answer.append(count)   

    return answer

print('출력 :',solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"],["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))