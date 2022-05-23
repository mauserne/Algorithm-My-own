import collections


def solution(partc, arch):
    answer = collections.Counter(partc) - collections.Counter(arch)
    print(11,answer[partc[3]])
    for key, val in collections.Counter(partc).items():
        print(123,key,val)

    return answer

print(solution(["mislav", "stanko", "mislav", "ana"],["stanko", "ana", "mislav"]))
