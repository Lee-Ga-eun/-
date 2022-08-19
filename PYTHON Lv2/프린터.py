"""
priorities 배열이 주어지면, 하나씩 순서대로 A,B,C... 문서라고 생각하면 된다.
priorities 배열의 숫자들은 우선순위이다. 우선순위는 1~9이며, 높은 순서가 높은 우선순위를 지닌다
location은 내가 알고 싶은 문서이며, 그 문서의 최종 출력 차례를 return 하면 된다

<입력>
priorities: [2,1,3,2]
location: 2

<출력>
return: 1
"""

# 나의 풀이 (큐 이용)
from collections import deque
def solution(priorities, location):
    answer=[]
    k=65 #알파벳을 포함한 배열을 만들기 위해서이다. 아스키코드 이용
    for i, j in enumerate(priorities):
        answer.append((j,chr(i+k))) #[(2, 'A'), (1, 'B'), (3, 'C'), (2, 'D')]   
    priorities=deque(answer) # 큐를 이용하기 위해서
    l=priorities[location] # return값 출력을 위해서
    answer=[] # 재활용을 위한 초기화
    while(priorities):
        M=max(priorities)[0] #배열의 최댓값 
        
        while(True):
            if priorities[0][0]==M: #가장 앞에 있는 문서가 최대값이라면
                break # 뒤로 보낼 필요 없음
            else: 
                p=priorities.popleft() #그렇지 않다면
                priorities.append(p) #뒤로 보내야 함
        
        p=priorities.popleft() # 최대값 해결했으므로 최종 출력 순서를 나타내는 answer에 대입할 것임
        answer.append(p) # 한 번만 해결하는 게 아닌, 전체적인 우선순위를 파악해 출력해야 하기 때문에 반복한다

    return answer.index(l)+1 # 내가 알고 싶은 문서의 위치

    """
    알파벳을 포함한 배열 내 원소들의 순서를, 숫자가 먼저 오게 한 이유:
    Max 값을 위해서이다.
    [(2, 'A'), (1, 'B'), (3, 'C'), (2, 'D')]  여기서 Max값은 (3,'C')인데(큰 숫자=최대값),
    [('A', 2), ('B', 1), ('C', 3), ('D', 2)] 이 경우 Max 값은 ('D',2)이다. (알파벳이 큰 것=최대값)
    """