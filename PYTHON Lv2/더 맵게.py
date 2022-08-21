"""
매운 맛을 좋아하는 Leo는 모든 음식의 스코빌 지수를 K 이상으로 만들고 싶다.
모든 음식의 스코빌 지수를 K이상으로 만들기 위해선,

섞은 음식의 스코빌 지수= 가장 맵지 않은 음식의 스코빌 지수 + (두번째 맵지 않은 음식의 지수*2)

모든 음식의 스코빌 지수를 K 이상으로 만들기 위해 섞어야 하는 최소 횟수를 return
"""

# 런타임 에러. 매번 정렬해서 그런 거 같음 & 계산한 값을 새로운 배열에 넣어서 연산에 포함하는 코드를 작성했으나, if문이 너무 많아짐
from collections import deque
def solution(scoville,k):
    count=0
    while(True):
        first=scoville.popleft()
        second=scoville.popleft()
        
        #if first<k or second<k: #생각해보니 second<k 여부는 중요하지 않음
        if first<k:
            mix=first+second*2
            scoville.append(mix)
            count+=1
            if scoville[0]>k and mix>k: # 섞은 숫자 혹은 다음으로 계산할 값이 k보다 크면, 중단해도 됨
                break
        else:
            break
        scoville=deque(sorted(scoville)) # 시간을 조금이라도 줄이기 위해 마지막에 배치
        
        if len(scoville)==1: # 모든 걸 섞어도 k을 넘어서지 못 하는 경우엔 -1을 리턴
            if scoville[0]<k:
                return -1

    return count or 0 # [10,10,10],1과 같은 케이스는, 섞을 필요가 없으므로 0을 리턴

"""
heap 을 이용
"""
import heapq # heapify, heappush, heappop 등

def solution(scoville,k):
    heapq.heapify(scoville) # 정렬. (최소값이 최상단 노드로)
    count=0
    
    while(scoville[0]<k and len(scoville)!=1):
        mix=heapq.heappop(scoville)+heapq.heappop(scoville)*2
        heapq.heappush(scoville,mix) # 알아서 최소값이 최상단 노드로 가게끔 정렬됨
        count+=1
    
    if len(scoville)==1:
        if scoville[0]<k:
            return 0
    
    return count or -1
    
    
        
    