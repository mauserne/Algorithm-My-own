def solution(n, times):
    answer = 0

    times.sort()

    arr = [n//len(times)]*len(times)
    print(arr)
    return answer

print(solution(6,[7,10]))