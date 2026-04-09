from collections import deque
#큐를 순회하여 최대 우선순위 찾는 함수
def max_queue(queue) :
    max = float('-inf')
    #queue 순회
    for i, (_, priority) in enumerate(queue) :
        if priority > max :
            max = priority
    
    return max

def solution(priorities, location):
    # location(key) : priorities(value)값을 가지는 딕셔너리 생성
    priorities_dict = {index : value for index, value in enumerate(priorities)}
    #위 딕셔너리의 키/값을 가져와 queue생성(deque)
    wait_queue = deque(priorities_dict.items())
    
    max_priority = max_queue(wait_queue)
    
    #cnt 번째로 실행되는 프로세스
    cnt = 1
    
    #wait_queue 순회
    while wait_queue :
        loc, priority = wait_queue.popleft()
        #우선순위가 더 높은 프로세스가 있다면
        if priority < max_priority :
            wait_queue.append((loc, priority))
        #없다면 그대로 빼고(프로세스 실행), 실행한 프로세스가 찾으려는 process인지 검사
        else :
            #실행했으니 max우선순위 갱신, 마지막에 cnt + 1
            max_priority = max_queue(wait_queue)
            if loc == location :
                return cnt
            cnt += 1
                
            
        
    
    