"""
ROT13
https://www.acmicpc.net/problem/11655
time spent : 23 min
"""

s = input()

output = ''
for i in s:
    if i.isupper():
        if chr(ord(i) + 13).isupper():
            output += chr(ord(i) + 13)
        else:
            output += chr(ord(i) - 13)
    elif i.islower():
        if chr(ord(i) + 13).islower():
            output += chr(ord(i) + 13)
        else:
            output += chr(ord(i) - 13)

    else:
        output += i
print(output)