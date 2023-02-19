# 서로소 찾기 == 유니온 파인드
# 부모 테이블이 있어야 한다

# 유니온: 하나의 집합으로 만드는 과정 --> 각 원소의 부모 노드를 찾은 뒤, 합친다. 이때 큰 노드의 부모가 작은 노드의 부모값으로 변경된다
# 파인드: 부모 노드를 찾는 과정., 노드 3의 부모: 2 -> 노드2의 부모:1 -> 노드1의 부모: 1 --> 결과=1


"""
문제:
N+1개로 팀이 이루어져있고, 각 관계는 M개 입력하여 설정한다
관계 앞이 0이면 팀 합치기 수행, 1이면 같은 팀인지 확인한 후 같은 팀이면 yes 다른 팀이면 no를 출력 
"""
def union(parent,a,b):
    a=find_parent(parent,a)
    b=find_parent(parent,b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b

def find_parent(parent,x):
    if parent[x]!=x: #현재가 최종 루트가 아니라면
        parent[x]=find_parent(parent,parent[x]) # parent[x]에 부모노드가 적혀 있으니까, 그 노드로 이동해서 탐색한다
    return parent[x]
        
    

# 몇 개의 팀인지, 몇 번의 연산을 수행해야 하는지
n,m = map(int, input().split())
# 부모 테이블 초기화
parent=[0]*(n+1) # 팀은 n+1개
# 부모 테이블 다시 초기화 (각 원소의 부모노드를 자기 자신으로)
for i in range(len(parent)):
    parent[i]=i

for i in range(m): # 연산 확인
    # 0인지 1인지에 따라 a와 b에서 합집합을 수행하거나 찾기를 수행한다
    operation, a, b= map(int, input().split())
    
    if operation==0: #합치기 연산
        union(parent,a,b)
        print(parent)
    elif operation==1:
        if find_parent(parent,a)==find_parent(parent,b):
            print("YES")
        else:
            print("NO")
        print(parent)