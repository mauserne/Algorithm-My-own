def solution(new_id):
    answer = new_id.lower()

    idx = 0
    while True:
        if 'a' <= answer[idx] <= 'z' or '0' <= answer[idx] <= '9' or answer[idx] in ['-','_','.']:
            idx += 1
        else:
            answer = answer.replace(answer[idx],'')
        if idx == len(answer):
            break
    while '..' in answer:
        answer = answer.replace('..','.')

    if answer and answer[0] == '.':
        answer = answer[1:]
    if answer and answer[-1] == '.':
        answer = answer[:-1]
    if not answer:
        answer = 'a'
    answer = answer[:15]
    if answer[-1] == '.':
        answer = answer[:14]
    if len(answer) < 3:
        answer += answer[-1]*(3-len(answer))

    return answer

print('출력', solution(input()))

#https://programmers.co.kr/learn/courses/30/lessons/72410/solution_groups?language=python3
def solution(new_id):
    answer = ''
    # 1
    new_id = new_id.lower()
    # 2
    for c in new_id:
        if c.isalpha() or c.isdigit() or c in ['-', '_', '.']:
            answer += c
    # 3
    while '..' in answer:
        answer = answer.replace('..', '.')
    # 4
    if answer[0] == '.':
        answer = answer[1:] if len(answer) > 1 else '.'
    if answer[-1] == '.':
        answer = answer[:-1]
    # 5
    if answer == '':
        answer = 'a'
    # 6
    if len(answer) > 15:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]
    # 7
    while len(answer) < 3:
        answer += answer[-1]
    return answer