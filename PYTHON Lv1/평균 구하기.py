# 정수를 담고 있는 배열의 평균 구하기

# 나의 풀이
def solution(arr):
    return sum(arr)/len(arr)

# reduce 함수: 누적 합계를 구하기 위해 
"""
<예시>

def solution(x,y):
    return x+y

arr=[i for i in range(1,21)] 
result=0
for value in arr:
    result=solution(result,value)


<reduce사용>
from functools import reduce

def solution(x,y):
    return x+y

arr=[i for i in range(1,21)]
print(reduce(solution,arr))

"""
from functools import reduce
def solution(arr):
    return reduce(lambda x,y : x+y , arr)/len(arr)

"""
arr=[1,2,3,4,5]
<초기값이 없는 경우>
sum1 = reduce(lambda x,y : x+y, arr)
>>
x=1 y=2
x=3 y=3
x=6 y=4
x=10 y=5

<초기값이 있는 경우>
sum2= reduce(lambda x,y: x+y, arr, 0)

x=0, y=1
x=1, y=2
x=3, y=3
x=6, y=4
x=10, y=5

"""
