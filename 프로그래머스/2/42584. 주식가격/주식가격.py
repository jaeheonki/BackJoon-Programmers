def solution(prices):
    res = []
    last_index = len(prices) - 1
    
    for i in range(len(prices)) :
        if i == last_index : 
            res.append(0)
        
        for j in range(i + 1, len(prices)) :
            if prices[i] > prices[j] :
                res.append(j - i)
                break
            elif j == last_index :
                res.append(last_index - i)
    
    return res
            