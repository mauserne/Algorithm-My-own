"""
📌Q4. 강의에서 미국과 유럽의 엘리베이터 층수를 변환하는 프로그램이 나왔습니다.

      그와 비슷하게 우리는 한국 나이를 미국 나이로 변환하는 프로그램을 코딩 해봅시다.

hint: 미국 나이는 생일이 지났는지 안지났는지가 중요하죠!

birth = int(input("생일이 지났습니까? 맞으면 0 아니면 -1 : "))
"""

"""
kr_age = int(input("당신의 한국 나이는 몇살 입니까? "))

us_age = kr_age - 1

while True:
    birth = int(input("생일이 지났습니까? 맞으면 0 아니면 -1 : "))
    if birth == 0 or birth == -1:
        break

us_age = kr_age - 1 + birth

print('당신의 미국 나이는', us_age,'살 입니다.')
"""

kr_age = int(input("당신의 한국 나이는 몇살 입니까? "))

if kr_age < 1:
    print("뭐? 한국 나이가 0보다 작다고? 거짓말쟁이")
else:
    us_age = kr_age - 1

    while True:
        birth = int(input("생일이 지났습니까? 맞으면 0 아니면 -1 : "))
        if birth == 0 or birth == -1:
            break
        else:
            print("다시 입력해 주십시오.")

    us_age = kr_age - 1 + birth

    print('당신의 미국 나이는', us_age,'살 입니다.')


