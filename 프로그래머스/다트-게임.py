#https://programmers.co.kr/learn/courses/30/lessons/17682

def solution(dartResult):
    dartResult = [i for i in dartResult]
    print(dartResult)
    history = []
    
    while dartResult:
        
        fstin = dartResult.pop(0)
        if fstin.isdigit():
            if fstin == '1' and dartResult[0] == '0':
                    table = 10
                    dartResult.pop(0)
            else:
                table = int(fstin)
        
        fstin = dartResult.pop(0)
        if fstin == 'D':
            table **= 2
        elif fstin == 'T':
            table **= 3
        
        if dartResult and not dartResult[0].isdigit():
            fstin = dartResult.pop(0)
            if fstin == '#':
                table *= -1
            elif fstin == '*':
                table *= 2
                if history:
                    history[-1] *= 2 
        
        print(history)
        history.append(table)
            
    return sum(history)