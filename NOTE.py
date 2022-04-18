C = int(input())

result = []
for _ in range(C):
    a = list(map(int, input().split()))
    avg = (sum(a)-a[0])/a[0]
    count = 0
    for i in a[1:]:
        if i > avg:
            count += 1
    result.append(count/a[0]*100)

for i in result:
        print(f'{i:.3f}%')