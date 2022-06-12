"""
1번 수포자가 찍는 방식: 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, ...
2번 수포자가 찍는 방식: 2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5, ...
3번 수포자가 찍는 방식: 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, ...
답을 얼마나 맞췄는가? 답을 가장 많이 맞춘 학생을 출력한다.

#조건1. 시험은 최대 10,000 문제로 구성
#조건2. 모두 틀릴 경우, 모두 출력 
#조건3. 가장 높은 점수를 받은 사람이 여려 명일 땐, 학생 번호를 오름차순으로 출력

"""

#나의 풀이. 12점 획득

import numpy as np

def solution(answers):

    # 학생들의 정답표를 담은 2차원 배열 생성
    students=[0,0,0] 
    students[0]=[1,2,3,4,5]*2000
    students[1]=[2,1,2,3,2,4,2,5]*1250
    students[2]=[3,3,1,1,2,2,4,4,5,5]*2000

    cnt=[]
    for student in students:
        
        #student_sliced=student[0:len(answers)]
        #make_zero=list(np.array(answers-np.array(student_sliced)))
        make_zero=list(np.array(answers-np.array(student[0:len(answers)])))
        # 0의 개수 세기
        cnt.append(make_zero.count(0))
        
    #cnt에는 각 학생 별 정답 맞춘 개수가 들어가 있을 것
    #각 학생 별 맞춘 개수 중 최대값
    max_item=max(cnt)
    #그 최대값의 위치 찾기
    answer=list(filter(lambda x: cnt[x]==max_item, range(len(cnt))))
    # 위치에 1을 더해주며 리턴 (인덱스이기 때문에)
    return list(map(lambda x: answer[x]+1, range(len(answer))))


"""
#다른 풀이1

<enumerate: 원소와 인덱스를 같이 출력하고 싶을 때>

for i, letter in enumerate(['A', 'B', 'C']):
    print(i, letter)

>> 0 A
   1 B
   2 C

"""
def solution(answers):
    pattern1 = [1,2,3,4,5]
    pattern2 = [2,1,2,3,2,4,2,5]
    pattern3 = [3,3,1,1,2,2,4,4,5,5]
    score = [0, 0, 0]
    result = []

#idx%len() : answer의 길이와 패턴 1,2,3 각각의 길이는 다르지만, 
# 패턴 1,2,3의 요소를 계속 반복적으로 사용하여 길이를 맞춰 사용할 수 있게 한다
    for idx, answer in enumerate(answers):
        if answer == pattern1[idx%len(pattern1)]:
            score[0] += 1
        if answer == pattern2[idx%len(pattern2)]:
            score[1] += 1
        if answer == pattern3[idx%len(pattern3)]:
            score[2] += 1

    for idx, s in enumerate(score):
        if s == max(score):
            result.append(idx+1)

    return result


"""
# 다른 풀이 2

"""
def solution(answers):
    student={1:[1,2,3,4,5],2:[2,1,2,3,2,4,2,5],3:[3,3,1,1,2,2,4,4,5,5]}
    score={1:0, 2:0, 3:0}

    for idx, answer in enumerate(answers):
        for key, value in student.items():
            if answer==value[idx%len(value)]:
                score[key]+=1
    
    highest=max(score.values())
    answer=[key for key, value in score.items() if value==highest]

    return answer

"""
한번 더
"""
def solution(answers):
# 학생들의 답안지를 딕셔너리로 생성. 학생1, 학생2, 학생3가 있다
    student={1:[1,2,3,4,5],2:[2,1,3,4,5,2,3,2,1,3,4,5,2,3],3:[5,5,3,3,2,2,1,1,5,5,3,3]}

# 맞춘 수를 넣을 score라는 딕셔너리를 생성(초기화: 1번 0점, 2번 0점, 3번 0점)
    score={1:0, 2:0, 3:0}

#for문을 통해, 이제 답지와 비교를 시작한다.(enumerate함수를 활용)답이 맞으면 score 딕셔너리의 값을 증가시킨다
    # idx % len(value)
    #items: 딕셔너리의 키와 값의 쌍을 얻을 수 있음
    #for key, value in student.items():
        #[1, [1,2,3,4,5]]
    for idx, answer in enumerate(answers):
        for key, value in student.items():
            # answers: [1,2,3,4,5]
            # answer: [1]
            if answer == value[idx%len(value)]:
                score[key]+=1
            
    answer=[]

#score 중 이제 최대값을 찾은 후, 최대값의 인덱스를 뽑아낸다. (학생 번호를 리스트로 추출)

    #{1:2,2:1,3:0} 이라고 생각
    for key, value in score.items():
        if value == max(score.values()):
            answer.append(key)
    
    return answer