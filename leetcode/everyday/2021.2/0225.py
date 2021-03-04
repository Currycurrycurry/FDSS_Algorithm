class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        row_len = len(matrix)
        col_len = len(matrix[0])
        res = []
        for i in range(col_len):
            tmp = []
            for j in range(row_len):
                tmp.append(matrix[j][i])
            res.append(tmp)
        return res

        