import copy
def solution(msg):
    answer=[]
    dic=dict()
    for i in range(1,27):
        dic[i]=chr(i+64)
    msgc=copy.deepcopy(msg)
    last_num=list(dic.keys())[-1]
    
    later=0
    for i in range(len(msg)):
        v=dic.values()
        cut=0
        for j in range(len(msgc)):
            if(msgc[:j+1] in v):
                #print(msgc[:j+1])
                cut+=1
            else:
                answer.append(msgc[:j])
                last_num+=1
                dic[last_num]=msgc[:j+1]
                break
        msgc=msgc[cut:]
        if(len(msgc)==0 and cut!=0):
            later=cut
       # print(msgc)
            
    new_dic={value: key for key, value in dic.items()}
    result=[]
    for i in answer:
        result.append(new_dic[i]) 
    
    result.append(new_dic[msg[len(msg)-later:]])
    return result

print(solution('KAKAO'))