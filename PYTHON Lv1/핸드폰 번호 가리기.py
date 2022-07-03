"""
문제: 뒷번호 4자리 제외 모두 가린다
"""

# 풀이1

def solution(phone_number):
    return '*'*(len(phone_number[:-4]))+phone_number[-4::]

    # 주의: 
    # "0101234"[:-4:-1] ==> 432 즉, 뒤에서부터 출력된다 (원하는 방향과 반대)