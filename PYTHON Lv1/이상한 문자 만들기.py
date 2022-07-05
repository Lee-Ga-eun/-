"""
입력 "try hello world"
출력 "TrY HeLlO WoRlD"
"""

# 풀이1
def solution(s):
    answer=""
    for i in s.lower().split(" "): #공백을 기준으로 나눠 배열에 넣었다 
        for idx, j in enumerate(i): #i가 try이며 j는 t, r, y
            if idx%2==0:
                j=chr(ord(j)-32) #짝수면 대문자
            answer+=j
        answer+=" "
    return answer[:-1]

"""
테스트 1 〉	통과 (0.01ms, 10.1MB)
테스트 2 〉	통과 (0.01ms, 10.1MB)
테스트 3 〉	통과 (0.01ms, 10.1MB)
테스트 4 〉	통과 (0.04ms, 10.3MB)
테스트 5 〉	통과 (0.02ms, 10.1MB)
테스트 6 〉	통과 (0.01ms, 10MB)
테스트 7 〉	통과 (0.01ms, 10.2MB)
테스트 8 〉	통과 (0.03ms, 9.97MB)
테스트 9 〉	통과 (0.01ms, 10.1MB)
테스트 10 〉통과 (0.03ms, 10.3MB)
테스트 11 〉통과 (0.04ms, 10.3MB)
테스트 12 〉통과 (0.02ms, 10.1MB)
테스트 13 〉통과 (0.01ms, 10.1MB)
테스트 14 〉통과 (0.01ms, 10.2MB)
테스트 15 〉통과 (0.02ms, 10.1MB)
테스트 16 〉통과 (0.02ms, 10.1MB)
"""

def solution(s):
    return " ".join(map(lambda x: "".join([a.lower() if i%2 else a.upper() for i,a in enumerate(x)]),s.split(" ")))

    # if condition에 해당하는 값만 출력하기
    for i in v:
        if i==12:
            print(i)
    ##
    [i for i in v if i==12]

    #for문에 해당하는 각각의 원소가 if condition에 해당하는지 아닌지
    for i in v:
        if i==12:
            print(i)
        else:
            print("no")
    ##
    [i if i==12 else "no" for i in v]