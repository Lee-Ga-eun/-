# 롤케이크를 반으로 나누었을 때 토핑의 가짓수가 동일해야 한다

def solution(topping):
    from collections import Counter
    toppings=Counter(topping) # for문으로 돌리지 말고 무조건 Counter 쓰기. 실행 속도 차이가 큼
    new=set()
    count=0

    while(topping):
        
        popping=topping.pop() # 하나 제거
        new.add(popping) # 하나 추가

        if toppings[popping]>1:
            toppings[popping]-=1
        else:
            del toppings[popping] # 카운팅하는 딕셔너리 키 지우기
            
        if len(toppings)==len(new):
            count+=1
        
    return count