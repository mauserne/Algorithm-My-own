def solution(new_id):
    answer = new_id.lower()
    idx = 0
    while True:
        if 'a' <= answer[idx] <= 'z' or '0' <= answer[idx] <= '9' or answer[idx] in ['-','_','.']:
            idx += 1
        else:
            print(answer[idx])
            answer = answer.replace(answer[idx],'')
        if idx == len(answer):
            break

    answer = answer.replace('...','.')
    answer = answer.replace('..','.')

    if answer[0] == '.':
        answer = answer[1:]
    if answer[-1] == '.':
        answer = answer[:-1]
    print(answer)
    if not answer:
        answer = 'a'*len(new_id)
    answer = answer[:15]
    if answer[-1] == '.':
        answer = answer[:14]
    if len(answer) < 3:
        answer += answer[-1]*(3-len(answer))



    
    return answer

print('출력', solution(input()))