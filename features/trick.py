class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        row_len = len(grid)
        if row_len == 0:
            return 0
        col_len = len(grid[0])
        if col_len == 0:
            return 0
        res = 0
        for i in range(row_len):
            for j in range(col_len):
                if grid[i][j] == 1:
                    res += 4
                    if i > 0 and grid[i-1][j] == 1:
                        res -= 2
                    if j > 0 and grid[i][j-1] == 1:
                        res -= 2
        return res
