import sys

arr = [i for i in range(10001)]



def bi_search(target, start, end):
    mid = 0 
    while start <= end:
        mid = (start + end) //2
        print(start, end, mid)
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            start = mid + 1
        if arr[mid] > target:
            end = mid - 1
    return -1

print(bi_search(5025, 1, 10000))