def solution(files):
    answer = []
    dic = dict()
    
    for file in files:
        headidx = ''
        numberidx = ''
        for i in range(len(file)):
            if file[i].isalpha() or file[i] in [' ','.','-']:
                if numberidx:
                    break
                headidx += file[i]
            elif file[i].isdigit():
                numberidx += file[i]
                
        dic[file] = [headidx.upper(),int(numberidx)]
        
    for i in sorted(dic.items(), key= lambda x:(x[1][0],x[1][1])):
        answer.append(i[0])
    
    return answer