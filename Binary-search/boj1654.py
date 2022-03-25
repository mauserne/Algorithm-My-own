#parametric search라고도 부르는, 이분 탐색을 응용하여 최솟값이나 최댓값을 찾는 테크닉을 배우는 문제
"""
랜선 자르기
https://www.acmicpc.net/problem/1654
"""
import sys


k, n = map(int, input().split())

lan = [int(sys.stdin.readline()) for _ in range(k)]
start = 1
end = max(lan)


#n개만큼의 랜선을 가장 길게 잘라 만들려면 주어진 랜선을 몇 cm씩 잘라야 하는가?


#이분탐색
while start <= end:
    mid = (start + end) // 2
    print(start, mid, end)
    count = 0
    for i in lan:
        count += i // mid
    print(count)
    if count >= n:
        start = mid + 1
    else:
        end = mid - 1

print(end)