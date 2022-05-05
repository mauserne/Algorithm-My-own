"""
신고 결과 받기
https://programmers.co.kr/learn/courses/30/lessons/92334
"""


def solution(id_list, report, k):
    answer = [0]*len(id_list)
    dic = dict()
    for user in id_list:
        dic[user] = [set(),0]
    for i in report:
        user, reported = i.split()
        dic[reported][0].add(user)
    for key,value in dic.items():
        if len(value[0]) >= k:
            for i in value[0]:
                dic[i][1] += 1
    for idx, user in enumerate(id_list):
        answer[idx] = dic[user][1]

    return answer



print(solution(["muzi", "frodo", "apeach", "neo"],["muzi frodo","muzi frodo","muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"],2))
