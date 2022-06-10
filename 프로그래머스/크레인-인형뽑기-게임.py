#https://programmers.co.kr/learn/courses/30/lessons/64061

def solution(board, moves):
    answer = 0
    moves = [i-1 for i in moves]
    stack = []    
    
    for move in moves:
        depth = 0

        while depth < len(board):
            if board[depth][move] == 0:
                depth += 1
            else:
                stack.append(board[depth][move])
                board[depth][move] = 0
                break

        if len(stack) > 1:
            if stack[-1] == stack[-2]:
                stack = stack[:-2]
                answer += 2
    return answer