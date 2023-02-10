"""
S = baabaa 라면

b aa baa → bb aa → aa →

의 순서로 문자열을 모두 제거할 수 있으므로 1을 반환
"""

def solution(s):
    stack=[]
    stack.append(s[0])

    for i in range(1,len(s)):
        if len(stack)!=0 and s[i]==stack[-1]:
            stack.pop()
        else:
            stack.append(s[i])
    if len(stack)==0:
        return 1
    else:
        return 0

answer=solution('aabbac')
print(answer)