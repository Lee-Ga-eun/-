"""
모든 단어의 첫 문자가 대문자이고 그 외의 알파벳은 소문자이다
첫 문자가 숫자일 때는 그 뒤 이어지는 알파벳은 소문자로 출력한다
공백 문자가 연속해서 나올 수 있다
"""

#나의 풀이
def solution(s):
    s=s.lower()
    s=s.lstrip()
    s=s.split(" ")
    answer=[]
    for i in s:
        if i=="":
            answer.append("")
            continue
        if i[0].isdigit():
            answer.append(i)
        else:
            k=chr(ord(i[0])-32)
            i=k+i[1::]
            answer.append(i)
    
    return " ".join(answer)

#정답 풀이는 아니지만, 새로 알게된 title()함수

"""
"abc".title()의 결과: "Abc"
"""