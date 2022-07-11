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

