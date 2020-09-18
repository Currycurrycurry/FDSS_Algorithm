class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row_len, col_len = len(board), len(board[0])
        visited = [[False] * col_len for _ in range(row_len)]
        def helper(x, y, index):
            if index == len(word):
                return True
            res = False
            if 0 <= x < row_len and 0 <= y < col_len and not visited[x][y] and board[x][y] == word[index]:
                visited[x][y] = True
                index += 1
                res = helper(x+1, y, index) or helper(x-1, y, index) \
                or helper(x, y+1, index) or helper(x, y-1, index)
                if not res:
                    visited[x][y] = False
                    index -= 1
            return res

        for row in range(row_len):
            for col in range(col_len):
                if helper(row, col, 0):
                    return True
        return False