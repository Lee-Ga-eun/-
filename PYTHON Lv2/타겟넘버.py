"""
정수들이 주어졌을 때 , target을 만들 수 있는 방법의 수는?
단, 정수들의 부호는 자유자재로 바꿀 수 있다

ex> [1,1,1,1,1], target=3이면
1+1+1-1-1
1+1+-1+1-1 등
"""

def solution(numbers, target):

    count=[0]

    def calculate(current, index):

        if len(numbers)==index:
            if target==current:
                count[0]+=1
            return
        
        calculate(current+numbers[index],index+1)
        calculate(current-numbers[index],index+1)

        return count[0]
    
    return calculate(0,0)

answer=solution([1,1,1,1,1],3)
print(answer)
