"""
8*8 좌표 평면에서, 다음과 같은 두 가지 규칙으로만 이동이 가능하다

1. 수평으로 두 칸 이동한 뒤에 수직으로 한 칸 이동하기
2. 수직으로 두 칸 이동한 뒤에 수평으로 한 칸 이동하기

현재 말의 위치가 주어질 때, 그 위치에서 이동이 가능한 모든 경우의 수를 출력한다
"""

def solution(position):
    dx=[-1,1,-1,1,-2,-2,2,2]
    dy=[-2,-2,2,2,-1,1,-1,1]

    # a1 --> [0][0]
    alphaDict={'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7}
    x=alphaDict[position[:1]]
    y=int(position[1:])-1

    result=0
    for i in range(len(dx)):
        nx,ny=0,0
        nx=x+dx[i]
        ny=y+dy[i]
        
        if nx<=-1 or ny<=-1 or nx>=8 or ny>=8:
            continue
        else:
            result+=1
    return result

answer=solution('a1')
print(answer)