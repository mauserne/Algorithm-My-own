#https://programmers.co.kr/learn/courses/30/lessons/92342

from itertools import combinations

def solution(n, info):
    apeach = 0
    trials = []
    candidates = []

    info = info[::-1]
    for i in range(11):
        if info[i]:
            apeach += i

    for r in range(1,n+1):
        for c in combinations([i for i in range(1,11)],r):
            #print(u)
            #겹치는것만 빼야대
            tmp_apeach = apeach
            for i in c:
                if info[i]:
                    tmp_apeach -= i
            if sum(c) > tmp_apeach:
                trials.append(c)

    for trial in trials:
        rion = n
        #print(trial)
        for i in trial[::-1]:
            rion -= info[i] + 1
            if rion < 0:
                break
        else:
            candidates.append(trial)
    
    if not candidates:
        return [-1]

    answer = [0]*11
    for i in candidates[-1]:
        answer[i] += (info[i]+1)
    return answer[::-1]

print('출력',solution(5,[2,1,1,1,0,0,0,0,0,0,0]	))

from itertools import combinations

def solution(n, info):
    apeach = 0
    trials = []

    info = info[::-1]
    for i in range(11):
        if info[i]:
            apeach += i

    for r in range(1,n+1):
        for c in combinations([i for i in range(0,11)],r):
            #print(u)
            #겹치는것만 빼야대
            tmp_apeach = apeach
            for i in c:
                if info[i]:
                    tmp_apeach -= i
            if sum(c) > tmp_apeach:
                trials.append([c,sum(c)-tmp_apeach])

    candidate = []
    diff_max = -1
    leftarrow = -1
    for trial,diff in trials:
        rion = n
        for i in trial[::-1]:
            rion -= info[i] + 1
            if rion < 0:
                break
        else:
            if diff >= diff_max:
                diff_max = diff
                candidate = trial
                leftarrow = rion
                print(candidate)
    
    if not candidate:
        return [-1]
    
    answer = [0]*11

    for i in candidate:
        answer[i] += (info[i]+1)

    answer[0] = leftarrow
    return answer[::-1]





from itertools import combinations

def solution(n, info):
    apeach = 0
    trials = []

    info = info[::-1]
    for i in range(11):
        if info[i]:
            apeach += i

    for r in range(1,n+1):
        for c in combinations(range(1,11),r):
            tmp_apeach = apeach
            for i in c:
                if info[i]:
                    tmp_apeach -= i
            if sum(c) > tmp_apeach:
                trials.append([c,sum(c)-tmp_apeach])

    trials.sort(key= lambda x:(x[1],-x[0][0]), reverse=True)
        # 라이언이 어피치에게서 큰 점수차이로 승리하는 경우를 우선순위로, 낮은 점수의 과녁판을 많이 맞힌 경우를 다음 우선순위로 하여 오름차순으로 정렬

    for trial,diff in trials:
        rion = n
        for i in trial[::-1]:
            rion -= info[i] + 1
            if rion < 0:    # 라이언이 화살이 부족해서 패배하는 경우는 넘어감
                break  
        else:       # 라이언이 승리하는 경우에서 가장 점수차이가 크고, 낮은 점수의 과녁판을 많이 맞힌 경우을 발견
            answer = [0]*11
            for i in trial:
                answer[i] += (info[i]+1)
            answer[0] = rion

            return answer[::-1]     # 문제 조건에 맞게 뒤집어서 출력
    
    # 라이언이 승리할 수 없는 게임이면
    return [-1]
    

print('출력',solution(10,[0,0,0,0,0,0,0,0,3,4,3]		))


