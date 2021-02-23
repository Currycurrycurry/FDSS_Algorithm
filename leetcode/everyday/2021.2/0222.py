# 自己写的暴力解法
class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        start_points = [(0, i) for i in range(n)] + [(i, 0) for i in range(m)]
        for x, y in start_points:
            val = matrix[x][y]
            x += 1
            y += 1
            while x < m and y < n:
                if matrix[x][y] != val:
                    return False
                x += 1
                y += 1
        return True

