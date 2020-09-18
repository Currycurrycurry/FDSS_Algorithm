# 回溯法
def hasPathInMatrix(matrix, test_str):
    row_len = len(matrix)
    col_len = len(matrix[0])
    visited = [[False] * col_len for _ in range(row_len)]

    def helper(row, col, pos):
        if pos == len(test_str):
            return True
        if row >= 0 and row <= row_len - 1 and col >= 0 and col <= col_len - 1 and not visited[row][col]:
            visited[row][col] = True
            return helper(row - 1, col, pos + 1) or \
                helper(row + 1, col, pos + 1) or \
                helper(row, col - 1, pos + 1) or \
                helper(row, col + 1, pos + 1)
    for row in range(row_len):
        for col in range(col_len):
            if helper(row, col, 0):
                return True
    return False

matrix = [
    ['a', 'b', 't', 'g'],
    ['c', 'f', 'c', 's'],
    ['j', 'd', 'e', 'h'],
]

test_str = 'abc'

print(hasPathInMatrix(matrix, test_str))

