from time import sleep


N = int(input())
now = N

cycle = 0
while True:
    if now < 10:
        now = now*10+now
    else:
        a = now // 10 
        b = now % 10
        now = b*10+ (a+b)%10

    cycle += 1
    if now == N:
        break

print(cycle)