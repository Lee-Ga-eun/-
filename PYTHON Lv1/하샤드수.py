"""
양의 정수 x가 하샤드 수라면, x의 자릿수의 합으로 x가 나누어져야 한다

입력 10 ==> 출력 true
입력 12 ==> 출력 true
입력 11 ==> 출력 false

"""
# 풀이1
def solution(x):
    answer=0
    for i in str(x):
        answer+=int(i)
    return x%answer==0 or False

# 풀이2

def solution(x):
    return x%sum([int(i) for i in str(x)])==0

#풀이3

def solution(x):
    answer=0
    for i in str(x):
        answer+=int(i)
    return True if x%answer==0 else False


# ***** 자릿수를 파악하는 방법: log10(x)