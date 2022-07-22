"""
불리언배열 signs, 정수가 담긴 배열 absolutes(절대값)
true면 양수 false면 음수

입력>
signs=[true,false,true]
absolutes=[1,2,3]

출력>
2 (1+(-2)+3)
"""

#나의 풀이
def solution(absolutes, signs):
    answer=0
    for idx,absolute in enumerate(absolutes):
        if signs[idx]==bool(1): # true,false는 문자열이 아니다. 
            answer+=(absolute)
        else:
            answer+=-(absolute)
    return answer

# 다른 풀이 - zip함수 이용
def solution(absolutes, signs):
    answer=0
    for a,b in zip(absolutes,signs):
        if b: #true이면
            answer+=a
        else:
            answer+=-a
    return answer

#다른 풀이 - 
def solution(absolutes,signs):
    return sum(absolutes if sign else -absolutes for absolutes, sign in zip(absolutes,signs))