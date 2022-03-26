"""
두 수의 합
https://www.acmicpc.net/problem/3273
41892KB	132ms
"""


n = int(input())

arr = sorted(list(map(int, input().split())))

m = int(input())
count = 0

start = 0
end = n-1

while start < end:
    cal = arr[start] + arr[end]
    if cal == m:
        count += 1
    if cal <= m :
        start += 1
    else:
        end -= 1

print(count)