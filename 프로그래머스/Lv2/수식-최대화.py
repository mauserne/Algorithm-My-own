from itertools import permutations

def solution(expression):
    answer = -1

    calc = []
    for i,v in enumerate(expression):
        if v in ['-','+','*']:
            calc.append((v))

    numbers = expression.replace('*',' ').replace('+',' ').replace('-',' ')
    numbers = list(map(int,numbers.split()))


    for combo in permutations(['-','+','*'],3):
        tmpcalc, tmpnums = calc[:], numbers[:]
        
        for i in combo:
            while i in tmpcalc:
                print(tmpcalc)
                pos = tmpcalc.index(i)
                if i == '-':
                    tmpnums[pos] = tmpnums[pos] - tmpnums[pos+1]
                if i == '+':
                    tmpnums[pos] = tmpnums[pos] + tmpnums[pos+1]
                if i == '*':
                    tmpnums[pos] = tmpnums[pos] * tmpnums[pos+1]

                tmpnums.pop(pos+1)
                tmpcalc.pop(pos)
                
        
        answer = max(abs(tmpnums[0]),answer)

    return answer

print(solution( "100-200*300-500+20"	))


"""
테스트 1 〉	통과 (0.04ms, 10.4MB)
테스트 2 〉	통과 (0.06ms, 10.4MB)
테스트 3 〉	통과 (0.06ms, 10.4MB)
테스트 4 〉	통과 (0.06ms, 10.3MB)
테스트 5 〉	통과 (0.10ms, 10.3MB)
테스트 6 〉	통과 (0.08ms, 10.4MB)
테스트 7 〉	통과 (0.08ms, 10.3MB)
테스트 8 〉	통과 (0.10ms, 10.4MB)
테스트 9 〉	통과 (0.13ms, 10.3MB)
테스트 10 〉	통과 (0.09ms, 10.4MB)
테스트 11 〉	통과 (0.08ms, 10.4MB)
테스트 12 〉	통과 (0.18ms, 10.4MB)
테스트 13 〉	통과 (0.15ms, 10.4MB)
테스트 14 〉	통과 (0.12ms, 10.4MB)
테스트 15 〉	통과 (0.15ms, 10.3MB)
테스트 16 〉	통과 (0.08ms, 10.3MB)
테스트 17 〉	통과 (0.05ms, 10.4MB)
테스트 18 〉	통과 (0.06ms, 10.3MB)
테스트 19 〉	통과 (0.05ms, 10.4MB)
테스트 20 〉	통과 (0.07ms, 10.4MB)
테스트 21 〉	통과 (0.09ms, 10.4MB)
테스트 22 〉	통과 (0.13ms, 10.2MB)
테스트 23 〉	통과 (0.05ms, 10.4MB)
테스트 24 〉	통과 (0.19ms, 10.4MB)
테스트 25 〉	통과 (0.13ms, 10.4MB)
테스트 26 〉	통과 (0.05ms, 10.3MB)
테스트 27 〉	통과 (0.11ms, 10.4MB)
테스트 28 〉	통과 (0.19ms, 10.4MB)
테스트 29 〉	통과 (0.11ms, 10.4MB)
테스트 30 〉	통과 (0.18ms, 10.5MB)
"""