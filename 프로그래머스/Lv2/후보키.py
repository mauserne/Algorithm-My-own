from itertools import combinations
from collections import defaultdict


def search(c,relation):
    ddict = defaultdict(lambda:0)
    for info in relation:
        tmp =[]
        for i in c:
            tmp.append(info[i])
        candkey = ' '.join(tmp)
                #print(candkey)
        if ddict[candkey] == 1:
            print(c,'candkey failed')
            return False
        ddict[candkey] = 1
            #print(list(ddict))
    return True

def checkans(candkey,answer):
    for ans in answer.keys():
        print(candkey,ans)
        for _ in range(len(candkey)):
            for k in candkey:
                if ans == '':
                    return False
                print(k,ans)
                if k in ans:
                    ans = ans.replace(k,'')

        
    return True

def solution(relation):
    answer = defaultdict(lambda:0)
    cases = []
    for i in range(1,len(relation)+2):
        cases.append(list(combinations([j for j in range(len(relation[0]))],i)))
    print(cases)
    for case in cases:
        for c in case:
            candkey = ''.join(str(i) for i in c)
            
            if checkans(candkey,answer):    
                if search(c,relation): 
                    print(c,'success')
                    c = [str(i) for i in c]
                    answer[candkey] = 1
            
                
                
    return len(answer)

print('출력 :', solution(    [['a','1','aaa','c','ng'],['b','1','bbb','c','g'],['c','1','aaa','d','ng'],['d','2','bbb','d','ng']]))