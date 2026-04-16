from collections import deque

def solution(n):
    res = deque()
    def recur_124(n) :
        quo = n // 3
        rem = n % 3
        nonlocal res
        
        if n == 0 :
            return ''.join(res)
        if rem == 1 :
            res.appendleft('1')
            return recur_124(quo)
        elif rem == 2 :
            res.appendleft('2')
            return recur_124(quo)
        else :
            res.appendleft('4')
            return recur_124(quo-1)
    return recur_124(n)