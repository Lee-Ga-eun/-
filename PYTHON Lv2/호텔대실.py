"""
최소한의 룸 수만 사용할 것
청소 시간은 10분. 
총 사용되는 룸 수를 출력
"""

# 풀이: 딕셔너리를 사용해 키 값은 룸 배정 방 넘버와 동일하게 판단한다
# 예약 시간대를 오름차순으로 정렬하였고
# 입실 시간이 기존 쓰이고 있는 방의 퇴실 시간 기준 10분 후 이상이면, 룸을 맞교환 하는 형식
# 새로 배정해야 하는 상황이면 딕셔너리의 키를 추가

def solution(book_time):
    book_time=sorted(book_time) # 시간 순서대로 정렬
    rooms=dict()
    rooms[0]=book_time[0] # 제일 빠른 시간대 방 배정
    print(book_time)
    
    for i in range(1,len(book_time)): #입실 시간 확인. 이미 방에 있는 값들의 퇴실 시간 확인 후 비교하기
        new_book_entrance=book_time[i][0]
        k=0
        for j in range(len(rooms.values())):
            print("들어가야할 방",book_time[i])
            rooms_values=list(rooms.values())
            new_hour=int(new_book_entrance.split(':')[0]) # 시 (새로 입실)
            new_mins=int(new_book_entrance.split(':')[1]) # 분 (새로 입실)
            exist_outtime=rooms_values[j][1] # 퇴실
            exist_hour=int(exist_outtime.split(':')[0]) # 시 (퇴실)
            exist_mins=int(exist_outtime.split(':')[1]) # 분 (퇴실)
            print(exist_hour,exist_mins)
            
            if new_book_entrance>exist_outtime: # 특정 퇴실 시간 다음에 입실 시간일 경우
                if new_hour-exist_hour>=1 and (60+new_mins-exist_mins)>=10: # 예를 들어, 18:50퇴실, 19:00 입실인 경우
    #                 print("마이너스값",book_time[i])
                    rooms[j]=book_time[i]
                    k+=1
                    break
                elif new_mins-exist_mins >=10: # 예를 들어, 18:10퇴실 18:20입실인 경우 | 18:10퇴실 19:20 입실인 경우 
                    rooms[j]=book_time[i]
                    k+=1
                    break
            if k==len(rooms_values)-1: # 배정되어 있는 룸을 다 돌았을 때 맞교환할 만한 룸이 없을 경우 
                    print(k)
                    rooms[len(rooms_values)]=book_time[i] #방추가
                    k+=1
                    break
            else:
                k+=1
                continue
        print(rooms)
            
        
    return len(rooms)

answer=solution([["15:00", "17:00"], ["16:40", "18:20"], ["14:20", "15:20"], ["14:10", "19:20"], ["18:20", "21:20"]])
print(answer)