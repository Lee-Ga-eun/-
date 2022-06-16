"""
String 배열(seoul)에서 Kim(무조건 들어있음)을 찾아 반환
seoul에 "Kim"은 오직 한 번만 나타난다
"""

def solution(seoul):
    #배열의 위치 알아내기. 한 번만 나타남: index() 사용
    #seoul.index('Kim') #Kim은 seoul 배열 안에 반드시 되어 있음
    #answer = ''
    return '김서방은 '+ str(seoul.index('Kim')) +'에 있다'


#다른 풀이
def solution(seoul):
    return "김서방은 {}에 있다".format(seoul.index('Kim'))

#풀이2
def solution(seoul):
    return ('김서방은 %d에 있다'%seoul.index('Kim'))

def solution(seoul):
    return f"김서방은 { seoul.index('Kim') }에 있다"

    # "seoul.index("Kim")으로 하면 출력되지 않음. 왜?

    # -------> 김서방 앞의 "와 K 앞의 "가 묶이기 때문이다

#풀이3
def solution(seoul):
    return '김서방은 {0}에 있다'.format(seoul.index('Kim'))

#풀이4
def solution(seoul):
    return '김서방은 {n}에 있다'.format(n=seoul.index('Kim'))
