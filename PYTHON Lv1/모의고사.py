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
        