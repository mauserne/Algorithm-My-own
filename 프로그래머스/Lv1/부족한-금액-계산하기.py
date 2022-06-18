#https://programmers.co.kr/learn/courses/30/lessons/82612#

def solution(price, money, count):
    cost = 0
    for i in range(1,count+1):
        cost += price*i
        
    if cost > money:
        return cost - money
        
    return 0