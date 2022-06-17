
def solution(s):
    if len(s)%2==0:
        #짝수이면
        return s[len(s)//2-1]+s[len(s)//2]
    else:
        #홀수이면
        return s[len(s)//2]


# ---다른 풀이

def solution(s):
    return s[ (len(s)-1)//2  : len(s)//2+1  ]