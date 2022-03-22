n = int(input())
cards = list(map(int, input().split()))


m = int(input())
numbs = list(map(int, input().split()))

hash = {}

for i in cards:
    print(hash)
    if i in hash:
        hash[i] += 1
    else:
        hash[i] = 1

for i in numbs:
    if i in hash:
        print(hash[i], end=' ')
    else:
        print(0, end=' ')