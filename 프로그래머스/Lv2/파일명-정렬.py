import heapq

def solution(files):
    answer = []
    dic = dict()
    dot = files[0].index('.')
    files = [i[:dot] for i in files]
    print(files)
    for file in files:
        tmpalpha = ''
        tmpdigit = ''
        dic[file] = ['',0]
        for i in file:
            if tmpalpha and tmpdigit:
                break
            if i.isalpha():
                if tmpdigit:
                    dic[file][1]=int(tmpdigit)
                tmpalpha += i
            if i.isdigit():
                if tmpalpha:
                    print(tmpalpha)
                    dic[file][0]+=tmpalpha
                tmpdigit += i
    print(dic)
    return answer

print(solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))