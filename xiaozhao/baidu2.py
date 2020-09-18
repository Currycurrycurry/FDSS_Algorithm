N = int(input())
board = []
for _ in range(N):
    board.append(list(map(int, input().split(' '))))
# board = [
#     [1,1,1,1],
#     [0,1,0,1],
#     [1,1,0,1],
#     [0,0,1,0]
# ]
# print(board)
def turn0to1(board):
    if not board:
        return None
    row_len = len(board)
    col_len = len(board[0])
    x = [1, -1, 0, 0]
    y = [0, 0, 1, -1]
    queue = []
    def helper(r, c, board):
        # change
        queue.append(r*col_len+c)
        while len(queue) > 0:
            temp = queue.pop(0)
            for i in range(4):
                rr = x[i] + temp // col_len
                cc = y[i] + temp % col_len
                if rr >= 0 and rr < row_len and cc >= 0 and cc < col_len and board[rr][cc] == 0:
                    board[rr][cc] = 2
                    queue.append(rr*col_len+cc)

    # row
    for i in range(col_len):
        firstLine = board[0][i]
        if firstLine == 0:
            board[0][i] = 2
            helper(0, i, board)
        lastLine = board[-1][i]
        if lastLine == 0:
            board[row_len-1][i] = 2
            helper(row_len-1, i, board)
    # col
    for j in range(1, row_len-1):
        firstCol = board[j][0]
        if firstCol == 0:
            board[j][0] = 2
            helper(j, 0, board)
        lastCol = board[j][col_len-1]
        if lastCol == 0:
            board[j][col_len-1] = 2
            helper(j, col_len-1, board)
    for i in range(row_len):
        for j in range(col_len):
            if board[i][j] == 0:
                board[i][j] = 1
            if board[i][j] == 2:
                board[i][j] = 0
    return board
turn0to1(board)
for i in range(len(board)):
    print(' '.join(map(str, board[i])))
    
