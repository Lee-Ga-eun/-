# 땅따먹기 게임의 땅은 총 N행 4열로 이루어져있고, 모든 칸에는 점수가 쓰여 있다
# 1행부터 한 칸만 밟으며 마지막 행까지 내려와야 하는데, 한 행씩 내려올 때 같은 열을 연속해서 밟을 수 없다
# 땅따먹기 결과가 가장 큰 값이 정답이다
"""
처음 문제를 풀이했을 땐, 가장 큰 값을 뽑고, 그 다음 행에서 가장 큰 값을 뽑는데, 
먼저 뽑았던 큰 값의 위치와 동일하다면 그 다음 큰 값을 뽑아 저장했다.
이렇게 풀면 안 되는 이유는 다음 예제로 확인할 수 있다

[1,2,3,4],
[2,3,4,100]

위의 과정대로 하면 4+4 =8이다

그러나, 땅따먹기 결과가 가장 크려면, 3+100=103이어야 할 것이다

이 이유로 Dynamic Programming을 통해 

"""

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

answer=solution([[1,2,3,5],[5,6,7,100],[4,3,2,1]])
print(answer)


# 다른 사람 풀이
    
"""
    a=[1,2,3,4,5]

    a[:1] ==> [1]
    a[1+1:] ==> [3,4,5]

    즉, 두번째 수를 제외하고 구할 수 있다! 
    
"""




def solution1(land):

    for i in range(1, len(land)):
        for j in range(len(land[0])):
            # 바로 위, 같은 열에 해당하는 것을 슬라이싱으로 작업한 담에 max값을 뽑아낸다!!!!
            land[i][j] = max(land[i -1][: j] + land[i - 1][j + 1:]) + land[i][j] 

    print(land)

    return max(land[-1])

answer1=solution1([[1,2,3,5],[5,6,7,100],[4,3,2,1]])
print(answer1)