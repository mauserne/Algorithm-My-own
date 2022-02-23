"""
최소공배수
https://www.acmicpc.net/problem/1934
"""

import math
import sys

t= int(input())

def lcm(x,y):
    a = x*y
    while y>0:
        x = x%y
        x,y = y,x
    return a//x
    

for _ in range(t):
    a,b = map(int,sys.stdin.readline().split())
    print(lcm(a,b))