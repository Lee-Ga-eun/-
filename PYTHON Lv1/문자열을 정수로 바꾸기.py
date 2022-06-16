

def solution(s):
    # answer = 0
    # return answer
    if (len(s)>=1 and len(s)<=5):
        return int(s)

#다른 풀이

def solution(s):
    result=0
    
#     s는 "123"
# 음수이면 -123, 양수이면 123으로 출력
# 123= 10^0*3 + 10^1*2 + 10^2*1
# idx는 0부터 시작. 즉 1의 자리부터 돌려야 함
# s_[::-1]은 슬라이싱이며 뒤에서부터 3 2 1 임
    for idx, s_ in enumerate(s[::-1]):
        if s_=='-':
            result*=-1
        elif s_=='+':
            continue
        else:
            print(s_)
            result+=(10**idx)*int(s_)
            
    return result
        
        