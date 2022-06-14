"""
"수박수박수박수.."와 같은 같은 패턴을 유지하는 문자열을
n까지 출력. 
ex n=5이면 수박수박수
   n=4이면 수박수박
"""

# 나의 풀이
# "수박"*5000를 하면서, 비효율적인 메모리를 사용함

def solution(n):
    수와박="수박"*5000
    l=list(수와박)
    answer=''.join(map(str,l[0:n]))

    return answer

#다른 풀이
# '수박'*n 을 하면서 비효율적 메모리를 사용

def solution(n):
    s='수박'*n
    return s[:n]

""" 
효율적으로 메모리를 쓰기
"""

def solution(n):
    s='수박'*(n//2 + n%2) 
    # 어차피 두 글자로, 나머지가 0 아니면 1.
    # s='수박'*(n//2+1)
    return s[:n]


def solution(n):
    return ("수박"*(n//2+1))[0:n]

"""
Ex
'수박수박수박수박'[0:2] ==> '수박'

"""