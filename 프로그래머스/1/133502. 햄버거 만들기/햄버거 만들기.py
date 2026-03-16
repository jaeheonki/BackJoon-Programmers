def solution(ingredient):
    hamburger = []
    success = [1, 2, 3, 1]
    cnt = 0
    for i in ingredient :
        hamburger.append(i)
        if hamburger[-4:] == success :
            cnt += 1
            for j in range(4):
                hamburger.pop()
        
    return cnt
            