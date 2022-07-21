"""
<2021 카카오 채용연계 인턴십>

네오와 프로도가 숫자 놀이를 하고 있다. 
네오가 영어(숫자를 영어로)와 숫자를 섞으면, 프로도는 그걸 전부 숫자로 바꿔야 한다 

입력: "one4seveneight"
출력: 1478
"""

# 나의 풀이
"""
생각1. 딕셔너리를 만들었을 때, 어떻게 value를 가져올까
생각2. str에서 인덱스로 접근했을 때, 대입으로 값 변경이 불가능하다.
        에러 메시지> 'str' object does not support item assignment
생각3. find함수로 접근했을 때, 시작 인덱스만 가져온다. 운이 나쁘게, 붙어있는 두 영단어가 존재하는 영단어가 될 경우 복잡해질 것이다
"""

def solution(s):
    # s="twoonethree"
    alpha_dict={0:'zero',1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight', 9:'nine'} # 숫자 0부터 9까지 딕셔너리를 만들어준다
    for i in alpha_dict: # 숫자 정보가 있는 딕셔너리를 처음부터 끝까지 돈다. 그러면 주어진 문자열의 숫자가 영단어로 표기되어 있는 모든 것을 탐색할 수 있을 것이다
        changing=alpha_dict.get(i) #영단어를 숫자로 바꿔야 하기 때문에, value를 뽑고, 그것을 변수에 저장해 활용할 것이다
        locate=s.find(changing) # s 문자열에서, value가 들어간 시작점을 찾아낸다
        if (s.find(changing, locate, locate+len(changing))) == locate: # 세번째 매개변수까지 포함한 find함수의 결과값은 시작 인덱스이다. 즉 locate와 똑같으며, 이 방식으로 생각3을 해결할 수 있다
            # 즉, s에서 two 는 0 인덱스에 있으며, two의 길이는 3이다. s 문자열에서 0부터 3까지 탐색하고 그것이 정확히 원하는 영단어와 맞아 떨어지게 필터링을 하기 위해 if문을 썼다
            s=s.replace(changing, str(i)) #replace함수를 이용하여 영단어를 숫자로 바꿔준다. 딕셔너리가 0부터 9까지 정렬되어 있으므로, str(i)로 처리해 변경해준다
    return int(s) # 오롯이 정수형으로 리턴한다 그렇지 않으면 문자형으로 리턴된다


# 딕셔너리 key값과 value를 for문으로 간단하게
for key,value in alpha_dict.items():
    print(key,value)