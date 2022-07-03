from itertools import combinations

def solution(n, info):
    answer = []
    
    A = [x for x in info]
    B = [x + 1 for x in info]
    A_total = 0
    for i in range(len(A)):
        if A[i]:
            A_total += 10 - i

    max_diff = 0
    for win in range(1, 10):
        # 이긴 점수의 경우의 수
        win_lists = combinations(range(10), win)
        for win_list in win_lists:
            candidate = []
            A_score, B_score = A_total, 0
            arrow_count = 0 # 라이언이 쏜 화살의 개수
            for i in range(10):
                if i in win_list:
                    candidate.append(B[i])
                    B_score += 10 - i
                    arrow_count += B[i]
                    if A[i]:
                        A_score -= 10 - i
                else:
                    candidate.append(0)
            
            # 라이언이 이기고, 화살개수를 초과하지 않은 경우
            if B_score > A_score and arrow_count <= n:
                diff_score = B_score - A_score
                # 0점에 쏜 화살의 개수
                candidate.append(max(0, n - arrow_count))
                # 점수차이가 큰 경우 업데이트
                # 점수차이가 같은 경우, 낮은 점수를 많이 맞춘 것으로 업데이트
                if max_diff <= diff_score:
                    answer = candidate
                    max_diff = diff_score
                    print(answer)
    # 이기는 방법이 없을 경우
    if len(answer) == 0:
        answer = [-1]
    return answer


print('출력',solution(10, [0,0,0,0,0,0,0,0,3,4,3]	)		)