"""
최고의 피자
https://codeup.kr/problem.php?id=3321
time spent : 58min
"""

n = int(input())
a,b = map(int,input().split())
c = int(input())

tplist = [0]
for _ in range(n):
    toping = int(input())
    tplist.append(toping)


caloriesum = sum(tplist) + c
tplist.sort()

pricesum = b*n +a
cdlist = [c//a, (caloriesum) //(pricesum)]
for i in range(1,n+1):
    caloriesum -= tplist[i]
    cdlist.append((caloriesum) // (pricesum - i*b)) 

print(max(cdlist))
