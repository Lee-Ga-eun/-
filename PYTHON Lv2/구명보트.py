# 구명보트는 한 번에 최대 2명씩 탈 수 있으며 무게 제한이 있다
# 구명보트를 최대한 적게 사용하여 모든 사람을 구출하려 한다

def solution(people, limit):
    from collections import deque
    people=deque(sorted(people, reverse=True))
    count=0
    while(people): # if문을 통해 종료 조건을 작성했으나, deque를 통해 결국 리스트에 남은 게 없게 될 것이니까 while(people)로 처리하면 된다
        
        if len(people)>=2 and people[0]+people[-1]<=limit: # [950,900,500,500,100] 큰 순서대로 정렬해야, 최소 보트 개수를 사용한다
            count+=1 # 함께 탈 사람 매칭 성공
            people.popleft() # 제일 앞 제거
            people.pop() # 제일 끝 제거
        else:
            if len(people)>=1 and people[0]<=limit: # 제일 큰 수와 제일 작은 수를 더했을 때 매칭이 안 된다면, 제일 앞에 있는 가장 큰 수를 제거
                people.popleft()
                count+=1 #제거했다는 것은 보트를 사용했다는 것
            
    return count

answer=solution([100,500,500,900,950],1000)
print(answer)