




# 나의 풀이
def solution(n, lost, reserve):
    
    # 1번부터 n번까지 배열을 만든다. 배열 이름은 all_students 로 한다
    all_students=[]
    for i in range(n):
        all_students.append(1)

    """
    코드 수정:
    all_students=[1 for i in range(n)]
    """
        
    # 도난 당한 학생들
    for lost_number in lost:
        all_students[lost_number-1]-=1
    
    #여분이 있는 학생들
    for re in reserve:
        all_students[re-1]+=1
        
    # 여분 옷 빌려준 것을 배열로 나타냄 (배열 이름: all_students) 
    for idx, al in enumerate(all_students):
        if al>1:
            if idx==0:
                if all_students[idx+1]==0:
                    all_students[idx+1]+=1
                    all_students[idx]-=1
                    continue
            elif idx==len(all_students)-1:
                if all_students[idx-1]==0:
                    all_students[idx-1]+=1
                    all_students[idx]-=1
                    continue
            else:
                #all_students[idx-1]+1 or all_students[idx+1]+1
                if all_students[idx-1]==0:
                    all_students[idx-1]+=1
                    all_students[idx]-=1
                    continue
            
                elif all_students[idx+1]==0:
                    all_students[idx+1]+=1
                    all_students[idx]-=1
                    continue

    
    # 수업을 들을 수 있는 학생 수 결과 출력. (answer)
    answer=0
    for i in all_students:
        if i != 0:
            answer+=1
    """
    코드 간략화
    answer=len([i for i in range(all_students) if i!=0])
    """

    return answer