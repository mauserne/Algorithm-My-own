#https://programmers.co.kr/learn/courses/30/lessons/42885

def solution(people, limit):
    answer = 0

    people.sort()
    
    left, right = 0, len(people)-1
    
    while left <= right:
        if left == right:
            answer += 1
            break

        if people[left] + people[right] > limit:
            right -= 1
            answer += 1
        else:
            answer += 1
            left += 1
            right -= 1

    return answer

print('출력',solution([100,500,500,900,950]	,1000))


"""

정확성  테스트
테스트 1 〉	통과 (0.87ms, 10.2MB)
테스트 2 〉	통과 (0.81ms, 10.3MB)
테스트 3 〉	통과 (0.60ms, 10.1MB)
테스트 4 〉	통과 (0.69ms, 10.3MB)
테스트 5 〉	통과 (0.32ms, 10.3MB)
테스트 6 〉	통과 (0.20ms, 9.98MB)
테스트 7 〉	통과 (0.30ms, 10.2MB)
테스트 8 〉	통과 (0.03ms, 10.1MB)
테스트 9 〉	통과 (0.05ms, 10.2MB)
테스트 10 〉	통과 (0.91ms, 10.2MB)
테스트 11 〉	통과 (0.49ms, 10.1MB)
테스트 12 〉	통과 (0.79ms, 10.1MB)
테스트 13 〉	통과 (0.59ms, 10.2MB)
테스트 14 〉	통과 (1.39ms, 10.3MB)
테스트 15 〉	통과 (0.07ms, 10.2MB)

효율성  테스트
테스트 1 〉	통과 (9.29ms, 10.5MB)
테스트 2 〉	통과 (10.47ms, 10.6MB)
테스트 3 〉	통과 (8.97ms, 10.5MB)
테스트 4 〉	통과 (10.14ms, 10.4MB)
테스트 5 〉	통과 (9.30ms, 10.5MB)
"""