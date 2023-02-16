"""
# 자카드 유사도 #
: 원소의 중복을 허용하는 다중집합

A= 원소 1을 3개 갖고 있음
B= 원소 1을 5개 갖고 있음

다중합집합= max(3,5)
다중교집합= min(3,5)

"""

"""
문제: 문자열이 주어졌을 떄 두 글자씩 끊어서 다중집합을 만들 수 있다
자카드유사도는 다중교집합/다중합집합*65536 으로 계산한다
단 두 글자씩 끊을 때, 두 글자 모두 영어가 아니라면 그 쌍은 버린다
대소문자 구분은 없다
"""

# 다중집합 풀이

# 다중교집합 = set()&set() ==> 문자열 for문 탐색, 한 글자씩 탐색해서 count (각 글자수 세기) -> min(문자열1에 있는 특정 문자 i의 개수, 문자열2에 있는 특정 문자 i의 개수)
# 다중합집합 = set()|set() --> 문자열 for문 탐색, 한 글자씩 탐색해서 count(각 글자 수 세기) -> max(문자열1에 있는 특정 문자 i의 개수, 문자열2에 있는 특정 문자 i의 개수)

#적용 풀이 (내가 푼 거 X)
import re
import math

def solution1(str1, str2):
    str1 = [str1[i:i+2].lower() for i in range(0, len(str1)-1) if not re.findall('[^a-zA-Z]+', str1[i:i+2])]
    str2 = [str2[i:i+2].lower() for i in range(0, len(str2)-1) if not re.findall('[^a-zA-Z]+', str2[i:i+2])]

    gyo = set(str1) & set(str2)
    hap = set(str1) | set(str2)

    if len(hap) == 0 :
        return 65536

    gyo_sum = sum([min(str1.count(gg), str2.count(gg)) for gg in gyo])
    hap_sum = sum([max(str1.count(hh), str2.count(hh)) for hh in hap])

    return math.floor((gyo_sum/hap_sum)*65536)

answer1= solution1('FRENCH','french')
print(answer1)



#내 풀이, copy 이용
# set()은 원소 중복을 허용하지 않기 때문이다
# 사실상 다중 집합은, 수학으로 알고 있는 합집합, 교집합 개념이다

def solution2(str1,str2):
    
    def check(st,arr):
        for i in range(len(st)):
            tmp=st[i:i+2].lower()
            if len(tmp)==2 and (ord(tmp[0]) not in range(97,122) or ord(tmp[1]) not in range(97,122)):
                print(tmp)
                continue
            else:
                if len(tmp)==2:
                    arr.append(''.join(tmp))
    s1=[]
    check(str1,s1) # 다중집합 결과 출력    
    s2=[]
    check(str2,s2) # 다중집합결과출력
    
    a1=s1.copy()
    a2=s1.copy()
    
    for i in s2:
        if i not in a1:
            a2.append(i)
        else:
            a1.remove(i)
    print("다중 합집합",a2)
    
    common=[]
    for i in s2:
        if i in s1:
            s1.remove(i)
            common.append(i)
    print("다중 교집합",common)
    
    if len(a2)>=1 and len(common)>=1:
        return int(len(common)/len(a2)*65536)
    return 65536

answer2=solution2('E=M*C^2','e=m*c^2')
print(answer2)
