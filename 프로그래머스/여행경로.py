answer = []

def solution(tickets):
    used = [False]*len(tickets)
    
    def dfs(leaving, visited):
        global answer
        
        if answer:
            return

        if not False in used:
            answer = visited
            return
        q = []
        for idx, ticket in enumerate(tickets):
            if not used[idx]:
                dep, arv = ticket
                if dep == leaving:
                    q.append((arv,idx))
        for arv, idx in sorted(q):
            used[idx] = True
            dfs(arv, visited+[arv])
            used[idx] = False

    dfs('ICN', ['ICN'])

    return answer

print('출력', solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))