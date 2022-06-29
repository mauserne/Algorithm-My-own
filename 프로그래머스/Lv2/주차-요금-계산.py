#https://programmers.co.kr/learn/courses/30/lessons/92341#

from collections import defaultdict
import math

def out(s,e):
    s = list(map(int,s.split(":")))
    e = list(map(int,e.split(":")))
    
    return e[1] - s[1] + (e[0] - s[0]) * 60
    
def solution(fees, records):
    answer = []
    dic = dict()
    mdict = defaultdict(int)
    
    for record in records:
        time,car,status = record.split()
        if status == "IN":
            dic[car] = time
        else:
            mins = out(dic[car],time)
            mdict[car] += mins
            dic.pop(car)
            
    for log in dic.items():
        car, time = log

        mins = out(time,"23:59")
        mdict[car] += mins
    print(mdict)
    
    for car, mins in sorted(mdict.items()):
        print(car)
        if mins <= fees[0]:
            answer.append(fees[1])
        else:
            charge = fees[1] + math.ceil((mins - fees[0]) / fees[2])*fees[3]
            answer.append(charge)
                
    return answer