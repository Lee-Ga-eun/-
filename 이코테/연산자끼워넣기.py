
n=6
data=[1,2,3,4,5,6]
add,sub,mul,div=[2,1,1,1]
min_value=1e9
max_value=-1e9
count=0

def dfs(i,now):
    global min_value, max_value,add,sub,mul,div,count
    print("재귀")
    if i==n:
        print('i==n')
        min_value=min(min_value,now)
        max_value=max(max_value,now)
        return
    else:
        if add>0:
            add-=1
            print("더하기",i,(add,sub,mul,div,"now",now+data[i]))
            dfs(i+1,now+data[i])
            print("더하기돌리기",i,(add,sub,mul,div,"now",now))
            add+=1
        if sub>0:
            sub-=1
            print("뺴기",i,(add,sub,mul,div,"now",now+data[i]))
            dfs(i+1,now-data[i])
            sub+=1
            print("빼기돌리기",i,(add,sub,mul,div,"now",now))
        if mul>0:
            mul-=1
            print("곱하기",i,(add,sub,mul,div,"now",now+data[i]))
            dfs(i+1,now*data[i])
            mul+=1
            print("곱하기돌리기",i,(add,sub,mul,div,"now",now))
        if div>0:
            div-=1
            print("나누기",i,(add,sub,mul,div,"now",now+data[i]))
            dfs(i+1,int(now/data[i]))
            div+=1
            print("나누기돌리기",i,(add,sub,mul,div,"now",now))
    print("음?",add,sub,mul,div)

dfs(1,data[0])

print(min_value)
print(max_value)
print(add,sub,mul,div)
print("count",count)