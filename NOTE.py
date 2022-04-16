h, m = map(int, input().split())
c = int(input())

rm = m+c

m = rm % 60
h += rm//60

if h > 23:
    h -= 24

print(h,m)