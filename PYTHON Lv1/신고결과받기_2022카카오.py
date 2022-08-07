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

