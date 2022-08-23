"""
스파이가 가진 의상들이 담긴 2차원 배열 clothes가 주어질 때, 서로 다른 옷의 조합의 수를
return한다

<입력 예>
clothes=[["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
<출력 예>
5

.. 조합 가능 의상..
1. yellow_hat
2. blue_sunglasses
3. green_turban
4. yellow_hat + blue_sunglasses
5. green_turban + blue_sunglasses
"""


#나의 풀이 해설:
"""
1. 각 종류별로 옷들을 정리한 딕셔너리를 생성한다.
2. 특정 종류의 옷을 입지 않을 수 있다. 이를 위해서, 각 종류마다 입지 않는다는 의미로 개수에 1을 더한다
3. 한 종류 당 두 개 이상의 옷을 입진 않는다. 따라서 조합은
   (1번 종류의 모든 의상의 개수+1)*(2번 종류의 모든 의상의 개수)...
4. 단, 각 종류마다 '없음'을 대입했기 때문에, 모두 입지 않을 확률인 1을 빼야 한다.

"""
def solution(clothes):
    # 딕셔너리 만들기
    j=0
    category={}
    for i in range(len(clothes)):
        i=len(clothes[i])-1
        tmp=clothes[j][i]
        category[tmp]=0
        j+=1
    # 값 넣기
    for i in clothes:
        tmp=i[-1::][0]
        category[tmp]+=len(i)-1
    print(list(category.values()))
    
    k=1
    for i in list(category.values()):
        k*=(i+1)
        
    
    
    return k-1