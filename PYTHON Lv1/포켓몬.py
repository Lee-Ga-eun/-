"""
같은 종류의 포켓몬은 같은 번호를 갖고 있으며, 연구실에 있는 포켓몬 N 중 N/2마리를 가져갈 수 있다.
예를 들어, 4마리의 포켓몬 중 2마리를 고르는 방법은 6가지가 있다. (4c2)
N마리 포켓몬의 종류가 담긴 배열 nums가 매개변수로 주어질 때, N/2마리의 포켓몬을 선택하는 방법 중,
가장 많은 종류의 포켓몬을 선택해 그때의 종류 개수를 return한다
"""

#나의 풀이
def solution(nums):
    if len(nums)//2<=len(set(nums)):
        return len(nums)//2
    return len(set(nums))
    """
    풀이 해석: N//2의 개수를 가져갈 수 있다. 
    이때 포켓몬들의 종류의 개수를 파악한다. 최대한 많은 종류를 가져가야 하기 때문이다.
    4개를 가져갈 수 있다고 할 때, 종류가 3개라면, 3이 return.
                            종류가 4개라면, 4가 return.
                            종류가 5개라면, 4가 return
                            종류가 6개라면, 6이 return
    이를 이용해 문제를 풀었다
    """

#다른 풀이
def solution(nums):
    return min(len(nums)//2,len(set(nums)))