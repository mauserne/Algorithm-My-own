#https://programmers.co.kr/learn/courses/30/lessons/42842

def solution(brown, yellow):
    b = brown - 4
    height = 1
    
    while True:
        width = (b - (height * 2))//2
        if yellow == width * height:
            return [width+2, height+2]
        height += 1

print('출력',solution(8,1))

"""
테스트 1 〉	통과 (0.00ms, 10MB)
테스트 2 〉	통과 (0.00ms, 10MB)
테스트 3 〉	통과 (0.12ms, 10.1MB)
테스트 4 〉	통과 (0.00ms, 10.3MB)
테스트 5 〉	통과 (0.01ms, 10.2MB)
테스트 6 〉	통과 (0.04ms, 10.2MB)
테스트 7 〉	통과 (0.09ms, 10.1MB)
테스트 8 〉	통과 (0.12ms, 10MB)
테스트 9 〉	통과 (0.11ms, 10.2MB)
테스트 10 〉	통과 (0.16ms, 10.1MB)
테스트 11 〉	통과 (0.00ms, 10MB)
테스트 12 〉	통과 (0.00ms, 10MB)
테스트 13 〉	통과 (0.00ms, 10.1MB)
"""