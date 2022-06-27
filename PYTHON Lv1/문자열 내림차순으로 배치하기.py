"""
영문 대소문자로만 구성되어 있는 문자열 s에 대하여
문자를 큰 것부터 작은 순으로 정렬해 리턴
단, 대문자는 소문자보다 작다

s: "Zbcdefg"
return: "gfedcbZ"
"""
def solution(s):
    #s=list(s) # 문자열을 리스트로 바꿈
    s=[ord(i) for i in s ]
    s.sort(reverse=True) # 아스키코드로 문자열을 바꾼 것을 리스트에 담는다
    answer=""
    for i in s: 
        answer+=chr(i)
    return answer