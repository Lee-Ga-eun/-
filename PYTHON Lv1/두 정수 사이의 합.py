"""
주어진 a,b 사이의 합 구하기. (a와 b의 대소관계는 정해지지 않음)
"""

# 나의 풀이

def solution(a,b):
    
    answer=0 
    
    if a>b:
        tmp=b
        b=a
        a=tmp
    
    for i in range(a,b+1):
        answer+=i
    
    return answer

# 다른 풀이 1

def solution(a,b):
    answer= (a+b)*(abs(b-a)+1)//2
    return answer

# 다른 풀이2
del sum # 어딘가에서 sum이란 변수를 썼다면. 
def solution(a,b):
    if a>b: a,b = b,a
    
    return sum(range(a,b+1))

# 다른 풀이3
def solution(a,b):
    return sum(range(min(a,b),max(a,b)+1))
