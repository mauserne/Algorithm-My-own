"""
나무 자르기
https://www.acmicpc.net/problem/2805
"""

n, m = map(int, input().split())

tree = list(map(int, input().split()))
start = 1
end = max(tree)

# 이분탐색

while start <= end:
    mid = (start + end) // 2
    count = 0
    print(start, mid, end)
    
    for i in tree:
        if i >= mid:
            count += i - mid
    print(count)
    if count >= m:
        start = mid + 1
    else:
        end = mid - 1

print(end)