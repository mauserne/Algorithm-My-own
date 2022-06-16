#https://programmers.co.kr/learn/courses/30/lessons/17681

def solution(n, arr1, arr2):
    answer = []
    result = [[],[]]
    cnt = 0
    for arr in (arr1,arr2):
        for i in arr:
            a = bin(i)[2:]
            a = '0'*(n - len(a)) + a
            result[cnt].append(a)
        cnt += 1
    
    for i in range(n):
        tmp = ''
        for j in range(n):
            if result[0][i][j] == '1' or result[1][i][j] == '1':
                tmp += '#'
            else:
                tmp += ' '
        answer.append(tmp)

    return answer