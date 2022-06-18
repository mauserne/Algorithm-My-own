#https://programmers.co.kr/learn/courses/30/lessons/12928#

def solution(n):
    sqrt = int(n**(1/2))	# n의 제곱근
    answer = 0	# 약수의 합을 저장하는 변수 선언
    for i in range(1,sqrt+1):	# 1부터 n의 제곱근 까지의 수 에서
        if n % i == 0:	# n가 i로 나누어 떨어진다면 i는 n의 약수
            if i**2 == n: # 만약 약수의 갯수가 홀수라면 
                answer += i	# 짝이 없으므로 한놈만 더해준다.
                return answer	# 약수의 합 리턴
            answer += i + n//i	# i # 약수와 그 짝을 더해준다.
    return answer #약수의 합 리턴