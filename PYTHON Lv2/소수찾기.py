"""
한 숫자가 적힌 종이 조각이 흩어져 있다.
흩어진 종이 조각을 붙여 소수를 몇 개 만들 수 있는지 알아보자

ex) 입력: 13 -> 1이 적힌 카드 한 장, 3이 적힌 카드 1장이 있단 뜻으로 이걸로 1, 3, 13 그리고 31을 만들 수 있으며,
이때 3, 13, 31 모두 소수이기 때문에 결과는 3이다
"""


def solution(numbers):
    l=[numbers[i] for i in range(len(numbers))]
    from itertools import permutations
    c=set()
    def combi(l,number):
        return list(permutations(l,number))
    
    for i in range(len(l)):
        tmp=combi(l,i+1)
        for j in range(len(tmp)):
            c.add(int(''.join(tmp[j])))
    c=list(c)
    #print(c)
    answer=0
    for i in range(len(c)):
        if c[i]==0 or c[i]==1:
            continue
        for j in range(1,c[i]):
            if j!=1 and c[i]%j==0:
                break
            if j==c[i]-1:
                #print(c[i])
                answer+=1            
    return answer

answer=solution('13')
print(answer)