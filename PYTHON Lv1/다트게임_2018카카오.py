"""
>다트 게임은 총 3번의 기회로 구성된다.
>각 기회마다 얻을 수 있는 점수는 0점에서 10점까지이다.
>점수와 함께 Single(S), Double(D), Triple(T) 영역이 존재하고 각 영역 당첨 시 점수에서 1제곱, 2제곱, 3제곱 (점수1 , 점수2 , 점수3 )으로 계산된다.
>옵션으로 스타상(*) , 아차상(#)이 존재하며 스타상(*) 당첨 시 해당 점수와 바로 전에 얻은 점수를 각 2배로 만든다. 아차상(#) 당첨 시 해당 점수는 마이너스된다.
>스타상(*)은 첫 번째 기회에서도 나올 수 있다. 이 경우 첫 번째 스타상(*)의 점수만 2배가 된다. (예제 4번 참고)
>스타상(*)의 효과는 다른 스타상(*)의 효과와 중첩될 수 있다. 이 경우 중첩된 스타상(*) 점수는 4배가 된다. (예제 4번 참고)
>스타상(*)의 효과는 아차상(#)의 효과와 중첩될 수 있다. 이 경우 중첩된 아차상(#)의 점수는 -2배가 된다. (예제 5번 참고)
>Single(S), Double(D), Triple(T)은 점수마다 하나씩 존재한다.
>스타상(*), 아차상(#)은 점수마다 둘 중 하나만 존재할 수 있으며, 존재하지 않을 수도 있다.
"""

#나의 풀이(실패)
"""
...
나는 split으로 문자를 기준으로 나누어 계산하려 했으나,
replace가 복잡했다.
코드를 완성시키지 못 했지만, 내가 풀려고 한 의도는..
"""
    #1. S,D,T에 따라 앞 수를 먼저 계산한다. (두자리 수인 10 처리 실패)
answer=""
for i in range(len(dartResult)):
    if dartResult[i]=="S":
        answer+=str(int(dartResult[i-1])**1)
    elif dartResult[i]=="D":
        answer+=str(int(dartResult[i-1])**2)
    elif dartResult[i]=="T":
        answer+=str(int(dartResult[i-1])**3)
    elif dartResult[i]=="*" or dartResult[i]=="#":
        answer+=(dartResult[i])

    #2. * 이 있으면, 앞의 두 숫자를 2배 한다
ind=answer.index("*") # *의 위치 찾기
d=answer[ind::-1]
if ind-3<=0:
    d=answer[ind::-1]
else:
    d=answer[ind:ind-3:-1]

for j in d:
    if j.isdigit():
            tmp=str(int(j)*2)
            answer=answer.replace(j,tmp,1)
            answer=answer.replace('*','',1)

    #3. #이 있으면 앞의 수에 -를 붙인다 >> 실패.

    # 없는 문자를 Index에서 찾으려고 하면, substring not found 에러가 출력된다




    