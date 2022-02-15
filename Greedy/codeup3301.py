"""
거스름돈
https://codeup.kr/problem.php?id=3301&rid=0

time spent : 7mins
"""

a = int(input())
count = 0

for i in [50000, 10000, 5000, 1000, 500, 100, 50, 10]:
    if a // i != 0 :
        count += a // i
        a = a % i

print(count)
