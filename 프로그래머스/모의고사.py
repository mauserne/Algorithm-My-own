def solution(answers):
    answer = []
    a = [1, 2, 3, 4, 5]
    b = [2, 1, 2, 3, 2, 4, 2, 5]
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    hit = [0,0,0]
    
    for i in range(len(answers)):
        if answers[i] == a[i%5]:
            hit[0] += 1
        if answers[i] == b[i%8]:
            hit[1] += 1
        if answers[i] == c[i%10]:
            hit[2] += 1
    
    hitmax = max(hit)
    for i in range(3):
        if hit[i] == hitmax:
            answer.append(i+1)
    
    return answer

"""
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.3MB)
테스트 2 〉	통과 (0.01ms, 10.2MB)
테스트 3 〉	통과 (0.01ms, 10.2MB)
테스트 4 〉	통과 (0.01ms, 10.2MB)
테스트 5 〉	통과 (0.02ms, 10.2MB)
테스트 6 〉	통과 (0.03ms, 10.2MB)
테스트 7 〉	통과 (1.20ms, 10.2MB)
테스트 8 〉	통과 (0.40ms, 10.2MB)
테스트 9 〉	통과 (2.23ms, 10.3MB)
테스트 10 〉	통과 (1.02ms, 10.3MB)
테스트 11 〉	통과 (2.31ms, 10.3MB)
테스트 12 〉	통과 (2.08ms, 10.2MB)
테스트 13 〉	통과 (0.15ms, 10.4MB)
테스트 14 〉	통과 (2.33ms, 10.2MB)

채점 결과
정확성: 100.0
합계: 100.0 / 100.0
"""

### 다른 풀이에서 쓰인 enumerate함수 사용

def solution(answers):
    answer = []
    a = [1, 2, 3, 4, 5]
    b = [2, 1, 2, 3, 2, 4, 2, 5]
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    hit = [0,0,0]
    
    for i, val in enumerate(answers):
        if val == a[i%5]:
            hit[0] += 1
        if val == b[i%8]:
            hit[1] += 1
        if val == c[i%10]:
            hit[2] += 1
    
    hitmax = max(hit)
    for i in range(3):
        if hit[i] == hitmax:
            answer.append(i+1)
    
    return answer