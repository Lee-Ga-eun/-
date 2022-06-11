"""
(입력) array [1,5,2,6,3,7,4]
(입력) commands[[2,5,3],[4,4,1],[1,7,4]]
(출력) [5,6,3]

풀이 예:
[1, 5, 2, 6, 3, 7, 4]를 2번째부터 5번째까지 자른 후 정렬합니다. 
[2, 3, 5, 6]의 세 번째 숫자는 5입니다.

"""

"""
<나의 풀이>

2차원 배열을 for문에서 작동시켜서, 하나씩 꺼내 i,j,k를 부여한다.
슬라이싱 범위를 생각한다
임의의 배열에 정렬한 배열을 대입한다
임의의 배열은 한 번 루프가 끝나면 초기화시킨다

"""

def solution(array, commands):
    
    answer=[]
    
    for com in commands:
        temp=[]
        i=com[0]
        j=com[1]
        k=com[2]
        temp=array[i-1:j]
        temp.sort()
        answer.append(temp[k-1])
        
    return answer


"""
<다른 풀이 1>

*sort와 sorted의 차이: sort는 리스트 자체를 변경해버리며, sorted는 기존의 리스트를 변경하는 것이 아닌, 정렬된 새로운 리스트를 반환함
사용법: 
arr=[1,4,3]
sorted이용. sorted(arr)
sort이용. arr.sort()


"""

def solution(array,commands):
    return list(map(lambda x: sorted(array[x[0]-1:x[1]])[x[2]-1],commands))

#분석
# map(함수, 리스트).. 함수와 리스트를 인자로 받고, 리스트로부터 원소를 하나씩 꺼내어
#                  함수를 적용시킨 다음, 그 결과를 새로운 리스트에 담는다

# lambda 매겨변수: 표현식
#    매개변수: x
#    표현식: sorted(array[x[0]-1:x[1]])
# commands로부터 원소를 하나씩 꺼내어 함수에 적용시킨다

# [1,2,3][0]은 1, [1,2,3][1]은 2, [1,2,3][2]는 3
"""
commands 원소 1. [1,3,2]라고 가정
[2,5,3]의 0번째 인덱스값 -1 : [2,5,3]의 1번째 인덱스 값 = array[2-1:5] = array[1:5]
슬라이싱 후 정렬 -> 새로운 리스트값 반환
새로운리스트[k-1]
즉: x[0]: i, x[1]: j, x[2]: k와 동일해진다

map(): 함수를 적용시킨 후 새로운 리스트에 담았음
list로 형변환 하기 위해 list() 사용. 
map의 반환 값은 map 객체이기 때문.
"""


"""
<다른 풀이2>
"""
def solution(array, commands):
    answer=[]
    for command in commands:
        i,j,k=command
        answer.append(list(sorted(array[i-1:j]))[k-1])

    return answer

    #분석
    # sorted(array[i-1:j]) .. 슬라이싱한 새로운 리스트 반환
    # list(sorted(array[i-1:j]))[k-1] ..k번째 숫자를 반환하기 위해 인덱스 활용
    # answer.append(list(sorted(array[i-1:j]))[k-1]) .. answer 배열에 저장
    
