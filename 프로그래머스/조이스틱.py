def solution(name):
    answer = 0
    name = list(name)
    namelen = len(name)-1
    cursor = 0
    left = 0
    right = namelen
    rightfirst = namelen

    for word in name:
        if word != 'A':
            alp = ord(word) - 65
            if alp > 12:
                answer += 26 - alp
            else:
                answer += alp
            print(answer)
  
    while cursor < namelen - cursor:
        if name[cursor] != 'A':
            left = cursor
        if name[namelen - cursor] != 'A':
            if not rightfirst:
                rightfirst = namelen - cursor
            right = namelen - cursor
        cursor += 1

    print(left,right)
    if right-left < left + namelen - right:
        answer += rightfirst
    if left < right:
        answer += left*2 + (namelen - right) +1
    else:
        answer += right*2 + 1 +left

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
        print(visited)
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
        if leftfirst + rightfirst > nameleng - left - right:
            print(left,right)
            print('as')
            answer += nameleng - leftfirst
        else:
            print(leftfirst,rightfirst)
            if left < right:
                answer += left*2 + right
            else:
                answer += right*2 + left
    
    print(answer)
    
    for i in name:
        if i != 'A':
            alp = ord(i) - 64
            if alp > 13:
                answer += 27 - alp
            else:
                answer += alp - 1
    
    return answer 



print('출력', sol2(input()))