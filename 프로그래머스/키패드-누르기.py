#https://programmers.co.kr/learn/courses/30/lessons/67256

def solution(numbers, hand):
    answer = ''

    leftum = (3,0)
    rightum = (3,2)

    pad = [[1,2,3],[4,5,6],[7,8,9],['*',0,'#']]

    def matt(parm,row,col):
        return  abs(parm[0]-row)+abs(parm[1]-col)

    def search(num):
        for i in range(4):
                for j in range(3):
                    if pad[i][j] == num:
                        return i,j
    
    for number in numbers:
        i, j = search(number)

        if number in [1,4,7]:
            answer += 'L'
            leftum = (i,j)
        elif number in [3,6,9]:
            answer += 'R'
            rightum = (i,j)
        else:
            if matt(leftum,i,j) < matt(rightum,i,j):
                answer += 'L'
                leftum = (i,j)
            elif matt(leftum,i,j) > matt(rightum,i,j):
                answer += 'R'
                rightum = (i,j)
            else:
                if hand == 'left':
                    answer += 'L'
                    leftum = (i,j)
                elif hand == 'right':
                    answer += 'R'
                    rightum = (i,j)

    return answer


print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5],'right'))