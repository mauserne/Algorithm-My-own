def solution(lottos, win_nums):
    hit = 0
    empty = 0
    
    for i in lottos:
        if i == 0:
            empty += 1
            continue
        if i in win_nums:
            hit += 1

    best = empty+hit
    worst = hit

    def rank(x):
        if x < 2:
            x = 6
        else:
            x = 7 - x
        return x
        
    answer  = [rank(best),rank(worst)]

    return answer

print('출력',solution([44, 1, 0, 0, 31, 25]	,[31, 10, 45, 1, 6, 19]	))