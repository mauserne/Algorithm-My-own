def sol(n,times):
    left, right = 1, max(times)*n

    while left<=right:
        people = 0
        mid = (left+right)//2
        for i in times:
            people += mid // i

            if people >= n:
                answer = mid
                right = mid - 1
                break
        else:
            left = mid + 1
    
    return answer 
print(sol(9,[10,1]))

""""
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.13ms, 10.2MB)
테스트 3 〉	통과 (3.35ms, 10.3MB)
테스트 4 〉	통과 (163.30ms, 14.2MB)
테스트 5 〉	통과 (326.37ms, 14.2MB)
테스트 6 〉	통과 (179.55ms, 14.3MB)
테스트 7 〉	통과 (402.81ms, 14.2MB)
테스트 8 〉	통과 (443.80ms, 14.2MB)
테스트 9 〉	통과 (0.02ms, 10.1MB)

"""