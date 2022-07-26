"""
스마트폰 다이얼 키는 아래와 같다
1 2 3
4 5 6
7 8 9
* 0 #

이 키패드에서 왼손과 오른손의 엄지손가락만을 이용할 것이며,
1,4,7,*을 누를 땐 왼손 엄지손가락 /  3,6,9,# 을 누를 땐 오른손 엄지손가락만을 이용한다.
그 외인 2,5,8,0 을 누를 땐 가깝게 위치한 손가락으로 누른다.
이때 거리는, 칸을 기준으로 계산한다 (대각선 x)
거리가 같다면 오른손잡이인지 왼손잡이인지로 나눈다
입력 매개변수 numbers: 누를 키패드 정보, hand: 왼손잡이?오른손잡이?
"""

#나의 풀이

def solution(numbers,hand):

    keypad=[[1,2,3],[4,5,6],[7,8,9],[10,0,10]] #2차원 배열을 통해 접근한다
    answer=""
    l=(3,0) # 왼손 엄지손가락의 시작 위치는 * 이다
    r=(3,2) #오른손 엄지손가락의 시작 위치는 # 이다
    if hand=="right": hand="R" # 밑에 코드를 위해서 바꿔준다
    if hand=="left": hand="L"

    for n in numbers:
        # 누를 키패드 번호의 위치를 파악한다
        willPress=list((i,j) for i in range(len(keypad)) for j in range(len(keypad[i])) if keypad[i][j]==n)[0] #list없이 출력하면 값이 나오지 않는다. 
        # 리스트 컴프리헨션으로, 리스트로 감싸줘야 한다. 이때 i와 j를 튜플 하나로 묶어줬기 때문에(원소 하나), 결과적으로 list((i,j))[0]을 출력하면 튜플이 나오는 것이다. [(0,1)][0]=(0,1)
        
        if n in [1,4,7]: # 거리와 상관 없이 왼손 엄지손가락으로 누르는 경우
            answer+="L"
            l=willPress
        if n in [3,6,9]: # 거리와 상관 없이 오른손 엄지손가락으로 누르는 경우
            answer+="R"
            r=willPress
        if n in [2,5,8,0]: #2,5,8,0을 눌러야 할 때 (거리를 따져야 할 때)
            if answer=="" and hand=="R": 
                answer+="R" #아직 빈 배열이라면? 오른손잡이인 경우
                r=willPress
                continue
            if answer=="" and hand=="L": 
                answer+="L" #아직 빈 배열이라면? 왼손잡이인 경우
                l=willPress
                continue # 밑의 연산이 진행되면 안 된다
            """
            생각해보니 빈 배열을 고려하는 건 불필요한 코드이다. 왜냐하면 시작 위치를 for문 밖에서 지정해줬기 때문이다
            """
                
            # 빈 배열이 아닐 때(이전에 키패드를 누른 경험이 있음)
            if abs(willPress[0]-l[0])+abs(willPress[1]-l[1])>abs(willPress[0]-r[0])+abs(willPress[1]-r[1]):  # 오른손이 더 가까울 때 (=오른쪽의 거리가 더 짧을 때)
                answer+="R" 
                r=willPress
            if abs(willPress[0]-l[0])+abs(willPress[1]-l[1])<abs(willPress[0]-r[0])+abs(willPress[1]-r[1]): #왼손이 더 가까울 때
                answer+="L"
                l=willPress
            if abs(willPress[0]-l[0])+abs(willPress[1]-l[1])==abs(willPress[0]-r[0])+abs(willPress[1]-r[1]): #왼손과 오른손 각각 거리가 같을 때
                answer+=hand # right를 R, left를 l로 바꾼 이유이다
                if hand=="R":
                    r=willPress
                if hand=="L":
                    l=willPress
    
    return answer

"""
    테스트 1 〉	통과 (0.01ms, 10.2MB)
    테스트 2 〉	통과 (0.01ms, 10.2MB)
    테스트 3 〉	통과 (0.01ms, 10.2MB)
    테스트 4 〉	통과 (0.01ms, 10.3MB)
    테스트 5 〉	통과 (0.01ms, 10.4MB)
    테스트 6 〉	통과 (0.02ms, 10.2MB)
    테스트 7 〉	통과 (0.04ms, 10.2MB)
    테스트 8 〉	통과 (0.07ms, 10.3MB)
    테스트 9 〉	통과 (0.06ms, 10.2MB)
    테스트 10 〉	통과 (0.06ms, 10.2MB)
    테스트 11 〉	통과 (0.15ms, 10.3MB)
    테스트 12 〉	통과 (0.13ms, 10.3MB)
    테스트 13 〉	통과 (0.27ms, 10.3MB)
    테스트 14 〉	통과 (0.56ms, 10.4MB)
    테스트 15 〉	통과 (1.39ms, 10.2MB)
    테스트 16 〉	통과 (1.41ms, 10.2MB)
    테스트 17 〉	통과 (2.69ms, 10.2MB)
    테스트 18 〉	통과 (2.55ms, 10.4MB)
    테스트 19 〉	통과 (2.68ms, 10.2MB)
    테스트 20 〉	통과 (2.63ms, 10.3MB)
"""