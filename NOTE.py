def hansu(num):
    count = 0
    for i in range(1, num+1):
        arr = list(map(int, str(i)))
        if i < 100:
            count += 1
        elif arr[0] - arr[1] == arr[1] - arr[2]:
            count += 1

    return count
    

num = int(input())
print(hansu(num))