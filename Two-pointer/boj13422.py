"""
도둑
https://www.acmicpc.net/problem/13422
"""
#https://baby-ohgu.tistory.com/27

from collections import deque
import sys

input = sys.stdin.readline


T = int(input())

for _ in range(T):
    N, M, K = map(int, input().split())
    arr = list(map(int, input().split()))

    right = 0
    result = 0
    nowsum = 0 

    q = deque()
    for left in range(N):
        while right < N + M - 1 and len(q) < M:
            q.append(arr[right%N])
            nowsum += arr[right%N]
            right += 1

        if nowsum < K:
            result += 1
        
        q.popleft()
        nowsum -= arr[left]
        left += 1

        if N == M:
            break
    print(result)