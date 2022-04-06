A = int(input())
T = int(input())
B = int(input())

arr = []

interval = 2

bun = 1
degi = 1
while True:
    for _ in range(2):
        arr.append((bun,0))
        bun += 1
        arr.append((degi,1))
        degi += 1

    for _ in range(interval):
        arr.append((bun,0))
        bun += 1

    for _ in range(interval):
        arr.append((degi,1))
        degi += 1
    
    if T < bun:
        print(arr.index((T,B))%A)
        break
    
    interval +=1