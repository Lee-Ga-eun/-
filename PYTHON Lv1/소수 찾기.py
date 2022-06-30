# 주어진 숫자까지 소수의 개수를 찾는다

# 알아야할 개념:> 에라토스테네스의 체

#풀이1
import math
def solution(n):
    
    arr=[True]*(n+1)
    arr[0]=False # 0은 소수가 아니다
    arr[1]=False # 1은 소수가 아니다
    
    for i in range(2,int(math.sqrt(n))+1):
        if arr[i]==True:
            j=2
            while(i*j)<=n:
                arr[i*j]=False
                j+=1
    return arr.count(True)
        

