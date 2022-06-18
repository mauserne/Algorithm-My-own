#https://programmers.co.kr/learn/courses/30/lessons/12926

def solution(s, n):
    answer = ''
    
    for i in s:
        if 'A' <= i <= 'Z':	# i 가 대문자 알파벳이면
            if ord(i) + n <= ord('Z'):	# i를 아스키코드에서 오른쪽으로 n칸 옮겨도 'Z'보다 같거나 작으면
                answer += chr(ord(i)+n)	# answer 문자열에 chr 함수를 통해 아스키코드를 문자열로 바꾸어서 추가
            else:	# i를 오른쪽으로 n칸 옮겼더니 'Z'를 넘으면
                answer += chr(ord(i)+n - ord('Z') + ord('A')-1) # Z에서 초과한 만큼을 A에서 시작시킴
        elif 'a' <= i <= 'z': # i 가 소문자 알파벳이면
            if ord(i) + n <= ord('z'):
                answer += chr(ord(i)+n)
            else:
                answer += chr(ord(i)+n - ord('z') + ord('a')-1)
        else:	# i가 공백이면
            answer += ' '	# answer에 공백 추가
                
    return answer