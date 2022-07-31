"""
<입력>
n: 5 (정사각형 지도의 한 변의 길이)
arr1=[9,20,28,18,11] # 10진수
arr2=[30,1,21,17,28]
<출력>
["#####","# # #", "### #", "# ##", "#####"] 

문제:
9를 2진수로 바꾸면 01001이다. 0이 있는 칸엔 공백이, 1이 있는 칸엔 #이 들어간다
arr1과 arr2에 따라 공백과 #으로만 표현되어 있는 암호화된 지도가 만들어지며, 
이 두 지도를 포갰을 때 최종적으로 나오는 지도를 출력한다
"""
def solution(n,arr1,arr2):
    a=[]
    for k in range(len(arr1)): #arr1에 따라 2진수가 들어간 지도
        i=0
        s=[0 for i in range(n)]
        j=arr1[k]
        while True:
            s[i]=(j%2)
            j=j//2
            i+=1
            if j<2:
                s[i]=(j%2)
                break
        s_=list(reversed(s))
        a.append(s_)
    
    b=[]
    for k in range(len(arr2)): # arr2에 따라 2진수가 들어간 지도
        i=0
        s=[0 for i in range(n)]
        j=arr2[k]
        while True:
            s[i]=(j%2)
            j=j//2
            i+=1
            if j<2:
                s[i]=(j%2)
                break
        s_=list(reversed(s))
        b.append(s_)

    for i in range(len(a)): # arr1과 arr2를 포갠다
        #0부터 5까지 . i가 0일 때
        for j in range(len(b)):
            a[i][j]+=b[i][j]
            if a[i][j]==1 or a[i][j]==2:
                a[i][j]='#'
    s=[]
    for i in range(len(a)): #최종 결과 출력
        answer=""       
        for j in range(len(a)):
            if a[i][j]==0:
                a[i][j]=" "
            answer+=a[i][j]
        s.append(answer)
    
    return s


#다른 풀이
def solution(n,arr1,arr2):
    answer=[]
    for i, j in zip(arr1,arr2):
        a12=str(bin(i|j)[2:]) # bin함수는 변환한 2진수 앞에 0b를 출력한다
        a12=a12.rjust(n,"0") # n의 개수에 맞춰 공백을 2번째 매개변수로 채워주며, 최종적으로 오른쪽 정렬이다
        a12=a12.replace('1','#')
        a12=a12.replace('0',' ')
        answer.append(a12)
    return answer