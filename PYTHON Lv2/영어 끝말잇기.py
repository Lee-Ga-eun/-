"""
사람의 수 n과 사람들이 순서대로 말한 단어 words 가 매개변수로 주어질 때, 
가장 먼저 탈락하는 사람의 번호와 그 사람이 자신의 몇 번째 차례에 탈락하는지를 구해서 출력
"""

def solution(n,words):
    finding=[]
    for i in range(len(words)):
        
        if words[i] in finding:
            return [i%n+1,i//n+1]
        finding.append(words[i])
        if i!=len(words)-1:
            if words[i][-1]!=words[i+1][0]:
                return [(i+1)%n+1,(i+1)//n+1]
        
    return [0,0]

answer=solution(3,["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"])
print(answer)