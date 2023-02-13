"""
상하좌우로 연결되는 땅은 하나의 무인도를 이루며
지도에 적힌 각 숫자를 모두 합한 값은 무인도에서 며칠동안 머물 수 있는지를 나타낸다
각 섬에서 머물 수 있는 기간을 배열에 오름차순으로 담아 출력한다

'X'는 바다이며 갈 수 없다
지낼 수 있는 무인도가 없으면 배열에 -1을 담아 리턴한다
"""

def solution(maps):
    visited=[[0]*len(maps[0]) for i in range(len(maps))]
    result=[]
    from collections import deque
    def bfs(x,y):
        queue=deque()
        queue.append((x,y))
        visited[x][y]=1
        dx=[-1,1,0,0]
        dy=[0,0,-1,1]
        count=0
        while(queue):
            a,b=queue.popleft()
            #print(maps[a][b])
            count+=int(maps[a][b])
            for k in range(4):
                nx=dx[k]+a
                ny=dy[k]+b

                if nx<=-1 or ny<=-1 or nx>=len(maps) or ny>=len(maps[0]):
                    continue
                if maps[nx][ny]!='X' and visited[nx][ny]!=1:
                    queue.append((nx,ny))
                    visited[nx][ny]=1
        result.append(count)
            
        
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j]!='X' and visited[i][j]!=1:
                bfs(i,j)

    
    if len(result)==0:
        return [-1]
    else:
        return sorted(result,reverse=False)