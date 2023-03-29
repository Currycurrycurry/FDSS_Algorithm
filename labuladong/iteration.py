class Solution:
    def trim_spaces(self, s: str) -> list:
        left, right = 0, len(s) - 1
        # 去掉字符串开头的空白字符
        while left <= right and s[left] == ' ':
            left += 1
        
        # 去掉字符串末尾的空白字符
        while left <= right and s[right] == ' ':
            right -= 1
        
        # 将字符串间多余的空白字符去除
        output = []
        while left <= right:
            if s[left] != ' ':
                output.append(s[left])
            elif output[-1] != ' ':
                output.append(s[left])
            left += 1
        
        return output
            
    def reverse(self, l: list, left: int, right: int) -> None:
        while left < right:
            l[left], l[right] = l[right], l[left]
            left, right = left + 1, right - 1
            
    def reverse_each_word(self, l: list) -> None:
        n = len(l)
        start = end = 0
        
        while start < n:
            # 循环至单词的末尾
            while end < n and l[end] != ' ':
                end += 1
            # 翻转单词
            self.reverse(l, start, end - 1)
            # 更新start，去找下一个单词
            start = end + 1
            end += 1
                
    def reverseWords(self, s: str) -> str:
        l = self.trim_spaces(s)
        
        # 翻转字符串
        self.reverse(l, 0, len(l) - 1)
        
        # 翻转每个单词
        self.reverse_each_word(l)
        
        return ''.join(l)


# 48. 旋转图像
def rotate(matrix) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    row_len = len(matrix)
    col_len = len(matrix[0])
    def rotate_diagonal():
        for i in range(row_len):
            for j in range(i, col_len):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    def reverse_array(array):
        left, right = 0, len(array) - 1
        while left < right:
            array[left], array[right] = array[right], array[left]
            left += 1
            right -= 1
            
    rotate_diagonal()
    for i in range(row_len):
        reverse_array(matrix[i])

# 54. 螺旋矩阵
# 老老实实遍历法
def spiralOrder(self, matrix):
    row_len = len(matrix)
    col_len = len(matrix[0])
    upper_bound = 0
    lower_bound = row_len - 1
    left_bound = 0
    right_bound = col_len - 1
    res = []
    while len(res) < row_len * col_len:
        # ->
        if upper_bound <= lower_bound:
            for j in range(left_bound, right_bound+1):
                res.append(matrix[upper_bound][j])
            upper_bound += 1
        # 往下
        if left_bound <= right_bound:
            for i in range(upper_bound, lower_bound+1):
                res.append(matrix[i][right_bound])
            right_bound -= 1
        # <-
        if upper_bound <= lower_bound:
            for j in range(right_bound, left_bound-1, -1):
                res.append(matrix[lower_bound][j])
            lower_bound -= 1
        # 往上
        if left_bound <= right_bound:
            for i in range(lower_bound, upper_bound-1, -1):
                res.append(matrix[i][left_bound])
            left_bound += 1
    return res 

# 59. 螺旋矩阵 II
def generateMatrix(n: int):
    left_bound, right_bound, top_bound, bottom_bound = 0, n - 1, 0, n - 1
    matrix = [[0 for _ in range(n)] for _ in range(n)]
    num = 1
    total = n * n
    while num <= total:
        for i in range(left_bound, right_bound + 1): # left to right
            matrix[top_bound][i] = num
            num += 1
        top_bound += 1
        for i in range(top_bound, bottom_bound + 1): # top to bottom
            matrix[i][right_bound] = num
            num += 1
        right_bound -= 1
        for i in range(right_bound, left_bound - 1, -1): # right to left
            matrix[bottom_bound][i] = num
            num += 1
        bottom_bound -= 1
        for i in range(bottom_bound, top_bound - 1, -1): # bottom to top
            matrix[i][left_bound] = num
            num += 1
        left_bound += 1
    return matrix




# 考虑到代码的可复用性和简洁性(可不看，面试官应该不会这么变态)
def spiralOrder(matrix):
    if not matrix or not matrix[0]:
        return list()
    
    rows, columns = len(matrix), len(matrix[0])
    visited = [[False] * columns for _ in range(rows)]
    total = rows * columns
    order = [0] * total

    directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    row, column = 0, 0
    directionIndex = 0
    for i in range(total):
        order[i] = matrix[row][column]
        visited[row][column] = True
        nextRow, nextColumn = row + directions[directionIndex][0], column + directions[directionIndex][1]
        if not (0 <= nextRow < rows and 0 <= nextColumn < columns and not visited[nextRow][nextColumn]):
            directionIndex = (directionIndex + 1) % 4
        row += directions[directionIndex][0]
        column += directions[directionIndex][1]
    return order