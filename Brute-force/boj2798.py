"""
블랙잭
https://www.acmicpc.net/problem/2798
"""

n, m = map(int,input().split())

cards = list(map(int,input().split()))

result = 0

for i in range(n):
    for j in range(i):
        for k in range(j):
            sumcard = cards[i] + cards[j] + cards[k]
            if sumcard > m:
                continue
            result = max(result , sumcard)

        
print(result)