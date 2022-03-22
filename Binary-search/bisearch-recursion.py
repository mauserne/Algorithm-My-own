def binary_search(arr, target, start, end):
    print(start, end)
    if start > end:
        return None
    mid = (start + end) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search(arr, target, start, mid-1)
    else:
        return binary_search(arr, target, mid + 1, end)

n, target = list(map(int, input().split()))

arr = list(map(int, input().split()))

result = binary_search(arr, target, 0, n-1)
if result == None:
    print('원소없음')
else:
    print(target,'은',result + 1,'번째에 있어요')