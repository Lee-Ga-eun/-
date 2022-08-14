
"""
올바른 괄호이면 true 아니면 false
"()()" true
(())() true
)()( false
(()( false
"""

from collections import deque
def solution(s):
    _open=deque()
    _close=deque()
    s=deque(s)
    
    if s[0]!='(' or len(s)<=2:
        return False
    #i=0
    while s: # 모두 탐색해야 끝남
        if s[0]=='(':
            _open.append(s.popleft())
        if s[0]==')':
            _close.append(s.popleft())
        
        if len(_open)!=0 and len(_close)!=0: #괄호 짝 맞추기
            _open.pop() #스택
            _close.popleft() #큐
            if len(s)!=0 and len(_open)==0 and s[0]==')': # 짝을 맞췄으나 그 다음 값이 )일 때
                return False
            
        if len(s)==1 and s[0]=='(': # 큐에 넣을 마지막 값이 (일 때
            break
        
    return len(_open)==0 and len(_close)==0  #true or false
        
        