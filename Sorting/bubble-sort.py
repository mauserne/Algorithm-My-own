# 정렬되는 모습이 거품이 떠다니는것 같다.
# 현재항이 다음항보다 크면 교환한다.
arr = [3,5,7,1,2,9,6,8,4,0]

for i in range(len(arr)):
    print(len(arr) - i - 1)
    for j in range(0, len(arr) - i - 1):
        if arr[j] > arr[j+1]:
            arr[j] , arr[j+1] = arr[j+1] , arr[j]
        print(arr)