"""
카드 뭉치에서 뭉치에 있는 순서대로 한 장씩 뽑아 goal의 문장을 만들어야한다
이것이 가능하면 Yes 불가능하면 No를 출력한다
첫 장을 뽑지 않고 다음 장으로 넘어갈 수 없으며, 뭉치 단위는 순서가 없다
"""

def solution(cards1, cards2, goal):
    # 카드 뭉치에서 순서 중요. 순서대로 해야 함
    from collections import deque
    cards1=deque(cards1)
    cards2=deque(cards2)
    for i in range(len(goal)):
        if len(cards1)>=1 and goal[i]==cards1[0]:
            cards1.popleft()
            continue
        elif len(cards2)>=1 and goal[i]==cards2[0]:
            cards2.popleft()
            continue
        else:
            return "No"
    
    return "Yes"

answer=solution(["i", "drink", "water"],["want","to"],["i", "want", "to", "drink", "water"])
print(answer)