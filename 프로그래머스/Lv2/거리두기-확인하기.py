# dfs
dx = [-1,0,0,1]
dy = [0,-1,1,0]

def solution(places):
    answer = []
    for place in places:

        for i in place:
            print(i)
        print()

        visited = [[False] * 5 for _ in range(5)]
        keeprule = True

        def dfs(x,y,matt):
            if matt < 1:
                return False
            matt += 1
            visited[x][y] = True

            for i in range(4):
                nx = dx[i] + x
                ny = dy[i] + y
                if 0 <= nx < 5 and 0 <= ny < 5:
                    if not visited[nx][ny] and place[nx][ny] != 'X':
                        if dfs(nx,ny,matt) == False:
                            return False
                    
                    
                        
        
        for i in range(5):
            for j in range(5):
                if keeprule == False:
                    break
                if place[i][j] == 'P' and not visited[i][j]:
                    if dfs(i,j,0) == False:
                        keeprule = False
        if keeprule == False:
            answer.append(0)
        else:
            answer.append(1)
    return answer

print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))