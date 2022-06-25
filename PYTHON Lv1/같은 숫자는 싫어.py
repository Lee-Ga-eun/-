"""
배열이 주어졌을 때, 연속된 숫자가 있다면 제거한다
"""

def solution(arr):
    answer=[arr[0]]
    j=0
    for i in range(1,len(arr)):
        print(arr[i])
        if arr[j]!=arr[i]: answer.append(arr[i])
        j+=1
    return answer

def solution2(arr):
    answer=[arr[0]]
    for idx, i in enumerate(range(1,len(arr))):
        if arr[idx]!=arr[i]:
            answer.append(arr[i])
    return answer

def solution3(arr):
    answer=[]
    # answer의 가장 마지막 (가장 최근 append된 것)과 arr 비교
    for i in arr:
        if answer[-1:]!=[i]: # 리스트끼리 비교해야하므로 [i] 
            answer.append(i)
    return answer
        
def solution4(arr):
    answer=[]
    for i in arr:
        # 빈 배열 answer에 answer[-1]이면 index out of range 오류
        # 그래서 solution3에서 슬라이싱을 쓴 것
        # answer[-1]로 풀고 싶으면, 비어있을 때를 따로 처리해줘야 함
        
        if len(answer)==0 or answer[-1]!=i:
            answer.append(i)
    return answer
        