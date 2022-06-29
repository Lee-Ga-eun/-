# 어떤 문장의 각 알파벳을 일정한 거리만큼 밀어서 다른 알파벳으로 바꾼다
"""
입출력 예:
"AB",1 ===> "BC"
"z",1 ====> "a"
"a B z", 4 ===> e F d
"""
# 나의 풀이
def solution(s,n):
    a=[chr(i) for i in range(97,123)] #소문자 배열 
    A=[chr(i) for i in range(65,91)] #대문자 배열
    answer=""
    for i in s:
        if i in a:
            answer+=a[(ord(i)-97+n)%len(a)]
        elif i in A:
            answer+=A[(ord(i)-65+n)%len(A)]
        else:
            answer+=" "
    return answer