"""
파일명에 포함된 숫자를 반영한 정렬 기능을 구현한다
<파일명 형태: foo9.txt , foo010bar020.zip, F-15 등>
HEAD는 숫자가 아닌 문자로 이루어져 있으며, 최소한 한 글자 이상이다.
NUMBER는 한 글자에서 최대 다섯 글자 사이의 연속된 숫자로 이루어져 있으며, 앞쪽에 0이 올 수 있다. 0부터 99999 사이의 숫자로, 00000이나 0101 등도 가능하다.
TAIL은 그 나머지 부분으로, 여기에는 숫자가 다시 나타날 수도 있으며, 아무 글자도 없을 수 있다.

1. HEAD 기준 사전 순 정렬, 대소문자 구분 없음
2. HEAD가 같으면 number로 정렬
3. head와 number이 같으면, 주어진 배열 순서 유지
"""

def solution(files):
    import re
    tmp=[]
    for i in range(len(files)):
        text=files[i]
        regex = re.compile("\d+") #숫자가 하나 이상이어야함
        number = regex.findall(text)[0] # 숫자 추출
        head=text[:text.index(number)] # 그 앞 문자 추출
        tail=text.index(number)+len(str(number))
        #print(text[for_tail:])
        #tail=text[text.index(number[:-1]):]
        tmp.append((head,number,text[tail:]))
        
    answer=[]
    """
    tmp: [('img', '12', '.png'), ('img', '10', '-png'), ('img', '02', '.png'), ('img', '1', '.png'), ('IMG', '01', '.GIF'), ('img', '2', '.JPG')]
    """
    tmp.sort(key=lambda x:(x[0].lower(), int(x[1]))) ########## 중요
    for i in range(len(tmp)):
        answer.append(''.join(tmp[i]))
    return answer

s=solution(["img12.png", "img10-png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"])
print(s)


"""
<추가, 숫자문자의 대소비교>

 - "9" 가 "12"보다 크다고 판단한다. 이게 바로 정수가 아닌 문자열에서의 차이점이다. 해당 문자열의 길이에 상관없이 무조건 앞에 자리수부터 대소 비교를 한다.
 - "129" vs "12": 짧은 길이 문자열과 전부 동일한 앞자리를 가졌기 때문에 길이가 더 긴 129가 크다고 판별한다.
"""