import sys 

sys.setrecursionlimit(10**6) 

def draw(LEN):
    if LEN == 1:
        return '*'
    
    stars = draw(LEN//3)
    L = []

    for i in stars:
        L.append(i*3)
    for i in stars:
        L.append(i+' '*(LEN//3)+i)
    for i in stars:
        L.append(i*3)
    return L


N = int(input())
print('\n'.join(draw(N)))