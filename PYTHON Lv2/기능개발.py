"""
작업의 진도가 적힌 정수 배열 progresses는 배포되어야 하는 순서대로 배열에 저장되어 있다.
각 작업 당 하루에 작업할 수 있는 퍼센티지를 speeds 변수에 저장하였다.

어떤 기능이 먼저 완성되었더라도, 앞에 있는 모든 기능이 무조건 먼저 배포되어야만 한다

<입력 예>
progresses=[93,30,55]
speeds=[1,30,5]
<출력 예>
[2,1]
"""


from collections import deque
def solution(progresses, speeds):
    answer=[]
    days=[] # 며칠동안 작업해야 하는지
    s=0 # speeds 배열의 원소 하나하나 접근할 변수
    for i in progresses:
        cal=0 #계산 초기화
        cal=(100-i)/speeds[s] # 계산 수식 (100%-현재 작업완료 퍼센트/하루 당 가능한 작업 양)=며칠동안 해야 하는지
        if cal!=int(cal): # 계산 결과가 소수인 경우, 올림해야한다
            cal=int(cal)
            days.append(cal+1)
        else:
            days.append(int(cal))
        s+=1
    days=deque(days) # deque    
    #print(days)
    
    while(days): #deque
        amount=0 # 한 번에 몇 개가 배포되었는지. answer에 저장할 때 쓰인다
        one_day=days.popleft() # 제일 앞에 있는 수를 꺼낸다
        amount+=1
        if len(days)!=0: # days배열이 비어있지 않아야 함
            while(True):
                if days[0]>one_day: # 다음 수가 one_day보다 크다는 건, one_day와 함께 배포되지 않을 거란 뜻이다
                    break
                else: # 한꺼번에 배포될 수 있는 양을 카운트한다
                    days.popleft()
                    amount+=1
                    if len(days)==0:
                        break
            answer.append(amount)
        else:
            answer.append(amount)
            break
        print(days)
    
    return answer