#2진법 구현

n = int(input())

result = ''
while n != 0:
    if n % 2:
        result = '1' + result
        n = n // 2
    else:
        result = '0' + result
        n = n // 2
    print(n)
print(result)