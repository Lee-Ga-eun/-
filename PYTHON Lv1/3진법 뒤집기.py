"""
<입력>
n(10진법) = 45
<과정>
n을 3진법으로 = 1200
앞뒤 반전 = 0021
<출력>
10진법으로 표현 = 7
"""

#나의 풀이

def solution(n):
    r=[]
    if n<3: return n
    while(True):
        r.append(n%3)
        n=n//3
        if n<3:
            r.append(n)
            break
    n=0
    k=len(r)-1
    for i in r:
        n+=i*(3**k)
        k-=1
    return n

