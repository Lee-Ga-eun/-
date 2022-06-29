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

    """
    테스트 1 〉	통과 (0.01ms, 10.1MB)
    테스트 2 〉	통과 (0.02ms, 10.3MB)
    테스트 3 〉	통과 (0.02ms, 10.1MB)
    테스트 4 〉	통과 (0.01ms, 10.1MB)
    테스트 5 〉	통과 (0.01ms, 10.3MB)
    테스트 6 〉	통과 (0.03ms, 10.3MB)
    테스트 7 〉	통과 (0.02ms, 10MB)
    테스트 8 〉	통과 (0.02ms, 10.2MB)
    테스트 9 〉	통과 (0.03ms, 10.1MB)
    테스트 10 〉	통과 (0.02ms, 10.3MB)
    테스트 11 〉	통과 (0.05ms, 10.3MB)
    테스트 12 〉	통과 (0.06ms, 10.2MB)
    테스트 13 〉	통과 (4.80ms, 10.1MB)
    """

def solution2(s,n):
    answer=""
    for i in s:
        if i.isupper(): #대문자라면
            answer+=chr((ord(i)-ord('A')+n)%26+ord('A'))
        elif i.islower(): #소문자라면
            answer+=chr((ord(i)-ord('a')+n)%26+ord('a'))
        else:
            answer+=" "
    
    return answer

def solution3(s,n):
    s=list(s)
    for i in range(len(s)):
        if s[i].isupper():
            s[i]=chr((ord(s[i])-ord('A')+n)%26+ord('A'))
        elif s[i].islower():
            s[i]=chr((ord(s[i])-ord('a')+n)%26+ord('a'))
    
    return "".join(s)

    """
    테스트 1 〉	통과 (0.01ms, 10.1MB)
    테스트 2 〉	통과 (0.01ms, 10.1MB)
    테스트 3 〉	통과 (0.01ms, 10.2MB)
    테스트 4 〉	통과 (0.01ms, 10.1MB)
    테스트 5 〉	통과 (0.01ms, 10.2MB)
    테스트 6 〉	통과 (0.01ms, 10.2MB)
    테스트 7 〉	통과 (0.02ms, 10.2MB)
    테스트 8 〉	통과 (0.01ms, 10.1MB)
    테스트 9 〉	통과 (0.03ms, 10.3MB)
    테스트 10 〉	통과 (0.01ms, 10.3MB)
    테스트 11 〉	통과 (0.02ms, 10.4MB)
    테스트 12 〉	통과 (0.02ms, 10.1MB)
    테스트 13 〉	통과 (2.02ms, 10.2MB)
    """