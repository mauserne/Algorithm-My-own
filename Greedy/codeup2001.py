"""
최소 대금
https://www.codeup.kr/problem.php?id=2001

time spent : 10min
"""

pasta = []
for _ in range(3):
    a = int(input())
    pasta.append(a)

juice = []
for _ in range(2):
    b = int(input())
    juice.append(b)
result = (min(pasta) + min(juice))*1.1
print("%.1f" %result)