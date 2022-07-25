"""
2021 Dev-Matching 문제

로또의 순위를 정하는 방식 (순서는 상관 없다)
1위:6개 모두 일치 , 2위:5개 모두, 3위:4개 모두, 4위:3개 모두 5위:2개모두 6위(낙첨): 1개 혹은 0개 일치

로또에 실수로 낙서가 되어 보지 못하는 부분을 0으로 표시. 이때, 당첨가능한 최고 순위와 최저 순위는?

<조건>
win_nums에는 전부 다른 숫자(0제외)로 되어 있다
"""

#나의 풀이
def solution(lottos, win_nums):
    wins_dict={6:'1', 5:'2', 4:'3',3:'4',2:'5',1:'6',0:'6'} # 맞은 개수에 따른 순위를 딕셔너리로 나타낸다
    순위=list(wins_dict.values()) # 키값만 뽑아낸 리스트. ['1위','2위'..]
    맞은수=list(wins_dict.keys()) # 일치한 갯수만 뽑아낸 리스트. [6,5,4,3,2,1,0]
    zero_nums=0 # 로또에서 0이 표시되어 있는 개수
    for i in range(len(lottos)): 
        if lottos[i]==0:
            zero_nums+=1
    same_nums=len(set(lottos)&set(win_nums)) #순서는 상관 없으므로, 교집합으로 일치하는 숫자를 알아낸다

    answer=[] # 출력 형식을 위해서. 
    min_= 순위[맞은수.index(same_nums)] # 0이 모두 답과 틀리다고 가정했을 때, 최저 순위가 된다
    max_=순위[맞은수.index(zero_nums+same_nums)] #0이 모두 답과 일치하는 숫자라고 가정했을 때, 최고 순위가 된다
    answer.append(int(max_)) # 출력 형식: [최고 순위, 최저 순위]
    answer.append(int(min_))

    return answer

    """
    테스트 1 〉	통과 (0.03ms, 10.5MB)
    테스트 2 〉	통과 (0.02ms, 10.6MB)
    테스트 3 〉	통과 (0.03ms, 10.5MB)
    테스트 4 〉	통과 (0.03ms, 10.5MB)
    테스트 5 〉	통과 (0.02ms, 10.5MB)
    테스트 6 〉	통과 (0.02ms, 10.5MB)
    테스트 7 〉	통과 (0.02ms, 10.6MB)
    테스트 8 〉	통과 (0.02ms, 10.6MB)
    테스트 9 〉	통과 (0.02ms, 10.6MB)
    테스트 10 〉	통과 (0.02ms, 10.6MB)
    테스트 11 〉	통과 (0.03ms, 10.5MB)
    테스트 12 〉	통과 (0.02ms, 10.6MB)
    테스트 13 〉	통과 (0.03ms, 10.5MB)
    테스트 14 〉	통과 (0.02ms, 10.5MB)
    테스트 15 〉	통과 (0.03ms, 10.5MB)
    """

    #*****위의 식에서 딕셔너리 value를 정수형으로 바꾸고, 형변환 없이 출력하면, 테스트 케이스 전부 0.01ms이다

# 다른 풀이
def solution(lottos, win_nums):
    rank=[6,6,5,4,3,2,1]
    zero_count=lottos.count(0) #0인 수를 센다
    same_num=0
    for i in win_nums: #win_nums와 얼만큼 일치하는지 센다
        if i in lottos:
            same_num+=1
    return [rank[same_num+zero_count],rank[same_num]]

    # 실행 결과 모두 0.00ms

#다른 풀이

def solution(lottos, win_nums):
    wins_dict={6:1, 5:2, 4:3,3:4,2:5,1:6,0:6}
    return [wins_dict[len(set(lottos)&set(win_nums))+lottos.count(0)],wins_dict[len(set(lottos)&set(win_nums))]]

    """
    wins_dict={6:1, 5:2, 4:3,3:4,2:5,1:6,0:6}
    wins_dict[0], wins_dict[1]은 6이다
    key의 value를 얻기 위해선, 딕셔너리이름[key값]
    
    """
    #테스트케이스 모두 0.01ms