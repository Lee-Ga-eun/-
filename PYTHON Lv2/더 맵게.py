"""
매운 맛을 좋아하는 Leo는 모든 음식의 스코빌 지수를 K 이상으로 만들고 싶다.
모든 음식의 스코빌 지수를 K이상으로 만들기 위해선,

섞은 음식의 스코빌 지수= 가장 맵지 않은 음식의 스코빌 지수 + (두번째 맵지 않은 음식의 지수*2)

모든 음식의 스코빌 지수를 K 이상으로 만들기 위해 섞어야 하는 최소 횟수를 return
"""

# 런타임 에러. 매번 정렬해서 그런 거 같음
from collections import deque
def solution(scoville,k):
    count=0
    while(True):
        scoville=deque(sorted(scoville))
        first=scoville.popleft()
        second=scoville.popleft()
        
        if first<k or second<k:
            mix=first+second*2
            scoville.append(mix)
            count+=1
        else:
            break
    return count or -1
        
    