def solution(n, k):
    answer = 0
    kbase = ''
    
    while n:
        kbase += str(n%k)
        n //= k
    kbase = kbase[::-1].split('0')
    print(int(kbase[0]))
    """
    kbase = [int(i) for i in kbase if i != '']

    maxk = max(kbase)
    
    for i in range(2,int((maxk+1)**1/2)+1):
        if arr[i]:
            multi = 2
            while i*multi <= maxk:
                arr[i*multi] = False
                multi += 1
    print(arr)
    print('heloo')
    # 소수찾기 알고리즘
    for i in kbase:
        if arr[i]:
            answer += 1
    """
    
    
    return answer

print(solution(797161,3))