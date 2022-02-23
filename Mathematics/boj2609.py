a, b = map(int,input().split())

def gcd(x,y):
    while y != 0:
        x = x % y
        x,y = y,x
    return x

def lcm(x,y):
    return a*b//gcd(x,y)
    
if b > a :
    a, b = b, a

print(gcd(a,b))
print(lcm(a,b))
    
#큰 수를 작은 수로 나누어 구한 나머지로 큰 수를 대체한다. 
#큰 수를 작은 수로 계속 나누어서, 나누어 떨어질 때까지 반복한다. 
# 나누어 떨어질 때(나머지가 0일 때), 나누는 수가 최대공약수이다

#math 라이브러리도 있는데.. 직접 구현할수있어야지

#map 객체라면서 왜 대입할수있지?