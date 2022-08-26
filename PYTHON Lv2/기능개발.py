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

# 나의 풀이
from collections import deque
import math
def solution(progresses, speeds):
    answer=[]
    days=[] # 며칠동안 작업해야 하는지
    s=0 # speeds 배열의 원소 하나하나 접근할 변수
    for i in progresses:
        cal=0 #계산 초기화
        cal=(100-i)/speeds[s] # 계산 수식 (100%-현재 작업완료 퍼센트/하루 당 가능한 작업 양)=며칠동안 해야 하는지
        days.append(math.ceil(cal))
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

# zip과
# 음수에서의 나눗셈을 이용한, 다른 이의 풀이

def solution(progresses, speeds):
    Q=[]
    for p,s in zip(progresses, speeds):
        #  17/3=  5.666666
        # -17//3= -6
        # -17/3=  -5.666666
        if len(Q)==0 or Q[-1][0]<-((p-100)//s): # popleft()한 것처럼 우선 젤 앞에 것을 빼고, 앞 기능의 개발이 끝났을 때
            Q.append([-((p-100)//s),1])
        else: # 앞 기능이 뒷 기능보다 개발이 더 남았을 때
            Q[-1][1]+=1 
    
    return [q[1] for q in Q]

    """
    Q: [[5, 1], [10, 1]]
    Q[-1][1]: 1
    Q: [[5, 1], [10, 2]]
    Q[-1][1]: 2
    Q: [[5, 1], [10, 3], [20, 1]]
    Q[-1][1]: 1


Out[145]: [1, 3, 2]
    
    """