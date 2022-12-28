#  중앙에는 노란색으로 칠해지고, 테두리 1줄은 갈색으로 칠해져 있는 격자 모양 카펫
# 노란색 격좌 수와 갈색 격좌수가 주어졌을 때 카펫의 가로 세로 길이 구하기
# brown: 8이상 5000이하
# yellow: 1 이상 2,000,000 이하
# 가로의 길이는 세로보다 같거나 크다

# solution1
def solution1(brown,yellow):
    y=1
    while(y<=2000000):
        if(y*((brown+4-2*y)/2)-2*((brown+4-2*y)/2)-2*y+4-yellow==0):
            x=int((brown+4-2*y)/2)
            return [x,y]
        y+=1

## solution1,과 solution2는 풀이법은 똑같음. 다만 라이브러리를 쓰냐 안 쓰냐 차이
# x= 전체 가로 길이, y=전체 세로 길이
# 식1: x+x+y-2+y-2= 2x+2y-4= brown
# 식2: (x-2)(y-2)=yellow 

#solution2
from sympy import Symbol,solve
def solution2(brown,yellow):
    x=Symbol('x')
    y=Symbol('y')

    equation1=(x-2)*(y-2)-yellow
    equation2=2*x+2*y-4-brown

    result=solve((equation1,equation2),dict=False)
    
    if(len(result)>1):
        first=list(result[0].values())
        second=list(result[1].values())
        if first[0]>second[0]:
            result=first
        else:
            result=second
    else:
        result=list(result[0].values())
    return result

solution1(10,2)
solution2(8,1)