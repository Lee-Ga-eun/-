
"""
주차장의 요금표와 차량이 들어오고(입차) 나간(출차) 기록이 주어졌을 때, 
차량별로 주차 요금을 계산한다

- 입차된 후 출차된 내역이 없으면, 23:59에 출차된 것으로 간주한다
- 누적 주차 시간이 기본 시간 이하라면, 기본 요금을 청구
- 누적 주차 시간이 기본 시간을 초과하면, 기본 요금에 더해서 초과한 시간에 대해 단위 시간 마다 단위 요금을 청구
- 즉, 차량 번호 0000은 출차 후 다시 입차할 수 있다

<입력>
fees [180, 5000, 10, 600] # 기본시간(분), 기본요금(원), 단위시간(분), 단위요금(원)
records ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"] # 입차시간/출차시간, 차량번호, 입차/출차 여부

<출력>
[14600, 34400, 5000]

"""

#생각한 방법...
# result 딕셔너리: 각 차량 번호에 대해 현재 입차인지, 출차인지 상태를 기록
# gate 딕셔너리: 각 차량 번호에 대해 누적 주차 시간을 저장

# 출차 내역이 없는 차량 처리: 최종 배열에서, result 딕셔너리의 값 중 OUT이 아닌 어떠한 시간이 기록되어 있다면, 출차 시간을 23:59로 계산해준다


def solution(fees,records):
    import math
    result=dict()
    gate=dict()
    for i in range(len(records)):
        car_num=records[i].split()[1]
        if car_num not in result: #{"0000":0} #사실상 초기화
            result[car_num]=records[i].split()[0]
            gate[car_num]=0
        elif car_num in result and result[car_num]=="OUT":#2번 이상 주차하는 차량
            result[car_num]=records[i].split()[0] # records에선 IN 상태. 그러니 result 딕셔너리의 OUT을, 입차 시간으로 업데이트
        elif car_num in result and records[i].split()[2]=="OUT": # 주차시간 계산 및 누적
            h=int(records[i].split()[0].split(":")[0])-int(result[car_num].split(":")[0]) # hour 계산
            m=int(records[i].split()[0].split(":")[1])-int(result[car_num].split(":")[1]) # minute 계산
            gate[car_num]+=h*60+m #시간을 분으로
            result[car_num]="OUT" 

    for i in range(len(list(result.values()))): # 최종 주차 요금 계산 
        key=list(result.keys())[i]
        if list(result.values())[i]!='OUT': # OUT처리 안 된 차량 계산(== 출차시간 23:59)
            h=23-int(result[key].split(":")[0])
            m=59-int(result[key].split(":")[1])
            gate[key]+=h*60+m
            tmp=gate[key]
            if fees[0]<tmp:
                gate[key]=fees[1]+math.ceil((tmp-fees[0])/fees[2])*fees[3]
            else:
                gate[key]=fees[1]
        
        else:
            if fees[0]<gate[key]:
                tmp=gate[key]
                gate[key]=fees[1]+math.ceil((tmp-fees[0])/fees[2])*fees[3]
            else:
                gate[key]=fees[1]
    so=sorted(gate.items(), key=lambda x:x[0]) #출력 조건: 차량 번호가 작은 순서대로 출력
    return [so[i][1] for i in range(len(so))]

a=solution([180, 5000, 10, 600],["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"] )
print(a)

# 다음엔 클래스나 함수를 써보자...