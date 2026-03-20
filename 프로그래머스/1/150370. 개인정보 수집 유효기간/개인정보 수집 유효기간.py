from collections import defaultdict

def solution(today, terms, privacies):
    terms_dict = defaultdict(int)
    today = int(today.replace('.', ''))
    res = []
    
    
    #terms_dict
    for term in terms : 
        t, month = term.split()
        terms_dict[t] = int(month)
        
    
    for i, privacy in enumerate(privacies) :
        date, t = privacy.split()
        year, month, day = map(int, date.split('.'))
        
        ex_month = terms_dict[t] #해당 약관의 개월 수
        
        #날짜 더하기
        month = month + ex_month
        
        if month  > 12 :
            year += (month - 1) // 12
            month = month % 12 if month % 12 != 0 else 12
            
        expire_day = int(f'{year}{str(month).zfill(2)}{str(day).zfill(2)}')
        
        if int(expire_day) <= int(today) :
            res.append(i+1)
            
    return res