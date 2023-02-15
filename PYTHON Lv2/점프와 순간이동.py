"""
한 번에 K칸 앞으로 점프: K만큼 건전지 사용
순간이동: 건전지 불필요

최소한의 건전지 사용으로 목적지에 도착

도착지점 N: 1 이상 10억 이하 자연수
"""

# dp 풀이: 정확성 100, 효율성 0 
# 아무래도 0부터 N까지 dp 테이블을 저장하기엔, 10억까지라는 숫자 조건에서 효율성이 떨어지는 거 같다

def solution1(N):
    
    from collections import deque
    d=deque()
    d.append(0)
    d.append(1)
    d.append(1)
    
    for i in range(3,N+1):
        if i%2==0:
            d.append(d[i//2])
        else:
            d.append(min(d[i//2]+1,d[i-1]+1))    
    
    return d[N]

answer=solution1(5)
print(answer)


# 풀이 2
def solution2(N):
    
    answer=0
    i=N
    for _ in range(i,0,-1):
            if i%2==0:
                i=i//2
            else:
                answer+=1
                i-=1
            if i==0:
                break
    
    return answer

answer2=solution2(5)
print(answer2)