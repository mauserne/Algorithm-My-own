#https://programmers.co.kr/learn/courses/30/lessons/42579

def solution(genres, plays):
    answer = []
    dic = {}

    for i,v in enumerate(plays):
        if not genres[i] in dic:
            dic[genres[i]] = [v, [v,i]]
        else:
            dic[genres[i]][0] += v
            dic[genres[i]].append([v,i])

    s = sorted(dic.items(), key=lambda x: x[1], reverse=True)
    
    for k in s:
        n = sorted(k[1][1:], key=lambda x:(-x[0], x[1]))[:2]
        for i in n:
            answer.append(i[1])

    return answer


print('출력',solution(['pop' ,'pop' ,'pop', 'rap','rap'], [45,50,40, 60, 70]))

"""
테스트 1 〉	통과 (0.02ms, 10.1MB)
테스트 2 〉	통과 (0.02ms, 10.2MB)
테스트 3 〉	통과 (0.01ms, 10.2MB)
테스트 4 〉	통과 (0.01ms, 10MB)
테스트 5 〉	통과 (0.06ms, 10.3MB)
테스트 6 〉	통과 (0.05ms, 10.3MB)
테스트 7 〉	통과 (0.04ms, 10.2MB)
테스트 8 〉	통과 (0.03ms, 10.1MB)
테스트 9 〉	통과 (0.01ms, 10.2MB)
테스트 10 〉	통과 (0.06ms, 10.1MB)
테스트 11 〉	통과 (0.02ms, 10.1MB)
테스트 12 〉	통과 (0.04ms, 10.3MB)
테스트 13 〉	통과 (0.06ms, 10.1MB)
테스트 14 〉	통과 (0.06ms, 10.1MB)
테스트 15 〉	통과 (0.01ms, 10.1MB)
"""

def sol1(genres, plays):
    answer = []
    dic = {}

    for i in range(len(genres)):
        if not genres[i] in dic:
            dic[genres[i]] = [plays[i], [(plays[i],i)]]
        else:
            dic[genres[i]][0] += plays[i]
            dic[genres[i]][1].append((plays[i],i))
            
    bestgenre = sorted(dic, reverse=True, key= lambda x:x[1])
    for i in bestgenre:
        tmp = sorted(dic[i][1], key=lambda x:(-x[0], x[1]))[:2]
        for i in tmp:
            answer.append(i[1])


    return answer
    
print('출력',sol1(['pop' ,'pop' ,'pop', 'rap','rap'], [45,50,40, 60, 70]))
