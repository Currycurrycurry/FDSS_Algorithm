def numIslands(self, grid: List[List[str]]) -> int:    
    if not grid:
        return 0
    row_len = len(grid)
    if row_len == 0:
        return 0
    col_len = len(grid[0])
    if col_len == 0:
        return 0
    res = 0
    def helper(i, j):
        if 0 <= i < row_len and 0 <= j < col_len and grid[i][j] == '1':
            grid[i][j] = 0
            helper(i-1, j)
            helper(i+1, j)
            helper(i, j+1)
            helper(i, j-1)
    for i in range(row_len):
        for j in range(col_len):
            if grid[i][j] == '1':
                res += 1
                helper(i, j)
    return res


# 695. 岛屿的最大面积
def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
    if not grid:
        return 0
    row_len = len(grid)
    if row_len == 0:
        return 0
    col_len = len(grid[0])
    if col_len == 0:
        return 0
    max_area = 0
    tmp_area = 0
    def helper(i, j):
        if 0 <= i < row_len and 0 <= j < col_len and grid[i][j] == 1:
            nonlocal tmp_area
            tmp_area += 1
            grid[i][j] = 0
            helper(i-1, j)
            helper(i+1, j)
            helper(i, j+1)
            helper(i, j-1)
    for i in range(row_len):
        for j in range(col_len):
            if grid[i][j] == 1:
                tmp_area = 0
                helper(i, j)
                max_area = max(max_area, tmp_area)
    return max_area