def solution(wallpaper):
    answer = []
    # 격자판에 위치판 파일들. 빈칸은 ., 파일은 #
    # 시작점은 행렬 좌표 그대로, 끝점은 x+1, y+1 해줘야함
    # 시작점은 가장 왼쪽, 가장 위
    # 끝점은 가장 오른쪽, 가장아래

    direction=[1e9,1e9,-1e9,-1e9] # 가장왼쪽, 가장윗쪽, 가장오른쪽, 가장아래쪽
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[0])):
            if wallpaper[i][j]=='#':
                direction[0]=min(i,direction[0])
                direction[1]=min(j,direction[1])
                direction[2]=max(i+1,direction[2])
                direction[3]=max(j+1,direction[3])
    return direction