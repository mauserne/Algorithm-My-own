# 정렬하려는 배열에 중복된 값이 많고
# 배열의 최소값 최대값 배열길이를 파악할 수 있으면 쓰기 좋을듯

arr = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]

count = [0]* (max(arr) + 1)

for i in range(len(arr)):
    count[arr[i]] += 1

for i in range(len(count)):
    for j in range(count[i]):
        print(i, end=' ')