"""
-2μ§μ
https://www.acmicpc.net/problem/2089
"""

#νμ΄π
#-2μ§μλ‘ λ³ννκ³ μ νλ κ° nμ μλ ₯λ°λλ€.
#nμ΄ -2λ‘ λλμ΄ λ¨μ΄μ§μ§ μλ κ²½μ°μλ κ²°κ³Όκ°μ 1μ λΆμ΄κ³  μμκ° μλ λͺ«μ κ΅¬νκΈ° μν΄ n//-2μ 1μ λνλ€.
#nμ΄ -2λ‘ λλμ΄ λ¨μ΄μ§λ κ²½μ°μλ κ²°κ³Όκ°μ 0μ λΆμ΄κ³  n//-2μ μννμ¬ nμ μ΄κΈ°ννλ€.
#
n = int(input())
res =''
if n == 0:
    print(0)
    exit()
while n:
    if n % (-2):
        res = '1' + res
        # -2λ‘ λλμ΄ λ¨μ΄μ§μ§ μλ κ²½μ° λͺ«μ κ΅¬νκΈ° μν΄ 1μ λν¨
        n = n//-2 + 1
    else:
        res = '0' + res
        n = n//-2
    print(n)

print(res)