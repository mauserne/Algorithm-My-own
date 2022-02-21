"""
알파벳찾기
https://www.acmicpc.net/problem/10809
time spent : 15min
"""

s = input()

output = [-1] * 26

for i in range(len(s)):
    p = ord(s[i])-ord('a')
    if output[p] != -1:
        continue
    output[p] = i

print(' '.join(map(str,output)))