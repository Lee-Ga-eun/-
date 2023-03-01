"""
주어진 항공권을 모두 이용하여 여행경로를 짜며, 항상 인천공항에서 출발한다
모든 도시를 방문할 수 없는 경우는 주어지지 않으며, 
tickets의 각 행 [a,b]는 a공항에서 b공항으로 간다는 의미이다
알파벳 순을 따져야 한다
"""
# 가는 경로를 출력한다
# 입력: [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
# 출력: ["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"]

# 딕셔너리를 정렬하는 법: (value 기준)
# tic=sorted(tic.items(), key=lambda x:x[1][1])

def solution(tickets):
    answer = []
    visited=[0]*len(tickets) # 방문한 건 1로 처리할 것임
    t1=[tickets[i] for i in range(len(tickets)) if tickets[i][0]=='ICN']
    t2=[tickets[i] for i in range(len(tickets)) if tickets[i][0]!='ICN']
    t1=sorted(t1, key=lambda x:x[1])
    t2=sorted(t2, key=lambda x:x[1])
    tickets=t1+t2
    st=[(0,tickets[0])]
    visited[0]=1 # 일단 방문처리 함으로써 초기화
    def making_dfs(tickets,st):
        
        for i in range(len(tickets)):
            if len(set(visited))==1:
                return st
            if st[-1][1][1]==tickets[i][0] and visited[i]==0: # 아직 방문처리하지 않았고
                #도착지와 출발지가 같은 경우
                visited[i]=1 #방문처리
                st.append((i,tickets[i]))
                making_dfs(tickets,st)
                break
            if i==len(tickets)-1: # 갈 수 있는 곳이 없을 때
                # 다시 돌려놔야 한다
                tmp=st.pop() # 일단 제거
                visited[tmp[0]]=0 # 방문하지 않은 것으로 다시 되돌려놓음
                making_dfs(tickets,st)
        return ['ICN']+[st[i][1][0] for i in range(len(st)) if i!=0]+[st[-1][1][1]]
    return making_dfs(tickets,st)

answer1=solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]])
print(answer1)