# 한 상자에 담으려는 귤의 개수 k, 귤의 크기를 담은 배열 tangerine
# 귤 k개를 고를 때 크기가 서로 다른 종류의 수의 최솟값을 return

#runtime error
# tangerine에서 중복을 제거해 크기 넘버링 정보만 빼낸 후, 이 크기를 갖고 있는 것들을 count하려 했다.
# 그러나 1번 귤이 100개이고 배열에 정렬되지 않은, 흩어진 상태라면 count해내는 데 시간이 많이 소요될 것이다
def solution1(k,tangerine):
    set_tan=list(set(tangerine))
    tangerine_dict={}
    for i in range(len(set_tan)):
        print(tangerine.count(set_tan[i]))
        tangerine_dict[set_tan[i]]=tangerine.count(set_tan[i])
    tmp=sorted(tangerine_dict.values(),reverse=True)
    
    count=0
    result=0
    for i in range(len(tmp)):
        k-=tmp[i]
        count+=1
        if k==0:
            result=count
            break
        elif k<0:
            result=count
            break
        
    return result

# 두번째 시도, 잘못된 접근
# count하는 횟수를 줄이기 위해 최대값을 먼저 구하고 빈 배열에 집어 넣은 후, 배열의 길이가 k를 초과하면
# count를 종료하도록 하려 했다. 그러나, 많은 개수가 중요하지 최대값이 중요한 것이 아니어서 잘못된 접근이었다.
def solution2(k,tangerine):
    set_tan=list(set(tangerine))
    tangerine_dict={}
    for i in range(len(set_tan)):
        print(tangerine.count(set_tan[i]))
        tangerine_dict[set_tan[i]]=tangerine.count(set_tan[i])
    tmp=sorted(tangerine_dict.values(),reverse=True)
    
    count=0
    result=0
    for i in range(len(tmp)):
        k-=tmp[i]
        count+=1
        if k==0:
            result=count
            break
        elif k<0:
            result=count
            break
        
    return result




# 통과
# Counter 라이브러리를 사용하면 배열의 모든 원소에 대해 딕셔너리 형태로 만들어준다. 
# 즉, 1번의 과정들을 한 줄로 해결한다
def solution3(k,tangerine):
    from collections import Counter
    tmp=Counter(tangerine)
    tmp=sorted(tmp.values(),reverse=True)
    print(tmp)
    count=0
    t=0
    if(k<tmp[0]):return 1
        
    for i in range(len(tmp)):
        t+=tmp[i]
        count+=1
        if(t>=k):
            return count

solution3(6,[1,3,2,5,4,5,2,3])