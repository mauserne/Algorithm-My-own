"""
숫자 카드 2
https://www.acmicpc.net/problem/10816
"""

from bisect import bisect_left, bisect_right



n = int(input())
cards = list(map(int, input().split()))
cards.sort()


m = int(input())
numbs = list(map(int, input().split()))

for i in numbs:
    print( bisect_right(cards,i) - bisect_left(cards,i), end=' ' )


"""
다른풀이
https://hongcoding.tistory.com/12
"""