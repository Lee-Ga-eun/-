"""
높이가 19,14,10,17 cm인 떡이 나란이 있다고 할 때,
절단기 기준을 15로 한다면
손님이 가져가는 떡의 길이는 (19-15) + 0 + 0 + (17-15) = 6cm이다

손님이 원하는 떡의 길이가 주어질 때, 절단기의 최대 높이를 설정한다
"""

def tteock(amount, request, tteocks, start ,end):
    
    # 절단기 높이 설정을 중간값으로 한다
    if start>end:
        return None
    mid=(start+end)//2 # 중간값 설정
#     setting=tteocks[mid]
    
    # 각각 뺀 값의 합이 요청보다 크면 절단기 높이를 높이고
    # 요청보다 작으면 절단기 높이를 낮추고
    # 합이 같으면 리턴한다
#     print(setting)
#     print([(i-setting) for i in tteocks if setting<i ])
    sums=sum([(i-mid) for i in tteocks if mid<i ])
    if sums==request:
        return mid
    
    if sums<request: # 요청보다 잘린 게 적으면
        return tteock(amount,request,tteocks, start,mid-1)
    
    elif sums>request: #요청보다 잘린 게 크면
        return tteock(amount,request,tteocks, mid+1,end)
    
    return sums

answer=tteock(4,6,[19,15,10,17],0,19)
print(answer)