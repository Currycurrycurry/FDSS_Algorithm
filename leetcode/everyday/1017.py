    def solveNQueens(self, n: int) -> List[List[str]]:
        def generateBoard():
            board = list()
            for i in range(n):
                row[queens[i]] = "Q"
                board.append("".join(row))
                row[queens[i]] = "."
            return board

        def backtrack(row: int):
            if row == n:
                board = generateBoard()
                solutions.append(board)
            else:
                for i in range(n):
                    if i in columns or row - i in diagonal1 or row + i in diagonal2:
                        continue
                    queens[row] = i
                    columns.add(i)
                    diagonal1.add(row - i)
                    diagonal2.add(row + i)
                    backtrack(row + 1)
                    columns.remove(i)
                    diagonal1.remove(row - i)
                    diagonal2.remove(row + i)
                    
        solutions = list()
        queens = [-1] * n
        columns = set()
        diagonal1 = set()
        diagonal2 = set()
        row = ["."] * n
        backtrack(0)
        return solutions

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        solutions, columns, digs1, digs2 = [], set(), set(), set()
        queens = [-1 for _ in range(n)] 
        def generateBoard():
            board = []
            for i in range(len(queens)):
                row = ['.' for i in range(n)]
                row[queens[i]] = 'Q'
                board.append(''.join(row))
            return board
        def dfs(row):
            if row == n:
                board = generateBoard()
                solutions.append(board)
                return
            for i in range(n):
                if i in columns or i + row in digs1 or row - i in digs2:
                    continue
                queens[row] = i
                columns.add(i)
                digs1.add(i+row)
                digs2.add(row-i)
                dfs(row+1)
                columns.remove(i)
                digs1.remove(i+row)
                digs2.remove(row-i)
        dfs(0)
        return solutions

class Solution:
    def totalNQueens(self, n: int) -> int:
        count = 0
        def dfs(row, column, dig1, dig2):
            nonlocal count
            if row == n:
                count += 1
                return
            aPs = ((1<<n) - 1) & (~(column | dig1 | dig2))
            while aPs:
                position = aPs & (-aPs)
                aPs = aPs & (aPs - 1)
                dfs(row+1, column | position, (dig1 | position) << 1, (dig2 | position) >>1)
        dfs(0, 0, 0, 0)
        return count