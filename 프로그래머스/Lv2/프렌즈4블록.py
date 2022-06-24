#https://programmers.co.kr/learn/courses/30/lessons/17679

def search(x,y,newboard,willpow):
    nowfriend = newboard[x][y]
    if newboard[x][y] == newboard[x+1][y] == newboard[x][y+1] == newboard[x+1][y+1] == nowfriend:
        # 2x2 블럭 확인
        print('detect',x,y)
        willpow.update([(x,y),(x+1,y),(x,y+1),(x+1,y+1)])
        print(willpow)


def solution(m, n, board):
    answer = 0
    newboard = [['']*m for _ in range(n)]
    for i in newboard:
        print(i)
    #print(newboard)
    for j in range(n):
        for i in range(m-1,-1,-1):
            print(i,j)
            newboard[j][m-i-1] += board[i][j]
    
    for i in newboard:
        print(i)
    while True:
        willpow = set()
        print(willpow)
        for i in range(n-1):
            for j in range(m-1):
                if newboard[i][j] == '0':
                    break
                search(i,j,newboard,willpow)
        willpow = sorted(list(willpow),key=lambda x:(x[0],-x[1]))
        for x,y in willpow:
            print('poping',x,y)
            newboard[x].pop(y)
            for i in newboard:
                print(i)
        for i,v in enumerate(newboard):
            newboard[i] += ['0']*(m - len(v))
        for i in newboard:
            print(i)
        if not willpow:
            break
        answer += len(willpow)

    return answer

print(solution(4,5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]		))


"""
테스트 1 〉	통과 (0.04ms, 10.3MB)
테스트 2 〉	통과 (0.06ms, 10.4MB)
테스트 3 〉	통과 (0.02ms, 10.5MB)
테스트 4 〉	통과 (1.43ms, 10.3MB)
테스트 5 〉	통과 (25.13ms, 10.3MB)
테스트 6 〉	통과 (3.09ms, 10.3MB)
테스트 7 〉	통과 (0.76ms, 10.5MB)
테스트 8 〉	통과 (1.48ms, 10.2MB)
테스트 9 〉	통과 (0.04ms, 10.3MB)
테스트 10 〉	통과 (0.52ms, 10.3MB)
테스트 11 〉	통과 (1.46ms, 10.3MB))
"""