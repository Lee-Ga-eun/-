# DP 테이블 생성.
# 총 N행 4열이라고 함

def solution(land):
    
    dp=[[] for i in range(len(land))] # land와 크기가 같은 dp 테이블 생성
    dp[0]=land[0]
    
    
    for i in range(1, len(land)): # land 테이블 한 행씩 돌기
        
        
        
        for j in range(len(land[0])): # 열 개수만큼 돌기
            
            m=0
            for k in range(len(land[0])):
                
                if j==k: 
                    continue
                tmp=land[i][j]+dp[i-1][k]
                if tmp>m:
                    m=tmp
            dp[i].append(m) # dp값 저장
        
        
    
    return max(dp[-1])