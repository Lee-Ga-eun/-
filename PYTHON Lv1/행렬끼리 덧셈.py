# 차원이 같은 행렬들끼리의 합

# 풀이1
def solution(arr1,arr2):
    for i in range(0,len(arr1)):
        for j in range(0,len(arr1[0])):
            arr1[i][j]+=arr2[i][j]
    return arr1
    # 포인트::::::: len(arr1)와 len(arr1[0])

#풀이2 : numpy이용

import numpy as np
def solution(A,B):
    A=np.array(A)
    B=np.array(B)
    print(A)
    print(B)
    answer=A+B
    return answer.tolist()

#풀이3: zip함수 이용

def solution(A,B):
    answer=[]
    for a,b in zip(A,B):
        print(a,b)
        l=[]
        for x,y in zip(a,b):
            print(x,"+",y,"는 ",x+y)
            l.append(x+y)
        answer.append(l)
        print("answer은",answer)
    return answer

    """
    [1, 2] [3, 4]
    1 + 3 는  4
    2 + 4 는  6
    answer은 [[4, 6]]
    
    [2, 3] [5, 6]
    2 + 5 는  7
    3 + 6 는  9
    answer은 [[4, 6], [7, 9]]
    """