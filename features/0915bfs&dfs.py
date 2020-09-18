class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # helper method
        def dfs(i, j):
            if 0 <= i < row_len and 0<= j < col_len and board[i][j] == 'O':
                board[i][j] = '-'
                dfs(i-1, j)
                dfs(i+1, j)
                dfs(i, j+1)
                dfs(i, j-1)
        if not board:
            return
        row_len = len(board)
        if row_len == 0:
            return
        col_len = len(board[0])
        if col_len == 0:
            return
        # col
        for i in range(col_len):
            dfs(0, i)
            dfs(row_len-1, i)
        # row
        for j in range(1, row_len - 1):
            dfs(j, 0)
            dfs(j, col_len - 1)

        for i in range(row_len):
            for j in range(col_len):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == '-':
                    board[i][j] = 'O'

class Solution:
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

class Solution:
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
 
class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        row_len = len(grid)
        if row_len == 0:
            return 0
        col_len = len(grid[0])
        if col_len == 0:
            return 0
        res = 0
        connect_boundary_flag = False
        def helper(i, j):
            if (i == 0 or i == row_len - 1 or j == 0 or j == col_len - 1) and grid[i][j] == 0:
                nonlocal connect_boundary_flag
                connect_boundary_flag = True
            elif 0 < i < row_len and 0 < j < col_len and grid[i][j] == 0:
                grid[i][j] = 1
                helper(i-1, j)
                helper(i+1, j)
                helper(i, j+1)
                helper(i, j-1)
        for i in range(row_len):
            for j in range(col_len):
                if grid[i][j] == 0:
                    connect_boundary_flag = False
                    helper(i, j)
                    if not connect_boundary_flag:
                        res += 1
        return res 
      

class Solution:
    def pondSizes(self, land: List[List[int]]) -> List[int]:
        if not land:
            return 0
        row_len = len(land)
        if row_len == 0:
            return 0
        col_len = len(land[0])
        if col_len == 0:
            return 0
        res = []
        tmp_area = 0
        def helper(i, j):
            if 0 <= i < row_len and 0 <= j < col_len and land[i][j] == 0:
                land[i][j] = 1
                nonlocal tmp_area
                tmp_area += 1
                helper(i-1, j)
                helper(i+1, j)
                helper(i, j+1)
                helper(i, j-1)
                helper(i-1, j-1)
                helper(i+1, j+1)
                helper(i+1, j-1)
                helper(i-1, j+1)
        for i in range(row_len):
            for j in range(col_len):
                if land[i][j] == 0:
                    tmp_area = 0
                    helper(i, j)
                    res.append(tmp_area)
        return sorted(res)
