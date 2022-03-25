"""
예산
https://www.acmicpc.net/problem/2512
"""

n = int(input())

arr = list(map(int, input().split()))

start = 1
end = max(arr) 

m = int(input())

while start <= end:
    mid = (start + end) // 2
    cal = []
    for i in arr:
        if i > mid:
            cal.append(mid)
        else:
            cal.append(i)
    calsum = sum(cal)
    if calsum == m:
        print(mid)
        exit(0)
    elif calsum > m:
        end = mid - 1
    else:
        start = mid + 1

print(end)