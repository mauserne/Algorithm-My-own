"""
https://programmers.co.kr/learn/courses/30/lessons/42883
테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.01ms, 10.2MB)
테스트 3 〉	통과 (0.02ms, 10MB)
테스트 4 〉	통과 (0.09ms, 10.1MB)
테스트 5 〉	통과 (0.15ms, 10.2MB)
테스트 6 〉	통과 (2.49ms, 10MB)
테스트 7 〉	통과 (7.01ms, 10.4MB)
테스트 8 〉	통과 (15.19ms, 10.5MB)
테스트 9 〉	통과 (31.73ms, 12.5MB)
테스트 10 〉	통과 (82.82ms, 12.9MB)
테스트 11 〉	통과 (0.00ms, 10.3MB)
테스트 12 〉	통과 (0.00ms, 10.1MB)
"""


maxnumb = 0
def solution(number, k):
    answer = ''
    partlen = len(number) - k
    headnumber = 0

    def dfs(i,now):
        global maxnumb

        now += number[i]
        print(now)
        if len(now) == partlen:
            maxnumb = max(int(now),maxnumb)
            return
        for idx in range(i+1, len(number)):
            dfs(idx, now)

    for i in range(len(number)):
        if int(number[i]) < headnumber:
            continue
        headnumber = int(number[i])
        print('h',headnumber)
        dfs(i,'')
    
    answer = str(maxnumb)
    return answer 


def sol1(number, k):
    stack = []
    for i in number:
        while stack and stack[-1] < i and k > 0:
            stack.pop()
            k -= 1
            # k는 숫자를 지울 수 있는 기회이다.
        stack.append(i)

    answer = ''.join(stack)
    if k > 0:
        answer = answer[:-k]
    return answer

print('출력',sol1(input(),int(input())))
