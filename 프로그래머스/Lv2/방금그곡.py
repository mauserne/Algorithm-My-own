#https://programmers.co.kr/learn/courses/30/lessons/17683#

def notecheck(org):
    arr = []
    for i in org:
            if i == '#':
                arr[-1] = arr[-1]+'#'
            else:
                arr.append(i)
    return arr

def solution(m, musicinfos):
    answer = []
    m = notecheck(m)

    for musicinfo in musicinfos:
        info = musicinfo.split(',')
        
        s = list(map(int,info[0].split(':')))
        e = list(map(int,info[1].split(':')))
        mins = e[1]-s[1] + (e[0] - s[0])*60
        
        notes = notecheck(info[3])
        notes = notes*((mins // len(notes))+1)
        notes = notes[:mins]
        
        idx = 0
        while idx < len(notes):
            if m == notes[idx:idx+len(m)]:
                answer.append([info[2],mins,notes])
                break
            idx += 1
                
    answer.sort(key=lambda x:x[1], reverse= True)
    
    if not answer:
        return "(None)"
    return answer[0][0]