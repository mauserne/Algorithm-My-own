def solution(n, t, m, p):
    game = '0'
    for i in range(1,100000):
        nbase = ''

        while i:
            if i%n > 9:
                nbase += chr(55+(i%n))
            else:
                nbase += str(i%n)
            i //=n
        game += nbase[::-1]
    
    arr = []
    while game:
        arr.append(game[:m])
        game = game[m:]
    
    answer = ''
    for i in arr:
        answer += i[p-1]
    return answer[:t]



def basechange(i,n):
    nbase = ''
    while i:
        if i%n > 9:
            nbase += chr(55+(i%n))
        else:
            nbase += str(i%n)
        i //=n
    return nbase[::-1]

def solution(n, t, m, p):
    answer = ''
    game = '0'
    number = 1
    while len(answer) != t:
        answer = ''

        game += basechange(number,n)
        number += 1

        arr = []
        tmp = game[:]
        while tmp:
            arr.append(tmp[:m])
            tmp = tmp[m:]

        for k in arr:
            try:
                answer += k[p-1]
            except:
                pass
        answer = answer[:t]
    return answer

    # 14 15 16에서 시간초과 발생해서 배열로 늘렸다 줄이는 과정을 리스트 슬라이싱으로 바꿈

def solution(n, t, m, p):
    answer = ''
    game = '0'
    number = 1
    while len(answer) != t:
        answer = ''

        game += basechange(number,n)
        number += 1

        for i in game[p-1::m]:
            answer += i

        answer = answer[:t]
    return answer

print(solution(16,	16,	2,	2))