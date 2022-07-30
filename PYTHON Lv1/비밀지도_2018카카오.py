
def solution(n,arr1,arr2):
    a=[]
    for k in range(len(arr1)):
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
    for k in range(len(arr2)):
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
    for i in range(n):    
        for a_,b_ in zip(a,b):
              print(a_[0])
    return a,b