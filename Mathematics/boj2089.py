"""
-2진수
https://www.acmicpc.net/problem/2089
"""

#풀이🙏
#-2진수로 변환하고자 하는 값 n을 입력받는다.
#n이 -2로 나누어 떨어지지 않는 경우에는 결과값에 1을 붙이고 소수가 아닌 몫을 구하기 위해 n//-2에 1을 더한다.
#n이 -2로 나누어 떨어지는 경우에는 결과값에 0을 붙이고 n//-2을 수행하여 n을 초기화한다.
#
n = int(input())
res =''
if n == 0:
    print(0)
    exit()
while n:
    if n % (-2):
        res = '1' + res
        # -2로 나누어 떨어지지 않는 경우 몫을 구하기 위해 1을 더함
        n = n//-2 + 1
    else:
        res = '0' + res
        n = n//-2
    print(n)

print(res)