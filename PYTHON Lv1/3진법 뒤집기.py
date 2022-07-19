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

#풀이2
def solution(n):
    remainder=''
    while n:
        remainder+=str(n%3)
        n=n//3

    answer=int(remainder,3)
    return answer

    # int(string,3)
    # 단, str(0012)에선, 
    # leading zeros in decimal integer literals are not permitted;이라는 에러가 뜬다
    
