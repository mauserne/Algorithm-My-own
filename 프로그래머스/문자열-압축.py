def solution(s):
    answer = len(s)
    div = 1

    while div <= len(s)//2:
        tmp = s
        divarr = []

        while tmp:
            divarr.append(tmp[:div])
            tmp = tmp[div:]
        print(divarr)

        now = 1
        comp = ''
        for i in range(1,len(divarr)):
            if divarr[i-1] == divarr[i]:
                now += 1
            else:
                print(now)
                if now == 1:
                    comp += divarr[i-1]
                else:
                    comp += str(now)+divarr[i-1]
                now = 1
        if now == 1:
            comp += divarr[i]
        else:
            comp += str(now)+divarr[i]
        print(comp)
        
        answer = min(answer, len(comp))

        div += 1
    return answer

        

print(solution("abcabcdededededede"	))