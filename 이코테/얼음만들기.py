"""
얼음틀에서 0으로 된 곳은 물을 부어 얼음을 만들 수 있고
1로 된 곳은 막힌 곳이다
0으로 연결된 곳은 아이스크림 하나를 만들 수 있다
만들 수 있는 아이스크림은 모두 몇 개인가?
"""

# dfs vs bfs? -> 0의 시작점 찾았을 때 막힌 지점 전까지 탐색 --> 깊은 곳까지 탐색: dfs

tray=[[0,0,1,1,0],
      [0,0,0,1,1],
      [1,1,1,1,1],
      [0,0,0,0,0]]

def dfs(x,y):
    if x<=-1 or y<=-1 or x>=len(tray) or y>=len(tray[0]): #범위를 벗어나는 경우
        return False

    if tray[x][y]==0:
        tray[x][y]=1
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y-1)
        dfs(x,y+1)
        return True
    return False
    
result=0
for i in range(len(tray)): # len(tray)=4
    for j in range(len(tray[0])): # len(tray[0])=5
        if dfs(i,j)==True:
            result+=1
        
print(result)