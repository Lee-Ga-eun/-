#정수 배열 numbers에서 서로 다른 인덱스에 있는 두 개의 수를 뽑아 더해서 만들 수 있는 모든 수를 오름차순으로 리턴

#나의 풀이
def solution(numbers):
    result=[]
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i==j: continue
            result.append(numbers[i]+numbers[j])
    return sorted(set(result))

    #배열을 순차적으로 탐색할 때, 초기 위치를 설정하는 방법:
    """
    for i in range(1, len(numbers)):
        ..
    """

    #참고로, 
    """
    for i in enumerate(numbers):
        print(i)의 결과는 tuble이다.
    
    (0,5)[1]은 5
    """
