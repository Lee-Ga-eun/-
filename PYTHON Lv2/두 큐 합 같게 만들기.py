# 초안 -> Cancle

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


# 더 쉽게 접근하기
# 계속 sum을 해줘야한다고 생각했으나, 그렇지 않음

from collections import deque

def solution(queue1, queue2):
    queue1=deque(queue1)
    queue2=deque(queue2)
    sum_queue1=sum(queue1)
    sum_queue2=sum(queue2)

    for i in range(len(queue1)*3): #queue2과 queue1의 길이는 동일하다. popleft와 append가 수행되므로, 넉넉하게 길이를 잡아준다
        if sum_queue1==sum_queue2: # 합이 같으면
            return i # 몇 번 수행되었는지 == popleft, popleft된 수의 개수
        if sum_queue1>sum_queue2: #queue1의 합이 더 크면
            num=queue1.popleft() # queue1에서 가장 앞 수를 빼서 queue2에 넣는다
            queue2.append(num)
            sum_queue1-=num # 굳이 모든 수를 더하지 않아도 된다
            sum_queue2+=num
        else: #queue2가 더 클 때
            num=queue2.popleft()
            queue1.append(num)
            sum_queue1+=num
            sum_queue2-=num
    return -1 # 합이 도저히 같지 않을 때