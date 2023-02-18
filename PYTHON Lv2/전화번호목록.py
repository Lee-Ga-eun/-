"""
접두사 - 119
119123의 접두사는 119 이다 --> O

접두사인 경우가 있으면 false 출력

"""
# 효율성 통과 
def solution(phone_book):
    
    phone_book.sort()
    
    for i in range(len(phone_book)):
        if i!=len(phone_book)-1 and phone_book[i] == phone_book[i+1][:len(phone_book[i])]:
            return False
    return True

answer=solution(["119", "97674223", "1195524421"])
print(answer)

"""
sort()********

a=[1,11,2,3,4]
a.sort()
a
결과: [1, 2, 3, 4, 11]



a=['1','11','2']
a.sort()
a
결과: ['1', '11', '2']

즉, 배열의 원소가 문자열일 때 정렬하면 '사전식' 정렬을 한다

"""

#효율성 통과 X

def solution2(phone_book):
    
    phone_list={}
    
    phone_book.sort(reverse=True)
    
    for i in range(len(phone_book)):
        tmp=phone_book[i][:1]
        print(phone_list)
        if tmp in phone_list:
            lists=phone_list[tmp]
            
            for k in range(len(lists)):
                if phone_book[i] == lists[k][:len(phone_book[i])]:
                    return False
            phone_list[tmp].append(phone_book[i])
            
        else:
            phone_list[tmp]=[phone_book[i]]

                
    return True
answer2=solution2(["119", "97674223", "1195524421"])
print(answer2)

answer3=solution2(["123","456","789"])
print(answer3)