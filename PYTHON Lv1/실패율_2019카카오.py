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
    
    return succ