# 1 upRight 
def search2Darray(matrix, num):
    row_len = len(matrix)
    col_len = len(matrix[0])
    row_index, col_index = 0, col_len - 1
    while row_index < row_len and col_index >= 0:
        if num == matrix[row_index][col_index]:
            return row_index, col_index
        elif num < matrix[row_index][col_index]:
            col_index -= 1
        else:
            row_index += 1
    return -1

# 2 bottomLeft
def search2Darray2(matrix, num):
    row_len = len(matrix)
    col_len = len(matrix[0])
    row_index, col_index = row_len - 1, 0
    while row_index >= 0 and col_index < col_len:
        if num == matrix[row_index][col_index]:
            return row_index, col_index
        elif num < matrix[row_index][col_index]:
            row_index -= 1
        else:
            col_index += 1
    return -1

matrix = [
    [0,1,2,3],
    [1,2,3,4],
    [2,3,4,5]
]

print(search2Darray(matrix, 7))
print(search2Darray2(matrix, 7))

print(search2Darray(matrix, 5))
print(search2Darray(matrix, 5))
