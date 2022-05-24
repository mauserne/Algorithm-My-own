#https://programmers.co.kr/learn/courses/30/lessons/68644
"""
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.01ms, 10.2MB)
테스트 3 〉	통과 (0.01ms, 10.1MB)
테스트 4 〉	통과 (0.01ms, 10.2MB)
테스트 5 〉	통과 (0.01ms, 10.1MB)
테스트 6 〉	통과 (0.03ms, 10.1MB)
테스트 7 〉	통과 (0.39ms, 10.1MB)
테스트 8 〉	통과 (0.41ms, 10MB)
테스트 9 〉	통과 (0.42ms, 10.1MB)

채점 결과
정확성: 100.0
합계: 100.0 / 100.0
"""
def solution(numbers):
    sums = set()

    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
           sums.add(numbers[i]+numbers[j])

    return sorted(sums)

print(solution([5,0,2,7]))