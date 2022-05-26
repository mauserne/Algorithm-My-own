from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    q = deque(truck_weights)
    onboard = deque([0 for _ in range(bridge_length)])

    while q or sum(onboard) != 0:
        #print('q',q)
        while q:
            if sum(onboard) + q[0] <= weight:
                onboard.append(q.popleft())
                onboard.popleft()
            else:
                break
        print(onboard)
        onboard.append(0)
        onboard.popleft()

        answer += 1

    return answer

print('출력',solution(2,10,[7,4,5,6]))