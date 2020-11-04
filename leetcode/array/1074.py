import collections
class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]],
                              target: int) -> int:
        rows, cols = len(matrix), len(matrix[0])
        colsm = [[0] * cols for r in range(rows)]
        for c in range(cols):
            cur = 0
            for r in range(rows):
                cur += matrix[r][c]
                colsm[r][c] = cur
        res = 0
        for sr in range(rows):
            for er in range(sr, rows):
                d = collections.defaultdict(int)
                cur = 0
                for c in range(cols):
                    # 注意此处减去的是colsm[sr - 1][c], 因为要把起点行sr统计在内
                    pre = 0 if sr - 1 < 0 else colsm[sr - 1][c]
                    cur += colsm[er][c] - pre
                    if cur == target:
                        # cur本身就是target的特殊情况
                        res += 1
                    res += d[cur - target]
                    d[cur] += 1
        return res

class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        if not matrix or len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        row_len, col_len = len(matrix), len(matrix[0])
        sum_matrix = [[0 for _ in range(col_len+1)] for _ in range(row_len+1)]
        res = 0
        for i in range(row_len):
            t = 0
            for j in range(col_len):
                t += matrix[i][j]
                sum_matrix[i+1][j+1] = t + sum_matrix[i][j+1]
        for i in range(1, row_len+1):
            for j in range(1, col_len+1):
                for x in range(1, i+1):
                    for y in range(1, j+1):
                        v = sum_matrix[i][j] - sum_matrix[x-1][j] - sum_matrix[i][y-1] + sum_matrix[x-1][y-1]
                        if v == target:
                            res += 1
        return res