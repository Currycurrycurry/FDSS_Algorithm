class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1, 1]]
        res = [[1], [1, 1]]
        for i in range(2, numRows):
            tmp = [1]
            for j in range(1, i//2+1):
                tmp.append(res[i-1][j-1] + res[i-1][j])
            if i % 2 == 0:
                # print(tmp[0:len(tmp)-1][::-1])
                tmp += tmp[0:len(tmp)-1][::-1]
            else:
                tmp += tmp[::-1]
            res.append(tmp)
        return res