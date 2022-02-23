import sys



while True:
    arr = []
    n = int(sys.stdin.readline().rstrip())
    if n == 0:
        break
    for i in range(2,int(n**0.5)+1):
        print(i)
        if n%i == 0:
            continue
        arr.append(i)
        
    x = n - arr[-1]
    print(n,'=',x,'+',arr[-1])

