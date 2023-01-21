# 10일 동안 회원 자격 부여
# 자신이 원하는 제품과 수량이 회원 자격이 부여된 날짜까지 전부 구매가 가능하다면 ?
# 원하는 제품을 모두 할인 받을 수 있는 회원 등록 날짜의 총 일수를 출력
# 1일 1개 구매 가능

"""
입력 예:
want= ["banana", "apple", "rice", "pork", "pot"]
number = [3,2,2,2,1] # 즉, 바나나 3개, 사과 2개, 쌀 2개 ,돼지고기2개, 냄비1개 구매할 것
discount: ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"] # 날짜별 할인 품목

출력:3 # 셋째날 or 넷째날 or 다섯째날에 회원권 등록시 모두 구매가 가능함


"""


def solution(want,number,discount):
    import collections
#     등록이 가능한 날짜의 총 수를 리턴
    count=0
    for i in range(len(discount)):
        tmp=discount[i:10+i] # 10일 동안 자격이 부여되기 때문 (특정 날짜부터 10일 내에 원하는 걸 모두 사야함)
        
        check=True
        check_arr=[]
        for j in range(len(want)):
            if tmp.count(want[j])>=number[j]: # 제품 하나씩 보았을 때 전부 10일 내에 구매가 가능하면 -> count 증가
                check=True
                check_arr.append(check)
            else:
                check=False
                check_arr.append(check)
                
            if j==len(want)-1 and False not in check_arr: #True가 tmp길이와 일치하다면, 모두 구매가 가능하단 것
                count+=1
                
                #return i+1

        #print(tmp)
    return count

answer=solution(["banana", "apple", "rice", "pork", "pot"], [3, 2, 2, 2, 1], ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"])
print(answer)


# 다른 사람 풀이
"""
***
{'banana': 3, 'apple': 2, 'rice': 2, 'pork': 2, 'pot': 1}==Counter({'banana': 3, 'apple': 2, 'rice': 2, 'pork': 2, 'pot': 1})
 --> 결과 : True
"""
from collections import Counter
def solution1(want, number, discount):
    answer = 0
    dic = {}
    for i in range(len(want)):
        dic[want[i]] = number[i] #구매해야할 품목 및 개수 딕셔너리 생성

    for i in range(len(discount)-9):
        print(dic)
        print(Counter(discount[i:i+10])) # Counter를 이용하여 슬라이싱한 배열에 대해 딕셔너리 생성
        if dic == Counter(discount[i:i+10]): # 딕셔너리A == Counter(딕셔너리A)
            answer += 1

    return answer