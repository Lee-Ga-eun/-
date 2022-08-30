# 초안

from collections import deque
def solution(queue1,queue2):
    queue1=deque(queue1)
    queue2=deque(queue2)
    
    
    
    if sum(queue1)>sum(queue2):
        moving=queue1
    else:
        moving=queue2

    ave=int((sum(queue1)+sum(queue2))/2)
    #얼마를 넘겨줘야 하는지
    dif=sum(moving)-ave 
    sum_moving=sum(moving)
    suc='F'
    for i in moving:
        if sum_moving-i==dif:
            suc='T'
        sum_moving-=i
        print(sum_moving)
    if suc=='F':
        return -1
        
        
    
    
    
    return 0