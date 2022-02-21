"""
알파벳 개수
https://www.acmicpc.net/problem/10808
"""

s = input()

output = [0]*26

for i in s:
    output[ord(i) - ord('a')] += 1

print(' '.join(map(str,output)))
