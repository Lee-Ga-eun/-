# n이 양의 정수 x의 제곱이라면, x+1의 제곱을 리턴하고,
# n이 양의 정수 x의 제곱이 아니라면, -1을 리턴하라

#나의 풀이
def solution(n):
    if n**0.5 == int(n**0.5):
        return int(((n)**0.5+1)**2)
    return -1

# 다른 풀이
def solution(n):
    sqrt= n **(1/2)

    if sqrt % 1 == 0 :
        return (sqrt+1)**2
    return -1
