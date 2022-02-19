"""
단어 뒤집기2
https://www.acmicpc.net/problem/17413
time spent : 45min
"""


s = input()
#꺽쇠 내용은 안 뒤집어야함
#<가 등장하면 >까지 따로 저장
#문자열 뒤집기어서 append

flip = []
output = []
count = 0 
for _ in s:
    if s[count] == '<':
        if len(flip) > 0 :
            for i in flip[::-1]:
                output.append(i)
            output.append(s[count])
            flip = []
            count += 1
        while True:
            output.append(s[count])
            count += 1
            if output[-1] == '>':
                break
    elif s[count] == ' ':
        for i in flip[::-1]:
            output.append(i)
        output.append(s[count])
        flip = []
        count += 1
    else:
        flip.append(s[count])
        count += 1
    if count == len(s):
        for i in flip[::-1]:
            output.append(i)
        break
        
print(''.join(output))
    

#큐 두개쓰고 pop()해서 아웃풋에 붙여 구별 스페이스