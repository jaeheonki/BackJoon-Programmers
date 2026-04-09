import math

def solution(progresses, speeds):
    res = []
    count = 0
    max_day = 0  # 현재 배포 그룹의 최대 소요일

    for i in range(len(progresses)):
        days = math.ceil((100 - progresses[i]) / speeds[i])

        if count > 0 and max_day < days:
            # 새로운 배포 그룹 시작
            res.append(count)
            count = 0
            max_day = 0

        max_day = max(max_day, days)
        count += 1

    if count > 0:
        res.append(count)

    return res
