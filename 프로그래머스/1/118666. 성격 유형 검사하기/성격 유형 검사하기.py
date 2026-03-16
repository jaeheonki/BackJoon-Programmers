def solution(survey, choices):
    mbti = {'R' : 0, 'T' : 0, 'C' : 0, 'F' : 0, 'J' : 0, 'M' : 0, 'A' : 0, 'N' : 0}
    res = ''
    
    for i in range(len(survey)) :
        if choices[i] > 4 :
            mbti[survey[i][1]] += (choices[i] - 4)
        elif choices[i] < 4 :
            mbti[survey[i][0]] -= (choices[i] - 4)
        else :
            continue
    
    if mbti['R'] >= mbti['T'] :
        res += 'R'
    else :
        res += 'T'
        
    if mbti['C'] >= mbti['F'] :
        res += 'C'
    else :
        res += 'F'
        
    if mbti['J'] >= mbti['M'] :
        res += 'J'
    else :
        res += 'M'
        
    if mbti['A'] >= mbti['N'] :
        res += 'A'
    else :
        res += 'N'
        
    return res