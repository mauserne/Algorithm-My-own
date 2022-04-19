#https://mxxcode.tistory.com/entry/%EB%B0%B1%EC%A4%80-11729-%ED%95%98%EB%85%B8%EC%9D%B4-%ED%83%91-%EC%9D%B4%EB%8F%99-%EC%88%9C%EC%84%9C-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%ED%92%80%EC%9D%B4

n = int(input())


# a 시작기둥, b 보조기둥, c 도착기둥
def hanoi(n, a, b, c):
    if n == 1:
        print(a, c)
    else:
        hanoi(n-1, a, c, b) # a 기둥에서 출발해, c기둥을 보조로 삼아, b 기둥에 쌓기
        print(a, c) # 시작기둥에 한개 남은 고리를 c기둥에 넣기
        hanoi(n-1, b, a, c) # b 기둥에 쌓여있던 고리들을 a를 거쳐 c로 쌓기

sum = 2**n - 1
print(sum)

hanoi(n, 1, 2, 3)