#https://programmers.co.kr/learn/courses/30/lessons/86491
def solution(sizes):
    # 객체 정렬
    maxw,maxh = 0,0
    for size in sizes:
        size.sort()
        maxw = max(size[0],maxw)
        maxh = max(size[1],maxh)
        
    return maxw*maxh