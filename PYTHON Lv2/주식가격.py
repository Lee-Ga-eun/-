"""
초 단위로 기록된 주식 가격이 담긴 배열 prices가 매개변수로 주어질 때, 가격이 떨어지지 않은 기간은 몇 초인가

<입력>
prices= [1,2,3,2,3]
<출력>
[4,3,1,1,0]

**
1초 시점의 $1은 끝까지 가격이 떨어지지 않는다
2초 시점의 $2는 끝까지 가격이 떨어지지 않는다
3초 시점의 $3은 1초 뒤에 가격이 2로 떨어진다
4초 시점의 $2는 끝까지 가격이 떨어지지 않는다
5초 시점의 $3은 0초간 가격이 떨어지지 않는다
"""
#나의 풀이

from collections import deque

def solution(prices):
    
    prices=deque(prices)
    down=-1
    answer=[]
    
    while prices:
        down=-1
        for i in prices:
            if prices[0]>i:
                down=prices.index(i)
                break

        if down>0:
            answer.append(down)
        else:
            answer.append(len(prices)-1)

        prices.popleft()
        # 아래의 코드가 필요하지 않은 이유는, 위의 else문 때문이다. 1-1=0 (마지막 수만 남았을 경우)
        """
        if len(prices)==1:
            answer.append(0)
            break
        """
    
    return answer
    