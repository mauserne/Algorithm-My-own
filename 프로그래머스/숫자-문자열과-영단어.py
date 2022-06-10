from re import U


def solution(s):
    arr = ['zero','one','two','three','four','five','six','seven','eight','nine']
    for i in range(10):
        s = s.replace(arr[i],str(i))
        print(s)
    return int(s)

print(solution("one4seveneight"	))