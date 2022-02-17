"""

!! 오답 !!

에디터
https://www.acmicpc.net/problem/1406
time spent:1hour
"""

import sys

string = list(input())

editor  = ['']
for i in range(len(string)):
    editor.append(string[i])
editor.append('')

cursor = -1
n = int(input())
for _ in range(n):
    command = sys.stdin.readline().rstrip.split()
    if command[0] == 'L':
        if cursor == 1 -1 * len(editor):
            continue
        else:
            #커서 좌로 1
            cursor -= 1
    if command[0] == 'D':
        # 커서 우로1
        if cursor == -1:
            continue
        else:
            cursor += 1
    if command[0] == 'B':
        #커서 좌측 문자 삭제
        del editor[cursor-1] 
    if command[0] == 'P':
        #커서 왼쪽에 command[1]추가
        editor.insert(cursor, command[1])

print(''.join(editor))

"""
스택 두개를 이용하는 풀이??
"""