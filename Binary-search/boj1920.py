"""
수 찾기
https://www.acmicpc.net/problem/1920
"""


def bi_search(arr, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return 1
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return 0 



n = int(input())
arr1 = list(map(int, input().split()))
arr1.sort()


m = int(input())
arr2 = list(map(int, input().split()))

for i in arr2:
    print(bi_search(arr1, i, 0, n-1))