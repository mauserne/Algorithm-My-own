"""
진법 변환2
https://www.acmicpc.net/problem/11005


수정 필요!!
"""



#A: 10, B: 11, ..., F: 15, ..., Y: 34, Z: 35

n,b = map(int,(input().split()))

result = []
while n:
    if n%b > 10:
        result.append(chr(n%b+55))
    else:
        result.append(n%b)
    n //= b

#ascii로 대입해야겠는데
#A -> 65 Z->90
print(''.join(map(str,result[::-1])))
