"""
입력: numbers 
  ==> 0부터 9까지의 숫자 중 일부가 들어있는 배열

출력: 0부터 9까지의 숫자 중 numbers에 해당하지 않는 값들끼리 더해 리턴
"""

# 나의 풀이
def solution(numbers):
    return sum(list(filter(lambda x:x not in numbers, [i for i in range(10)])))

    # 순간 filter와 map이 헷갈려 filter 대신 map을 써보았다.
    """
    list(map(lambda x:x not in [1,2,3,4,6,7,8,0], [i for i in range(10)]))의 결과는?!
    .
    .
    .
    [False, False, False, False, False, True, False, False, False, True]

    이떄, sum(list(map(lambda x:x not in [1,2,3,4,6,7,8,0], [i for i in range(10)])))을
    실수로 눌렀더니, 2가 나왔다. True+True의 결과는 2이기 때문이다 ^^
    """