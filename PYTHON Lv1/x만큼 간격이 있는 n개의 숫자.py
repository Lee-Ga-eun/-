# x는 시작 정수이기도 하며, 동시에 증가값이다
# n은 리스트 개수의 조건이다
# x:2 , [2,4,6,8,10]
# x x+x x+x+x x+x+x+x x+x+x+x+x
# x x+x*1 x+x*2 x+x*3

#나의 풀이
def solution(x,n):
    return [x+x*i for i in range(n)]

# 다른 풀이
def solution(x,n):  
    return [i for i in range(x, x*(n+1), x)]
