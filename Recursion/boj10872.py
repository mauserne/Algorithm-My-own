# 팩토리얼을 재귀함수로 구현하기

n = int(input())

def facto(x):
    if x <= 1:
        return 1
    return x * facto( x - 1 )

print(facto(n))