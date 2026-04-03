def solution(want, number, discount):
    answer = 0
    wants = []
    for wan, num in zip(want, number) :
        while num > 0:
            wants.append(wan)
            num -= 1
            
    for i in range(len(discount)) :
        if all(wants.count(x) <= discount[i:i+10].count(x) for x in set(wants)) :
            answer += 1
    
    
    return answer