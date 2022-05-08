def sol3(name):
    answer = 0
    min_move = len(name) - 1
    
    while name[min_move] == 'A' and min_move > 0:
        min_move -= 1

    for idx, char in enumerate(name):
        answer += min(ord(char)-ord('A') , ord('Z') - ord(char) + 1)

        next = idx + 1
        for i in range(idx + 1, len(name)):
            if name[i] != 'A':
                next = i
                break
        min_move = min(min_move, idx*2 + len(name) - next, (len(name)-next)*2 + idx)
    
    answer += min_move
    return answer


















def solution(name):

	# 조이스틱 조작 횟수 
    answer = 0
    
    # 기본 최소 좌우이동 횟수는 길이 - 1
    min_move = len(name) - 1

    while name[min_move] == 'A' and min_move > 0:
        min_move -= 1
    print(min_move)
    for i, char in enumerate(name):
        if char != 'A':
    	    # 해당 알파벳 변경 최솟값 추가
            answer += min(ord(char) - ord('A'), ord('Z') - ord(char) + 1)

            # 해당 알파벳 다음부터 연속된 A 문자열 찾기
            next = i + 1
            while next < len(name) and name[next] == 'A':
                next += 1

            # 기존, 연속된 A의 왼쪽시작 방식, 연속된 A의 오른쪽시작 방식 비교 및 갱신
            min_move = min(min_move, i*2 + len(name) - next , i + (len(name) - next)*2 )
        
    # 알파벳 변경(상하이동) 횟수에 좌우이동 횟수 추가
    answer += min_move
    return answer

def sol(name):
    answer = 0
    name = list(name)
    cursor = 0

    def check():
        for i in range(len(name)):
            if name[(cursor+i)%len(name)] != 'A':
                return i
            if name[cursor-i] != 'A':
                return -i
        return 'Done'

    while True:
        dist = check()
        if dist == 'Done':
            return answer 
        answer += abs(dist)

        if cursor + dist < 0:
            cursor = len(name) + (cursor + dist)
        else:
            cursor = (cursor+dist)%len(name)
        alp = ord(name[cursor]) - 64
        if alp > 13:
            answer += (27 - alp)
        else:
            answer += alp -1
        name[cursor] = 'A'
        print(name)
        print(answer)


def sol2(name):
    answer = 0
    name = list(name)
    nameleng = len(name)
    visited = [False] * (nameleng)
    leftfirst, rightfirst = 0,0
    left, right = 0,0

    for i in range(1,nameleng):
        if name[i] != 'A':
            if visited[i]:
                break
            if not rightfirst:
                rightfirst = i
            right = i
            visited[i] = True
        if name[nameleng-i] != 'A':
            if visited[nameleng-i]:
                break
            if not leftfirst:
                leftfirst = i
            left = i
            visited[nameleng-i] = True
        # i는 name[0] 으로부터 떨어진 거리또한 의미한다
    
    if left == 0 and right == 0:
        pass
    else:
        if leftfirst + rightfirst > nameleng -1 - left - right:
            answer += nameleng - leftfirst
        else:
            if left < right:
                answer += left*2 + right
            else:
                answer += right*2 + left
    
    for i in name:
        if i != 'A':
            alp = ord(i) - 64
            if alp > 13:
                answer += 27 - alp
            else:
                answer += alp - 1
    
    return answer 



print('출력', sol3(input()))