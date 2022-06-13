"""
문제 설명
몇 학생들은 체육복을 도난 맞았으며, 체육복이 없으면 수업에 참석할 수 없다
이때 여분의 체육복을 갖고 있는 학생은 자신을 기준으로 앞 뒤 중 한 명에게 체육복을 빌려줄 수 있다
단, 여분이 있는데 도난을 맞았다면 빌려줄 수 없다
수업에 참석할 수 있는 학생 수는?

"""




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


#다른 풀이1

def solution(n, lost, reserve):
    #여분이 있는데 도둑 맞은 경우엔, 여분을 제공할 수 없다
    reserving_person=[r for r in reserve if r not in lost] # 여분을 확실하게 갖고 있는 사람
    lost_person=[l for l in lost if l not in reserve] #확실하게 잃어버린 사람

    for r in reserving_person:
        front_person_num=r-1 #여분을 제공할 수 있는 사람의 앞 번호
        back_person_num=r+1 #여분을 제공할 수 있는 사람의 뒷 번호
        if front_person_num in lost_person:
            lost_person.remove(front_person_num)
        elif back_person_num in lost_person:
            lost_person.remove(back_person_num)
        
    return n-len(lost_person)

#다른 풀이2
def solution(n, lost, reserve):
    
    reserved=set(reserve)-set(lost)
    losted=set(lost)-set(reserve)

    for r in sorted(reserved):
        if r-1 in losted:
            losted=losted-{r-1}
        elif r+1 in losted:
            losted=losted+{r+1}
    return n-len(losted)
    
