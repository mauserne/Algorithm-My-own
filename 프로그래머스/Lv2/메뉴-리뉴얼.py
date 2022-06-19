#https://programmers.co.kr/learn/courses/30/lessons/72411

from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    for i in course:
        print(i)
        freq = []
        for order in orders:
            for tmp in combinations(order, i):
                print(type(tmp),tmp)
                freq.append(''.join(sorted(tmp)))
        
        mostcnt = Counter(freq).most_common()
        answer += [menu for menu, cnt in mostcnt if cnt > 1 and cnt == mostcnt[0][1]]
    return sorted(answer)


print('출력', solution(   ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]  ,  [2,3,4]  ))