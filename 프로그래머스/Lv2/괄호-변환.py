def solution(p):
    def process(w):
        print(w)
        if w == '':
            return ''
        leftcnt = 0
        rightcnt = 0
        for i in w:
            if i == '(':
                leftcnt += 1
            elif i == ')':
                rightcnt += 1
            if leftcnt == rightcnt:
                break
        u = w[0 : leftcnt+rightcnt]
        v = w[leftcnt+rightcnt : ]
        print(u,v)

        if len(u) == 2:
            return '()' + process(v)
        else:
            return '(' + process(u[1:-1]) + ')' + process(v)

    return process(p)

print(solution('))))(((('))

def check(x):
    stack = []
    for i in x:
        if i == '(':
            stack.append(1)
        else:
            try:
                stack.pop()
            except:
                return False
    
    return True


def div(w):
    for i in w:
        leftcnt = 0
        rightcnt = 0
        for i in w:
            if i == '(':
                leftcnt += 1
            elif i == ')':
                rightcnt += 1
            if leftcnt == rightcnt:
                break
        return w[0 : leftcnt+rightcnt], w[leftcnt+rightcnt : ]
        

def solution(p):
    if not p:
        return ''
    
    u, v = div(p)

    if check(u):
        return u + solution(v)
    else:
        tmp = '('
        tmp += solution(v)
        tmp += ')'

        for i in u[1:-1]:
            if i == '(':
                tmp += ')'
            else:
                tmp += '('
        return tmp

print('solution',solution('))))(((('))