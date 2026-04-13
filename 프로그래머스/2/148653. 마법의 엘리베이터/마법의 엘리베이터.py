def solution(storey):
    num = storey
    cnt = 0
    while num :
        #현재 1의 자리
        digit = num % 10
        #다음에 들어갈 num
        num = num // 10
        #num % 10 : 다음 10의 자릿수
        if digit > 5 or (digit == 5 and (num % 10 + 1) > 5):
            cnt += (10 - digit)
            num += 1
        else :
            cnt += digit
    return cnt