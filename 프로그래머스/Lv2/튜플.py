#https://programmers.co.kr/learn/courses/30/lessons/64065

def solution(s):
    answer = []
    s = s[:-2].replace('{','').replace(',',' ').split('}')
    
    s = [i.split() for i in s]
    
    s.sort(key=lambda x:len(x))

    for tup in s:
        for i in answer:
            tup.remove(i)
        answer.append(tup[0])
    
    answer = [int(i) for i in answer]
    
    return answer

"""
테스트 1 〉	통과 (0.03ms, 10.4MB)
테스트 2 〉	통과 (0.02ms, 10.5MB)
테스트 3 〉	통과 (0.02ms, 10.3MB)
테스트 4 〉	통과 (0.04ms, 10.4MB)
테스트 5 〉	통과 (0.20ms, 10.5MB)
테스트 6 〉	통과 (0.53ms, 10.5MB)
테스트 7 〉	통과 (13.22ms, 11.6MB)
테스트 8 〉	통과 (64.46ms, 14.7MB)
테스트 9 〉	통과 (22.99ms, 12.3MB)
테스트 10 〉	통과 (75.88ms, 15.1MB)
테스트 11 〉	통과 (109.99ms, 16.7MB)
테스트 12 〉	통과 (172.37ms, 19.8MB)
테스트 13 〉	통과 (182.52ms, 19.8MB)
테스트 14 〉	통과 (184.40ms, 20MB)
테스트 15 〉	통과 (0.02ms, 10.4MB)
"""

# 리팩토링 !! 

from collections import Counter

def solution(s):
    answer = []
    s = s[:-2].replace('{','').replace(',',' ').split('}')
    
    s = [i.split() for i in s]
    
    s.sort(key=lambda x:len(x))

    for tup in s:
        counter1 = Counter(tup) - Counter(answer)
        answer.append(list(counter1.elements())[0])
    
    answer = [int(i) for i in answer]
    
    return answer