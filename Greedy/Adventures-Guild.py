"""
모험가 길드
https://freedeveloper.tistory.com/367?category=888096
"""

a = int(input())
list = list(map(int,input().split()))
x = set(list)   # 중복 제거위해 list를 집합으로 만들어 변수 x에 선언
groups=0        # 그룹 갯수 

for i in x:
    groups += list.count(i) // i    # 자기 공포도만큼 그룹을 구성하기 위해
                                    # list에 공포도 같은 사람 숫자를 공포도로 나누고 그룹갯수 올림

print(groups)