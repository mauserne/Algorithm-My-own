a = [1,2,3]

def draw():
    b = list(a)
    b[1] = 77
    print(a)
    print(b)

draw()