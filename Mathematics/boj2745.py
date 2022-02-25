"""
진법 변환
https://www.acmicpc.net/problem/2745
time spent : 11min
"""



n,b = input().split()

b = int(b)

# b진법에서 10진법으로
#일단 각 자릿수 10진법으로 

arr = []
for i in n :
    if '0' <= i <= '9':
        arr.append(int(i))
    else:
        arr.append(ord(i)-55)

# 자릿수에 거듭제곱맞게 더하고 저장

arr.reverse()

result = 0
for i in range(len(arr)):
    result += arr[i]*(b**i)

print(result)