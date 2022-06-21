dx = [-1,0,0,1]
dy = [0,-1,1,0]

def dfs(x,y,place,visited,step):
    step += 1
    if step > 2:
        return True
        # P로부터 2 맨해탄 거리 내에 다른 P 없음 -> 거리두기 만족
        
    visited[x][y] = True

    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y

        if 0 <= nx < 5 and 0 <= ny < 5:
            if place[nx][ny] != 'X' and not visited[nx][ny]:
                if place[nx][ny] == 'P':
                    return False
                    # 거리두기 실패
                else:
                    if visited[nx][ny]:
                        continue
                    if dfs(nx,ny,place,visited,step) == False:
                        return False

def search(place,visited):
    for i in range(5):
        for j in range(5):
            if place[i][j] == 'P' and not visited[i][j]:
                if dfs(i,j,place,visited,0) == False:
                    # 이번 place는 글러먹음
                    return False
    return True


def solution(places):
    answer = []
    for place in places:
        visited = [[False]*5 for _ in range(5)]

        if search(place,visited):
            answer.append(1)
        else:
            answer.append(0)
            
    return answer

print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))

"""
테스트 1 〉	통과 (0.09ms, 10.4MB)
테스트 2 〉	통과 (0.04ms, 10.3MB)
테스트 3 〉	통과 (0.04ms, 10.4MB)
테스트 4 〉	통과 (0.06ms, 10MB)
테스트 5 〉	통과 (0.06ms, 10.1MB)
테스트 6 〉	통과 (0.06ms, 10.2MB)
테스트 7 〉	통과 (0.04ms, 10.2MB)
테스트 8 〉	통과 (0.05ms, 10.2MB)
테스트 9 〉	통과 (0.06ms, 10.3MB)
테스트 10 〉	통과 (0.04ms, 10.2MB)
테스트 11 〉	통과 (0.04ms, 10.2MB)
테스트 12 〉	통과 (0.06ms, 10.3MB)
테스트 13 〉	통과 (0.05ms, 10.4MB)
테스트 14 〉	통과 (0.05ms, 10.2MB)
테스트 15 〉	통과 (0.03ms, 10.3MB)
테스트 16 〉	통과 (0.05ms, 10.3MB)
테스트 17 〉	통과 (0.05ms, 10.2MB)
테스트 18 〉	통과 (0.05ms, 10.3MB)
테스트 19 〉	통과 (0.05ms, 10.3MB)
테스트 20 〉	통과 (0.05ms, 10.3MB)
테스트 21 〉	통과 (0.04ms, 10.2MB)
테스트 22 〉	통과 (0.04ms, 10.2MB)
테스트 23 〉	통과 (0.04ms, 10.3MB)
테스트 24 〉	통과 (0.02ms, 10.3MB)
테스트 25 〉	통과 (0.03ms, 10.3MB)
테스트 26 〉	통과 (0.02ms, 10.3MB)
테스트 27 〉	통과 (0.04ms, 10.3MB)
테스트 28 〉	통과 (0.05ms, 10.1MB)
테스트 29 〉	통과 (0.05ms, 10.2MB)
테스트 30 〉	통과 (0.06ms, 10.3MB)
테스트 31 〉	통과 (0.10ms, 10.3MB)
"""


