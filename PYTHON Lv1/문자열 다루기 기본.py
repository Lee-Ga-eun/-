"""
주어진 문자열이 모두 숫자로 이루어져있다면 True 출력, 그렇지 않다면 False 출력
문자열의 길이는 4또는 6이다
"""

#1. 나의 풀이

def solution(s):
    if len(s)==4 or len(s)==6:
        if s.isdigit(): return True
        else: return False
    else: return False

#2. 다른 풀이: isdigit() 함수는 True/False를 반환한다

def alpha_string46(s):
    return s.isdigit() and len(s) in (4, 6)

#3. 다른 풀이: ==. >= 등 비교구문은 True/False를 반환한다
def alpha_string46(s):
    try:
        int(s)
    except:
        return False
    return len(s) == 4 or len(s) == 6 
        # True/False를 반환함
        # True or False => True
        # False or False => False
        # True or True => True

#4. 다른 풀이. bool 함수 이용
def alpha_string46(s):
    import re
    return bool(re.match("^(\d{4}|\d{6}$",s))

