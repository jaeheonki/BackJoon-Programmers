def solution(s):
    #stack 활용
    stack = []
    for c in s :
        #stack이 비어있거나, 전 문자와 같을때(짝지어져 있을 때)
        if stack and stack[-1] == c :
            stack.pop()
        else : 
            stack.append(c)
    
    if len(stack) == 0 :
        return 1
    else :
        return 0