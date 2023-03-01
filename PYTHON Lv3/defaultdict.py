from collections import defaultdict

# 초기값이 설정한 형태로 자동으로 저장되는 형식

d_int=defaultdict(int) # int형식으로 지정
d_int['key1']
print("int형식 딕셔너리 d_int",d_int)
d_int['key2']='파괴'
print("굳이 지정형식으로 값을 저장하지 않아도 된다 d_int:",d_int)


d_list=defaultdict(list) #list형식으로 지정
d_list['key1'] # value를 넣지 않았기 때문에 빈 리스트가 저장됨
d_list['key2']='value2'
print(d_list)