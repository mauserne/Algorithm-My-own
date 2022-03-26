"""
두 용액
https://www.acmicpc.net/problem/2470
"""

n = int(input())

arr = sorted(list(map(int, input().split())))

left = 0
right = n-1

best = abs(arr[left] + arr[right])
while left < right:
    cal = arr[left] + arr[right]
    if abs(cal) <= best:
        comb = (arr[left],arr[right])
        best = abs(cal)
        if best == 0:
            break
    if cal < 0:
        left += 1
    else:
        right -= 1

print(comb[0], comb[1])