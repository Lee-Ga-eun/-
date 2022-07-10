# 입력> n:118372
# return> 873211

def solution(n):
    return int("".join(sorted(str(n), reverse=True)))