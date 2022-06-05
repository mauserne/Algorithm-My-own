def solution(n, costs):
    answer = 0
    costs.sort(key = lambda x: x[2]) # 비용기준으로 오름차순 정렬
    visited = set([costs[0][0]]) # 연결을 확인하는 집합
    print(costs)
    
    # Kruskal 알고리즘으로 최소 비용 구하기
    while len(visited) != n:
        for idx, cost in enumerate(costs):
            print(idx,visited)
            print(cost[2])
            if cost[0] in visited and cost[1] in visited:  
                print(cost[0],cost[1])
                continue
            if cost[0] in visited or cost[1] in visited:
                visited.update([cost[0], cost[1]])
                answer += cost[2]
                break

    return answer
#출처: https://soohyun6879.tistory.com/145 [코딩기록:티스토리]

print(solution( 5, [[0, 1, 1], [0, 4, 5], [2, 4, 1], [2, 3, 1], [3, 4, 1]]  ))

    


def find_parent(parent, a):
    if parent[a] != a:
        parent[a] = find_parent(parent, parent[a])
    return parent[a]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent,b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def solution1(n, costs):
    answer = 0
    parent = [i for i in range(n)]
    costs.sort(key=lambda x:x[2])

    for i in costs:
        if find_parent(parent, i[0]) != find_parent(parent, i[1]):
            union_parent(parent,i[0],i[1])
            answer += i[2]

    return answer

print(solution1( 5, [[0, 1, 1], [0, 4, 5], [2, 4, 1], [2, 3, 1], [3, 4, 1]]  ))
