answer = 0

def solution(routes):
    global answer
    answer = len(routes)

    routes.sort()

    visited = [False]*len(routes)

    def gyup(x,cycle):
        global answer 
        if x == len(routes):
            print('f',x)
            return
        if routes[x-1][0] <= routes[x][0] and routes[x-1][1] >= routes[x][1]:
            visited[x] = True
            answer -= 1
            print('ans',routes[x])
            gyup(x+1,0)
        elif routes[x-1][1] < routes[x][1]:
            print(x)
            if cycle == 1:
                return
            visited[x] = True
            answer -= 1
            gyup(x+1,1)

        print('either',x)
    
    idx = 1
    while idx < len(routes):
        if not visited[idx]:
            gyup(idx,0)
            visited[idx] = True
        idx += 1

    return answer

print(solution( [[-20,15], [-20,-15], [-14,-5], [-18,-13], [-5,-3]]  ))