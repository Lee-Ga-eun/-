"""
채팅방에 들어오고 나가거나, 닉네임을 변경한 기록이 담긴 문자열 배열 record가 매개변수로 주어질 때, 
모든 기록이 처리된 후, 최종적으로 방을 개설한 사람이 보게 되는 메시지를 문자열 배열 형태로 리턴한다

<입력>
record 배열= ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
<출력>
["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."]


"""
def solution(record):
    info=dict()
    for i in range(len(record)):
        a=record[i].split() 
        if len(a)==3:
            info[a[1]]=a[2]
    answer=[]
    for i in range(len(record)):
        a=record[i].split()
        if a[0]=='Enter':
            answer.append(str(info[a[1]])+"님이 들어왔습니다.")
        elif a[0]=='Leave':
            answer.append(str(info[a[1]])+"님이 나갔습니다.")
    return answer

result=solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"])
print(result)

# 풀이방법: 딕셔너리는 키값을 기준으로 value값이 변경되면 최종적으로 갱신된 것이 저장되어 있다