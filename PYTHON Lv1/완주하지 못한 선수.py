
# 참석한 사람들의 배열 이름: participant
# 완주한 사람들의 배열 이름: completion
# 완주하지 못한 사람은 한 명이다


# _______________풀이 1 __________________

import collections

def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]


"""
import collections는, dict, list, set 및 tuple에 대한 대안을 제공하는 특수 컨테이너 데이터형을 구현한다
Counter 클래스는, import collections에 내장되어 있다
Counter 클래스는, 상호간의 뺼셈을 제공한다
list를 가지고 Counter를 생성하면, key가 이름이고 Value가 count인 딕셔너리를 생성한다

<<list(answer.keys())[0]>>
1. 우린 key값을 알아야 하기 때문에, answer.keys() 를 시행한다 // {'A':1} 에서 -> dict_keys(['A']) 가 된다
2. list로 형변환을 해야 한다. // ['A']
3. list[0] 로 문자 "A"에 접근한다

"""


# _______________풀이 2 __________________
def solution(participant, completion):
    participant.sort()
    completion.sort()
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
    return participant[len(participant)-1]
    # return participant[-1]

# _______________풀이 3 __________________

def solution(participant, completion):
    participant.sort() #정렬
    completion.sort() #정렬
    for p, c in zip(participant, completion):
        if p != c:
            return p
    return participant[-1]

"""
<입력>
numbers = [1, 2, 3]
letters = ["A", "B", "C"]
for p,c in zip(numbers, letters):
    print("p는",p, "c는",c)

<결과>
p는 1 c는 A
p는 2 c는 B
p는 3 c는 C


>>> dict_num = { x:y for x, y in zip(range(10),range(10))}
{0: 0, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9}

"""


# _______________풀이 4 __________________

def solution(participant, completion):
    answer = ''
    sumHash = 0
    dic = {}  # 해쉬테이블 만들기
    for part in participant:
        dic[hash(part)] = part
        sumHash += hash(part)
    for com in completion:
        sumHash -= hash(com)
    answer = dic[sumHash]

    return answer

"""
>>> dic{} : 해쉬 맵이다
    해쉬 맵(Hash map/Hash table)이란, Key-Value 쌍을 관리하는 클래스이다.
    key는 hash한 값이 될 것이며, Value는 선수 이름이 될 것이다

>>> for part in participant: 
        dic[hash(part)] = part
        sumHash += hash(part)
    part는 이름이 되고, hash(part)는 임의의 숫자가 된다
    해쉬 함수로 인해 생성된 모든 숫자들을 더해 sumHash에 저장한다

--------예시-------
파이썬에서, dictionary가 곧 해쉬 테이블

a=['banana','apple','kiwi']
b=['banana','watermelon','apple']
dic={}
for i in a:
    dic[hash(i)]=i
    print(dic[hash(i)],"는",hash(i))
>>>    
banana 는 -9025520212752651988
apple 는 -5828658187723283107
kiwi 는 

for j in b:
    dic[hash(j)]=j
    print(dic[hash(j)],"는",hash(j))
>>>
banana 는 -9025520212752651988
watermelon 는 -8579716853824114078
apple 는 -5828658187723283107

결론::::: 동일한 키 값은 동일한 해시 값을 가진다.
"""