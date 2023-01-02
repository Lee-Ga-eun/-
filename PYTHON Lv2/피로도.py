# 가장 많이 탐험할 수 있도록 할 때, 그 숫자
# 각 라운드는 [최소 필요 피로도, 소모피로 필요도]이며 최소필요피로도: 던전 탐험을 위해 가지고 있어야 하는 최소의 피로도, 소모피로필요도: 해당 던전 탐험 시 소모되는 피로도
# 매개변수: 현재 피로도, [최소 필요피로도, 소모피로필요도] 배열
# 현재 피로도는 1이상 5000이하로 주어짐
# dungeons 길이는 1 이상 8 이하

# 경우의 수로 푸는 방법
from itertools import permutations

def solution(k, dungeons):
    
    print(list(permutations(dungeons, len(dungeons))))
    answer=[]
    for permutation in permutations(dungeons,len(dungeons)):
        #print(list(permutations)) --> [([80, 20], [50, 40], [30, 10]), ([80, 20], [30, 10], [50, 40]), ([50, 40], [80, 20], [30, 10]), ([50, 40], [30, 10], [80, 20]), ([30, 10], [80, 20], [50, 40]), ([30, 10], [50, 40], [80, 20])]
        print((permutation))
        current=k # k를 current로 복사하여 보존
        count=0
        for i in range(len(permutation)):
            if current>=permutation[i][0]: # 현재 피로도 >= 최소 필요 피로도
                current-=permutation[i][1] # 현재 피로도 -= 소모 필요도
                count+=1
        answer.append(count)
    
    return max(answer)

solution(80, [[80,20],[50,40],[30,10]])

# 무리수 (실패한 풀이, 정확도 61)
def solution(k,dungeons):
    lost=[i[1] for i in dungeons] # 소모 필요도만 분리
    minimum=[i[0] for i in dungeons] # 최소 필요도만 분리
    print(lost)
    print(minimum)
    count=0
    while(True):
        if k in minimum: # 현재 피로도와 최소 필요도가 같은 게 있으면 먼저 처리 (예를 들어 80, 80)
            find_index=minimum.index(k) # 같은 것의 인덱스를 찾아냄
            minimum[find_index]=10000000 # 해당 최소필요피로도 해결했으므로 더이상 건드릴 수 없게 1000000으로 갱신
            k-=lost[find_index] # 현재값 갱신
            count+=1 
            lost[find_index]=1000000 # 해당 손실피로도 해결
        else:
            # 온갖 경우의 수를 하나씩 해결해보려 하다 보니, 코드도 너무 길어지고 비효율적으로 됨

            m=min(lost)
            find_index=lost.index(m)
            if k>=minimum[find_index]: # 도전할 수 있는 단계
                k-=lost[find_index] #현재 값 갱신
                minimum[find_index]=1000000
                lost[find_index]=100000
                count+=1
                
            elif k<minimum[find_index] and sum(lost)<len(lost)*100000:
                tmp=lost
                tmp_mi=min(tmp)
                tmp[tmp.index(tmp_mi)]=100000
                m=min(tmp)
                print(m)
                find_index=lost.index(m)
                k-=lost[find_index] #현재 값 갱신
                minimum[find_index]=1000000
                lost[find_index]=100000
                count+=1

# dfs로 풀기 (공부 중)