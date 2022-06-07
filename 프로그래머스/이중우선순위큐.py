import heapq

def solution(operations):
    heap = []

    for oper in operations:
        func, val = oper.split()
        val = int(val)
        if func == "I":
            heapq.heappush(heap, val)
        elif heap:
            if val == -1:
                heapq.heappop(heap)
            else:
                heap = heapq.nlargest(len(heap),heap)[1:]
                heapq.heapify(heap)
        print(heap)

    heap = heapq.nlargest(len(heap),heap)
    return 0


print(solution(["I 7","I 5","I -5","D -1"]	))