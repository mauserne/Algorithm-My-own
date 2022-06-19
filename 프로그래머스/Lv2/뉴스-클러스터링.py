from collections import Counter

def solution(str1, str2):
    str1, str2 = str1.upper(), str2.upper()
    arr1, arr2 = [], []
    
    for i in range(1,len(str1)):
        if str1[i-1].isalpha() and str1[i].isalpha():
            arr1.append(str1[i-1] + str1[i])
    for i in range(1,len(str2)):
        if str2[i-1].isalpha() and str2[i].isalpha():
            arr2.append(str2[i-1] + str2[i])
    
    
    counter1 = Counter(arr1)
    counter2 = Counter(arr2)
    
    inter = list((counter1&counter2).elements())
    union = list((counter1|counter2).elements())

    if len(union) == 0 and len(inter) == 0:
        return 65536
    else:
        return int(len(inter) / len(union) * 65536)

print(solution("aa1+aa2","AAAA12"))