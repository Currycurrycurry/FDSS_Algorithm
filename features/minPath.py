class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        row_len, col_len = len(grid), len(grid[0])
        for row in range(1, row_len):
            grid[row][0] += grid[row-1][0]
        for col in range(1, col_len):
            grid[0][col] += grid[0][col-1]
        for row in range(1, row_len):
            for col in range(1, col_len):
                grid[row][col] += min(grid[row-1][col], grid[row][col-1])
        return grid[-1][-1]