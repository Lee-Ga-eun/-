"""
동쪽 방향으로 가다가 남쪽 방향으로 가기 등
"""

# 동 남 서 북
dx=[0,1,0,-1]
dy=[1,0,-1,0]

def turn(direction,C):
    if C=='왼쪽':
        direction=(direction-1)%4
    elif C=='오른쪽':
        direction=(direction+1)%4
    
    return direction

print(turn(0,'왼쪽')) # 동쪽 방향으로 가다가 왼쪽으로 90도 회전하기 == 북쪽 바라보기 == x에서 -1빼고 y는 그대로