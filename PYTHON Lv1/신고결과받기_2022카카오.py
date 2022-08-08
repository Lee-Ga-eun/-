"""
-각 유저는 한 번에 한 명의 유저를 신고할 수 있다
- 동일한 유저에 대한 신고 횟수는 1회로 처리된다
- k번 이상 신고된 유저는 이용이 정지되며, 해당 유저를 신고한 모든 유저에게 정지 사실을 메일로 발송한다

<입력>
id_list=["muzi", "frodo", "apeach", "neo"] # 모든 이용자 
report=["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
     .. muzi는 frodo를 신고/ apeach는 frodo를 신고 ..
k=2
<출력>
[2,1,1,0]

"""

# 나의 풀이: run time error
def solution(id_list,report,k):
    report=list(set(report))
    r={} # {신고한 유저: 신고당한 유저} 딕셔너리로 정리할 것임
    for i in id_list:
        r[i]=[] #한 유저 당 한 명 이상 신고할 수 있기 때문에(append처리 위함)
    for i in id_list: #id_list에 모든 id가 없을 수 있다. 이때 0으로 결과를 내야 한다
        # 여기 timeout 걸리는 듯. 1<=report<=200,000 이어서.
        for j in report: # 신고한 기록이 있을 때
            if j.split(" ")[0] in i: # 아이디가 같을 때
                r[i].append(j.split(" ")[1])  
    got=[] # 신고당한 이용자들이 몇 번 신고 당했는지를 알기 위해, got배열에 신고 당한 것을 순서대로 넣었다
    for i in report: #그럼 이것도 timeout?
        got.append(i.split(" ")[1])
    
    email=[] # 누굴 신고하면 이메일을?
    for j in got: #k번 이상 신고당한 유저가 누군지 알아내고 email에 넣는다
        if got.count(j)>=k:
            email.append(j)
    email=list(set(email))
    r=list(r.values()) # 신고당한 사람들
    """
    {"muzi":["frodo","neo"], "apeach":["frodo","muzi"]} 라면,
    r=[["frodo","neo"],["frodo","muzi"]] 이고
    email과 비교해, 몇 개가 겹치는지 판단하여 딕셔너리 값을 숫자로 변경한다
    """
    for i in range(len(r)): # 신고 당한 이용자들에서 메일 보내는 것에 해당하는 이용자 있는지
        if len(set(r[i])&set(email))>=1:
            r[i]=len(set(r[i])&set(email))
        else:
            r[i]=0
        
    return r

# 재풀이: 딕셔너리로 해결 (딕셔너리 시간복잡도 O(1))

def solution(id_list, report, k):
    report=list(set(report))
    report_dict={}
    complained_count={}
    for i in id_list:
        complained_count[i]=0
    for i in id_list:
        report_dict[i]=[]
    #---> report_dict={i:[] for i in id_list}
    #---> complained_count={i:0 for i in id_list}
    # key:value <== i:0/ i:[]
        
    for i in report:
        a,b=i.split() #a는 신고한 사람, b는 신고 당한 사람
        report_dict[a].append(b)
        complained_count[b]+=1 # report를 딕셔너리로 분류함과 동시에 신고당한 유저 딕셔너리 추가
    print(report_dict) # {'muzi': ['frodo', 'neo'], 'frodo': ['neo'], 'apeach': ['frodo', 'muzi'], 'neo': []}
    print(complained_count) #{'muzi': 1, 'frodo': 2, 'apeach': 0, 'neo': 2}
    answer=[] # 최종 결과를 출력할 배열
    for i,j in report_dict.items(): #i는 key, j는 value
        result=0
        for t in range(len(j)): #각 i의 value 순찰
            if complained_count[(j[t])]>=k: #report_dict의 value는 compalined_count의 key
                result+=1
        answer.append(result)
        
    return answer