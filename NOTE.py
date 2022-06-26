def solution(msg):
    answer = []
    dic = dict()
    for i in range(1,27):
        dic[chr(64+i)] = i
    
    while msg:
        print(msg)
        w = ''
        for i in range(len(msg)):
            w += msg[i]
            if w in dic:
                if w == msg:
                    answer.append(dic[w])
                    return answer
                continue
            else:
                print(w,i)
                answer.append(dic[w[:-1]])
                dic[w] = len(dic) + 1
                msg = msg[i:]
                break
    
    return answer


print(solution('KAKAO'))