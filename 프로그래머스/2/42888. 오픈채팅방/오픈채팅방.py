from collections import defaultdict

def solution(record):
    access_list = []
    member_dict = defaultdict(str)
    res = []
    
    #access_list 저장, 멤버 이름 업데이트
    for rec in record :
        parts = rec.split()
        #change, enter 경우
        if len(parts) == 3 :
            access, user_id, nickname = parts
            #user_id에 맞는 닉네임 업데이트
            member_dict[user_id] = nickname
            #enter
            if access == 'Enter' :
                access_list.append([access, user_id])
            #user_id에 맞는 닉네임 업데이트
            member_dict[user_id] = nickname
        #Leave 경우
        else :
            access, user_id = parts
            access_list.append([access, user_id])
    
    #최종 메세지 업데이트
    for access in access_list :
        name = member_dict[access[1]]
        if access[0] == 'Enter' :
            message = f'{name}님이 들어왔습니다.'
            res.append(message)
        else :
            message = f'{name}님이 나갔습니다.'
            res.append(message)
            
    return res
            
    