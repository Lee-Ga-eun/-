
def solution1(arr,divisor):
    answer=[]
    for i in arr:
        if i%divisor==0: answer.append(i)
    if answer==[]: answer.append(-1) 
    return sorted(answer)

def solution2(arr,divisor):
    answer=[i for i in arr if i%divisor==0]
    if answer==[]: answer.append(-1)
    return sorted(answer)

def solution3(arr,divisor):
    return sorted([i for i in arr if i%divisor==0]) or [-1]

#파이썬은 or앞이 참일 경우 해당 값까지만, 거짓일 경우 뒤에 것까지 호출

def solution4(arr,divisor):
    answer=[i for i in arr if i%divisor==0]
    if answer==[]: answer.append(-1)
    answer.sort()
    return answer #return answer.sort() 는 None 반환됨

# 파이썬은 list.sort(), list.append(), random.shuffle()과 같이
# 데이터를 변경하는 메서드에서 None을 반환하며 변경되었다는 사실을 암시한다 생각
# 따라서 sort()는 반환값이 없다


# return - or문 연습
def solution(a):
    return [10] or [i for i in a if i==1] 
# 참 거짓을 따질 것 없이 [10]이 반환된다


