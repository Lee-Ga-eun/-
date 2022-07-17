"""
<2019 카카오 개발자 겨울 인턴십>
N*N 크기의 정사각형 격자가 있으며, 그 격자에는 인형들이 들어가있다.
인형들의 종류는 숫자로 표현하며, 0은 격자가 비어있단 뜻이다. 같은 인형 종류는 같은 숫자이다
moves는 크레인의 위치이다. 1이라면 1열에 있다.
크레인이 1열을 선택하면, 1열의 가장 위에 있는 인형을 끄집어내 바구니에 순서대로 집어 넣는다.
바구니에 쌓였을 때, 같은 인형이 연속으로 들어가면 둘 다 제거시킨다.
이때 제거된 인형의 수를 구한다

입력
board: [[0,0,0,0,0],
        [0,0,1,0,3],
        [0,2,5,0,1],
        [4,2,4,4,2],
        [3,5,1,3,1]]
moves: [1,5,3,5,1,2,1,4]
출력
result:4

"""
def solution(board, move):
    # 2차원배열인  board의 열과 행을 뒤집는다. 
    # 1열은 [0,0,0,4,3] 2열은 [0,0,2,2,5]..로 접근하기 위해서이다
    reversed_arr=[[0 for i in range(len(board))] for i in range(len(board))] #0으로 전부 초기화된 2차열 배열을 만든다
    for i in range(len(board)):
        #i는 0부터 5까지
        for j in range(len(board)):
            #j는 0부터 5까지
            reversed_arr[i][j]=board[j][i] #값을 대체한다
    #print(reversed_arr)

    basket=[] # 인형들을 담을 배열
    cnt=0 # 밖으로 빼진 인형 수

    for i in move: # move가 끝날 때까지(크레인이 다 돌 때까지)
        for idx, j in enumerate(reversed_arr[i-1]): # 크레인이 1이면, board 배열의 0번째 행을 돈다는 것과 같다
            if j!=0: # 0은 비어있는 곳이다. 즉 인형이 있는 깊이까지 내려가야 한다
                print("pop후 제대로 나갔나?") # break가 제대로 되는지 디버깅
                # 만약 j가 basket의 마지막 인덱스와 같다면, j를 basket에 넣지 않을 것이며,
                # 마지막 인덱스 또한 pop한다
                #count 를 센다. 2를 더하면 될 것이다
                # basket이 빈 배열이라면?
                
                if (len(basket)>=1): #basket이 비어있으면, pop에서 에러가 난다
                    if j==basket[-1]: # basket의 마지막 들어간 값과 이번에 들어갈 값을 비교한다. 
                        print("************** 같은 인형 들어간다") # 같으면 제거해야 한다
                        print("j는",j)
                        print("pop전",basket)
                        basket.pop()
                        print("pop후",basket)
                        cnt+=2
                        print("****************. 같은 인형 나갔다")
                        reversed_arr[i-1][idx]=0 #board에 크레인이 인형을 집어갔다는 것을 적용해야 한다
                        break
                print("-------새로운 인형 들어갑니다------")
                print("append할 j",j) 
                basket.append(j) # 같은 인형이 아니라면, 그대로 바구니에 들어간다
                print("basket:",basket)
                reversed_arr[i-1][idx]=0 # board에 크레인이 인형을 집어갔다는 것을 적용해야 한다
                    
                #print(reversed_arr[i-1])
                break # 하나만 빼가야 하기 때문에 for문을 멈춘다
    return cnt 