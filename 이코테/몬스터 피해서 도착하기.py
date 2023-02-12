"""
0과 1로 구성된 맵이 있다.
0은 몬스터가 있어서 갈 수 없는 길이다.
시작점 (0,0)에서 끝 (n,m)까지 갈 때, 최단 길이를 찾는다 
"""

load=[[1,0,1,0,1,0],
     [1,1,1,1,1,1],
     [0,0,0,0,0,1],
     [1,1,1,1,1,1],
     [1,1,1,1,1,1]]

from collections import deque

def bfs(x,y):
    
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    
    queue=deque()
    
    queue.append((x,y)) # (0,0) 들어올 것
    
    while(queue): # 큐가 빌 때까지
        
        x,y=queue.popleft()
        for i in range(4):
            nx=dx[i]+x
            ny=dy[i]+y
            
            if nx<=-1 or ny<=-1 or nx>=len(load) or ny>=len(load[0]):
                continue
            
            if load[nx][ny]==1: # 몬스터가 없으면서 방문하지 않은 길이 1이다. 방문했다면 +1로 누적된다
                load[nx][ny]=load[x][y]+1
                queue.append((nx,ny)) # 방문 노드 큐에 삽입
        print(queue)

                
    return load[4][5]

answer=bfs(0,0)
print(answer)