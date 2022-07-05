def nbase1(n, k):
    ans = ''
    while k:
        ans += str(k % n)
        k //= n
    return ans[::-1]

print(nbase1(3,10))

def nbase2(n, k):
    ans = ''
    while k:
        ans += str(k % n)
        if n >= k:
            return ans
        k //= n
    return ans[::-1]

print(nbase2(16,23))

def nbase3(n, k):
    ans = ''
    while k:
        if k % n > 9:
            ans += chr(55 + k % n)
        else:
            ans += str(k % n)
        k //= n
    return ans[::-1]

print(nbase3(36,35))

def nbase4(n, k):
    if n > 36:
        return 'n진수가 알파벳으로 표현할 수 있는 범위를 넘었습니다. (n > 36)'

    ans = ''
    while k:
        if k % n > 9:
            ans += chr(55 + k % n)
        else:
            ans += str(k % n)
        k //= n
    return ans[::-1]

print(nbase4(36,12414))

print(int('9KU',base=36))

print(bin(10))
print(oct(10))
print(hex(10))
print(int('0xa',base=16))