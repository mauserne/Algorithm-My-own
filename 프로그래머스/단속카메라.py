def solution(routes):
    answer = 0 
    length = len(routes)
    visited = [False]*length

    routes.sort(key=lambda x:x[1])

    for i in range(length):
        if not visited[i]:
            camera = routes[i][1]
            answer += 1
            for j in range(i+1,length):
                if not visited[j]:
                    if routes[j][0] <= camera <= routes[i][1]:
                        visited[j] = True
    return answer
        


print(solution( [[-20,15], [-20,-15], [-14,-5], [-18,-13], [-5,-3]]  ))