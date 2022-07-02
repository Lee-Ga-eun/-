"""
입력 12345 ==> 출력 [5,4,3,2,1]
자연수는 iteral이 아니다
"""

# 풀이1: 문자열로 형변환하여 배열 만들기
def solution(n):
    answer=[]
    for i in str(n):
        answer.append(int(n))
    answer.reverse()
    return answer


# 풀이2: 나머지 이용하기
"""
EX. 12345 % 10 = 5
    1234 % 10 = 4
    123 % 10 = 3
    12 % 10 = 2
    1
"""
def solution(n):
    answer=[]
    while(len(str(n))>1):
        answer.append(n%10)
        n=n//10
    answer.append(n)
    return answer

    """
    통과 (0.01ms, 10.1MB)
    테스트 2 〉	통과 (0.01ms, 10.2MB)
    테스트 3 〉	통과 (0.00ms, 10.1MB)
    테스트 4 〉	통과 (0.01ms, 10.2MB)
    테스트 5 〉	통과 (0.01ms, 10.2MB)
    테스트 6 〉	통과 (0.01ms, 9.92MB)
    테스트 7 〉	통과 (0.01ms, 10.1MB)
    테스트 8 〉	통과 (0.01ms, 10.2MB)
    테스트 9 〉	통과 (0.01ms, 10.3MB)
    테스트 10 〉	통과 (0.00ms, 10.2MB)
    테스트 11 〉	통과 (0.00ms, 10.1MB)
    테스트 12 〉	통과 (0.01ms, 10.2MB)
    테스트 13 〉	통과 (0.01ms, 10.1MB)
    """

# 풀이3
def solution(n):
    return list(map(int, reversed(str(n))))

    # list(reversed(str(n))) ==> ['5','4','3','2','1']
    # reversed(str(n)) ==> <reversed at 0x7fe5e9351430>
    # reversed() 함수는 자료구조에 담긴 원소들을 역순으로 순회할 수 있도록 "iterator"를 결과값으로 반환한다

    # map(function, iterable)


# 풀이4

def solution(n):
    return [int(i) for i in str(n)][::-1]


# 풀이 3 & 4

def soltuion(n):
    return list(map(int, list(str(n))[::-1]))

    # list('1234') ==> ['1','2','3','4']
    