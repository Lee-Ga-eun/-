
# 정수를 저장한 배열, arr에서 가장 작은 수 리턴
# 리턴하려는 배열이 빈 배열인 경우, [-1]로 리턴

def solution(arr):
    arr.remove(min(arr))
    return arr or [-1]


# 다른 제출자의 코드 리뷰
def solution(n):
    return [i for i in n if i>min(n)] or [-1]

    # min은 그 자체로 for문을 돌리기 때문에 시간 복잡도가 추가된다.
    # 위의 코드처럼 매번 min을 갖고 비교하면, 효율성이 망가진다


"""
이 문제에서 filter를 쓸 수 없는 이유:
"""
# filter 함수의 인자로 들어가는 "함수"의 "리턴" 타입은 "bool" 형이어야 한다