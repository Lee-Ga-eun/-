"""
숫자가 담긴 리스트에서 3개의 수를 골라 더했을 때 소수가 되는 경우의 수

"""

def solution(nums):
    from itertools import combinations
    # 순서 고려는 필요 없어서, permutations는 안 써도 됨
    count=0
    p=list(combinations(nums,3))
    for i in range(len(p)):
        t=sum(p[i])
        for i in range(2,t):
            if t%i==0:
                break
            if i==t-1:
                count+=1

    return count