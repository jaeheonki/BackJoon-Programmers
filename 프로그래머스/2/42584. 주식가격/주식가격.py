def solution(prices):
    n = len(prices)
    res = [0] * n
    stack = []  # 인덱스를 저장

    for i in range(n):
        # 현재 가격이 스택 top의 가격보다 낮으면 → 가격이 떨어진 시점
        while stack and prices[stack[-1]] > prices[i]:
            idx = stack.pop()
            res[idx] = i - idx  # 버틴 시간
        stack.append(i)

    # 스택에 남은 건 끝까지 가격이 안 떨어진 경우
    while stack:
        idx = stack.pop()
        res[idx] = n - 1 - idx

    return res
