def solution(s):
    num_list = list(map(int, s.split()))
    res = str(min(num_list)) + " " + str(max(num_list))
    return res