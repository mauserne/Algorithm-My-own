def out():
    b = 'b'
    
    def inner():
        print(b)

    return inner()

out()
