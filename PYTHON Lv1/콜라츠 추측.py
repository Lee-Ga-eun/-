"""
입력된 수가 짝수라면 2로 나눈다
입력된 수가 홀수라면 3을 곱하고 1을 더한다
입력된 수가 위의 식을 통해 1이 될 때까지 반복한다
500번 이상을 반복하게 된다면 -1을 리턴한다
"""
def solution(n):
    answer=0
    while(True):
        if n==1: break
        if n%2==0: n = n//2 #짝수라면 2로 나눈다
        else: n = n*3 + 1 #홀수라면
        answer=answer+1
        if answer==500:
            return -1
        
    return answer