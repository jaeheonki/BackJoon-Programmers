import math

def solution(progresses, speeds):
    stack = []  #기술 배포 대기 스택
    res = []
    today = 0
    for i in range(len(progresses)) :
        # days : 기능 개발까지 걸리는 일수
        # 나눗셈의 결과가 ex. 7.3일 이렇게 나오면 8일이 걸리므로 math.ceil 사용
        days = math.ceil((100 - progresses[i]) / speeds[i])
        if stack and max(stack) < days : 
            res.append(len(stack))
            stack.clear()
            stack.append(days)
            
            print(stack)
        else :
            stack.append(days)
            
    if stack :
        res.append(len(stack))
        
    return res