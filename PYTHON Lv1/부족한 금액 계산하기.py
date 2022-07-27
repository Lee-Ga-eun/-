"""
이용료 price원
N번째 이용 --> 이용료의 N배

놀이기구를 count번 타게 되면 현재 자신이 갖고 있는 금액에서 얼마나 모자라는지.
모자라지 않으면 0
"""

# 나의 풀이
def solution(price, money, count):
    result=sum([price*i for i in range(1,count+1)])
    if money-result<0:
        return result-money
    return 0
   
   # result 변수로 메모리를 사용

# 다른이의 풀이

def solution(price, money, count):
    return max(0,price*(count+1)*count//2-money) 
    #이 문제를 등차수열로 접근했다. 등차수열의 합 공식을 사용하였음
    # 금액이 모자라지 않다면, 음수가 나올 것이다
    