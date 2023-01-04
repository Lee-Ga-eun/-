"""
U: 위쪽으로 한 칸 가기
D: 아래쪽으로 한 칸 가기
R: 오른쪽으로 한 칸 가기
L: 왼쪽으로 한 칸 가기

게임 캐릭터가 지나간 길 중 캐릭터가 처음 걸어본 길의 길이를 구한다
단 길이가 5를 넘으면 무시하고 제자리에 있는다
"""
def solution(dirs):
    U=(0,1)
    D=(0,-1)
    L=(-1,0)
    R=(1,0)
    
    walks=[]
    passed=[]

    j=0
    count=0
    for i in range(len(dirs)):
        
        if i==0:
            start=(0,0)
            end=eval(dirs[0])
            passed.append([start,end])
            continue
        # eval을 쓰면, 대상 문자열이 변수로 변환된다. 즉 위에 설정한 변수의 좌표값을 사용할 수 있다
        direction=dirs[i] # 'U', 'D', 'L', 'R'
        x=passed[j][1][0]+eval(direction)[0] # 이동한 x좌표
        y=passed[j][1][1]+eval(direction)[1] # 이동한 y좌표
                
        if -5<=x<=5 and -5<=y<=5:

            new=(x,y) #예를 들면 (1,1)
            print(new)
            # (0,0)->(1,0) 과 (1,0)->(0,0) 으로 이동한 '길이'는 동일하다
            if [new, passed[j][1]] in passed or [passed[j][1],new] in passed:
                passed.append([passed[j][1],new])
                j+=1
                count+=1
                continue
            else: 
                passed.append([passed[j][1],new])
                j+=1
        else: # 조건 범위를 벗어났으니 걸어본 것으로 포함할 수 없다
            count+=1
    print(passed)
    
    return len(dirs)-count

# Do not use eval
## 가독성을 떨어뜨리고 디버깅을 어렵게 한다
## ** 사용자가 마음대로 프로그램에 명령을 입력할 수 있게 된다 --> 해킹


"""
eval을 사용하지 말자 --> 이 문제는 딕셔너리로 풀이하는 것이 좋겠다
"""
