#https://programmers.co.kr/learn/courses/30/lessons/17680

from collections import deque

def solution(cacheSize, cities):
    answer = 0
    cache = deque()
    
    for city in cities:
        if len(cache) > cacheSize:
            cache.popleft()
        city = city.upper()
        if city in cache:
            answer += 1
            cache.remove(city)
            cache.append(city)
        else:
            answer += 5
            cache.append(city)
    return answer