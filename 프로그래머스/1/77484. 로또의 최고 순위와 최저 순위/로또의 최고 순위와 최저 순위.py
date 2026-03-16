def lotto_count(cnt) :
    if cnt == 6 :
        return 1
    elif cnt == 5 :
        return 2
    elif cnt == 4 :
        return 3
    elif cnt == 3 : 
        return 4
    elif cnt == 2 :
        return 5
    else :
        return 6

def solution(lottos, win_nums):
    worst = 0
    best = 0
    res = []
    
    for num in lottos :
        
        if num in win_nums :
            worst += 1
            best += 1
            
        elif num == 0 :
            best += 1
        else :
            continue
    
    res.append(lotto_count(best))
    res.append(lotto_count(worst))
    
    return res

        