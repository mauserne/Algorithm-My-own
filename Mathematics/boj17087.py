"""
숨바꼭질 6
https://www.acmicpc.net/problem/17087
"""
#이게.. gcd문제라고?

import math

n,s  = map(int,input().split())

arr = list(map(int,input().split()))

distance = []
for i in arr:
    distance.append(abs(s - i))

ans=distance[0]
for i in range(1,n):
    ans=math.gcd(distance[i],ans)

print(ans)