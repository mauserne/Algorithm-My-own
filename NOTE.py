N, B = input().split()

N = N[::-1]

result = 0

for i in range(len(N)):
    if N[i].isalpha():
        print(N[i],'ispalpha')
        result += (ord(N[i]) - 55) * int(B) **i
    else:
        print(N[i],'is digit')
        result += int(N[i]) * int(B) **i

print(result)

print('1'.isalpha)