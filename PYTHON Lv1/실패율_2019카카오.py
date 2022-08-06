"""
전체 스테이지의 개수 N, 게임을 이용하는 사용자가 현재 멈춰있는 스테이지의 번호가 담긴 배열 stages
실패율이 높은 스테이지부터 내림차순으로 스테이지의 번호가 담겨있는 배열을 return

"""

def solution(N,stages):
    stages=sorted(stages) # 참여자들 스테이지 정렬
    #[1,2,2,2,3,3,4,6]
    #[4,4,4,4,4]
    sc=[i for i in range(1,N+1)] # 스테이지 몇 개인지 배열에 담는다. stage count
    print(sc)
    succ=[] # 
    j=0
    for i in sc:
        if stages[j]==i:
            succ.append(stages.count(i))
            print(stages.count(i))
            j+=stages.count(i)
        else:
            succ.append(0)
            j+=1
    #실패율 계산
    tmp=len(stages)
    for i in range(len(succ)):
        keep=succ[i] #킵한다는 의미
        succ[i]=succ[i]/tmp
        tmp-=keep
    # 딕셔너리로 스테이지 부여 후, value를 정렬한 후 key값 뽑아내어 값 도출
    suc_dict={}
    for i in range(len(succ)):
        suc_dict[i+1]=succ[i]
        
    suc_dict=sorted(suc_dict.items(), key=lambda x:x[1], reverse=True)
    return [suc_dict[i][0] for i in range(len(suc_dict))]
    
    """
    결과
    실패 (런타임 에러)
    테스트 2 〉	통과 (0.28ms, 10.3MB)
    테스트 3 〉	통과 (104.93ms, 10.6MB)
    테스트 4 〉	통과 (551.52ms, 12MB)
    테스트 5 〉	통과 (2800.54ms, 17.2MB)
    테스트 6 〉	실패 (런타임 에러)
    테스트 7 〉	실패 (런타임 에러)
    테스트 8 〉	통과 (555.90ms, 11.9MB)
    테스트 9 〉	실패 (런타임 에러)
    테스트 10 〉	실패 (193.29ms, 12MB)
    테스트 11 〉	실패 (183.05ms, 11.9MB)
    테스트 12 〉	실패 (347.93ms, 13MB)
    테스트 13 〉	실패 (런타임 에러)
    테스트 14 〉	통과 (0.02ms, 10.4MB)
    테스트 15 〉	통과 (23.84ms, 11.2MB)
    테스트 16 〉	통과 (17.11ms, 10.6MB)
    테스트 17 〉	통과 (24.44ms, 11.2MB)
    테스트 18 〉	통과 (11.25ms, 10.7MB)
    테스트 19 〉	통과 (2.39ms, 10.4MB)
    테스트 20 〉	통과 (19.04ms, 10.8MB)
    테스트 21 〉	통과 (34.30ms, 11.7MB)
    테스트 22 〉	통과 (2149.79ms, 19.3MB)
    테스트 23 〉	실패 (런타임 에러)
    테스트 24 〉	실패 (런타임 에러)
    테스트 25 〉	실패 (런타임 에러)
    테스트 26 〉	통과 (0.01ms, 10.2MB)
    테스트 27 〉	통과 (0.01ms, 10.4MB)
    
    """



# 다시 풀고 성공
def solution(N,stages):
    stages=sorted(stages) # 참여자들 스테이지 정렬
    sc=[i for i in range(1,N+1)] # 스테이지 몇 개인지 배열에 담는다. 
    succ=[] # 몇 명이 스테이지를 성공했는지 담을 예정
    j=0 # 스테이지를 탐색할 변수
    for i in sc: # 스테이지를 탐색
        if stages[j]>=i: # 현재 i라는 스테이지를 성공한 사람이 있다면
            succ.append(stages.count(i)) #몇 명인지 세고 succ에 넣는다
            j+=stages.count(i) #다음 스테이지 탐색
        else: # 성공하지 못 했다면
            succ.append(0) # 0명을 succ에 넣는다
            j+=1 # 다음 스테이지 탐색
        if j==len(stages): #더이상 stages에서 탐색할 게 없을 때
            for k in range(N-stages[-1:][0]):
                succ.append(0)
            break
    print(succ)
    #실패율 계산
    tmp=len(stages) # 스테이지 도전한 사람들 몇 명?
    for i in range(len(succ)):
        keep=succ[i] #킵한다는 의미
        succ[i]=succ[i]/tmp
        tmp-=keep
        if tmp==0:
            break
            
    suc_dict={}
    for i in range(len(succ)):
        suc_dict[i+1]=succ[i]
        
    suc_dict=sorted(suc_dict.items(), key=lambda x:x[1], reverse=True)
    return [suc_dict[i][0] for i in range(len(suc_dict))]

