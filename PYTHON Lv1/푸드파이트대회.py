"""
입력: [1,7,2,1] 
출력: 111202111

첫번째 원소는 물이며 가운데에 배치한다
두 선수들은 똑같은 순서대로 똑같은 음식을 똑같은 양으로 먹어야 한다
한 선수는 왼쪽에서부터 시작, 다른 선수는 오른쪽에서부터 시작
선수들이 먹는 음식을 출력
"""

def solution(food):
    # [1,7,1,2] => 7은 홀수 -> (7-1)//2=3, (1-1)//2=0, 2는 짝수, 2//2=1
    # 따라서 111303111이 결과
    answer = ''
    food=food[1:]
    for i in range(len(food)):
        answer+=str(i+1)*((food[i])//2)

    return answer+'0'+answer[::-1]

answer=solution([1,7,2,1])
print(answer)