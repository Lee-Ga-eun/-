"""
* 다리에는 트럭이 최대 bridge_length대 올라갈 수 있으며, 다리는 weight 이하까지의 무게를 견딜 수 있다.
1초당 1 length 움직일 수 있고, 대기트럭에 있는 순서대로 움직인다

<입력>
bridge_length=2
weight=10
truck_weights=[7,4,5,6]
<출력>
return 8

<입력>
bridge_length=100
weight=100
truck_weights=[10]
<출력>
return 101
"""

#나의 풀이(실패)
from collections import deque
def solution(bridge_length, weight, truck_weights):
    # bridge length는 트럭이 올라갈 수 있는 최대 개수이다
    # weight는 다리가 견딜 수 있는 무게이다
    # truck_weights는 다리를 건너고자 하는 각 트럭의 무게들이다
    cnt=0 # 경과시간 카운트
    waiting_trucks=deque([i for i in truck_weights]) #대기트럭을 큐로 변환: deque([7,4,5,6])
    #waiting_trucks.popleft(): 7
    # .append와 .popleft()사용을 위해서
    on_bridge=deque() # 다리에 있는 트럭
    passed_truck=[] # 다리를 지난 트럭
    
    if bridge_length>=sum(truck_weights):
        print("뇸")
        cnt=-1
        
    l=0 # 가장 앞에 있는 차가, 나갈 차례인지 아닌지를 파악하게 한다
    while(True):
        
        if waiting_trucks!=deque([]):
            l+=1
            if sum(on_bridge)+waiting_trucks[0]<=weight:
                on_bridge.append(waiting_trucks.popleft())
        
        
        #***********************************
        while(len(waiting_trucks)>=1):
        
            #if len(on_bridge)==bridge_length or sum(on_bridge)+waiting_trucks[0]>weight:
            if l==bridge_length and sum(on_bridge)+waiting_trucks[0]>weight:
                passed_truck.append(on_bridge.popleft())
                l=len(on_bridge) # 들어와있던 트럭에게 번호 부여

                
            break
            
        #*************************************
        print("지난 트럭",passed_truck)
        print("다리 위",on_bridge)
        print("대기트럭",waiting_trucks)
        print("--------")


        
        cnt+=1


        if waiting_trucks==deque([]):
            cnt+=bridge_length+1
            break


            
    return cnt
    
# 다른 풀이
from collections import deque

def solution(bridge_length, weight, truck_weights):
    queue = deque([0]*bridge_length) #deque([0,0])
    print(queue)
    orders = deque(truck_weights)
    time=0
    total=0
    while orders: #popleft()로 인해 결국 비게 될 것이므로
        time+=1
        print(total,"-",queue[0])
        total -= queue[0]
        queue.popleft()
        if total + orders[0] > weight:
            queue.append(0) #무게가 0인 트럭 넣기
            #[0,0] 혹은 [7,0] 등
        else:
            w = orders.popleft() #다리 위로 올라감
            total+=w
            queue.append(w)
            #[0,7] 혹은 [5,4] 같은 식
            print(queue)

    return time+bridge_length # orders가 비면 끝나기 때문에