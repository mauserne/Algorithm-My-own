import heapq

def heapsort(iterable):
    h = []
    result = []
    for value in iterable:
        heapq.heappush(h, value)
        print(h)
    for _ in range(len(h)):
        result.append(heapq.heappop(h))
    return result

result = heapsort([4,5,3,7,1,9,6,2,8])
print(result)