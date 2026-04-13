def solution(m, n, board):
    board = [list(row) for row in board]
    cnt = 0
    while True:
        check_board = [[0] * n for _ in range(m)]
    #4개의 블록 겹치는지 검사
        for i in range(m-1):
            for j in range(n-1):
                if board[i][j] is not None and board[i][j] == board[i + 1][j] == board[i][j+1] == board [i+1][j+1] :
                    check_board[i][j] = 1
                    check_board[i+1][j] = 1
                    check_board[i][j+1] = 1
                    check_board[i+ 1][j + 1] = 1

        # 없앨 블록이 없으면 종료
        if sum(row.count(1) for row in check_board) == 0:
            break

        #없애야할 블록 없애기
        for i in range(m) :
            for j in range(n) :
                if check_board[i][j] == 1 :
                    cnt += 1
                    board[i][j] = None


        #블록 내리기
        for j in range(n):  # j로 열 순회
            col = [board[i][j] for i in range(m) if board[i][j] is not None]
            none_cnt = m - len(col)
            new_col = [None] * none_cnt + col
            for i in range(m):
                board[i][j] = new_col[i]
                    
    return cnt
                