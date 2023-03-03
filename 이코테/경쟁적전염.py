
from collections import deque

def solution(graph, sec,x,y):
    virus=[]
    for i in range(len(graph)):
        for j in range(len(graph[0])):
            if graph[i][j]!=0: # 바이러스라면
                virus.append((graph[i][j],0,i,j))
    virus.sort()
    q=deque(virus)

    target_s=sec
    target_x, target_y=x,y

    dx=[-1,1,0,0]
    dy=[0,0,-1,1]

    while q:
        tmp_v, tmp_s, tmp_x, tmp_y=q.popleft()
        if tmp_s==target_s:
            break # while문 종료

        for i in range(4):
            nx=dx[i]+tmp_x
            ny=dy[i]+tmp_y

            if nx<=-1 or ny<=-1 or nx>=len(graph) or ny>=len(graph[0]):
                continue

            if graph[nx][ny]==0:
                graph[nx][ny]=tmp_v
                q.append((tmp_v, tmp_s+1, nx, ny))


    return graph[target_x-1][target_y-1]



answer=solution([[1,0,2],[0,0,0],[3,0,0]],2,3,2)
print("answer1",answer)

answer2=solution([[1,0,2],[0,0,0],[3,0,0]],1,2,2)
print("answer2",answer2)