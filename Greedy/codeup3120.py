"""
리모컨
https://www.codeup.kr/problem.php?id=3120&rid=0

time spent : 2h 25m
"""

a, b = map(int,input().split())

temp = abs(b - a)

count = 0
while temp != 0:
    settinglist = []
    for i in [10, 5, 1]:
        x = temp - i
        settinglist.append(abs(x))
    temp = min(settinglist)
    
    count += 1

print(count)

# abs() 절대값함수
# 절대값으로 거리 구하는 아이디어.. 거리가 0이 될 때까지 반복
# 순회할 때 마다 count += 1 