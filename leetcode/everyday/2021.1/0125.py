class UnionFind:
    def __init__(self, n):
        self.n = n
        self.parents = [i for i in range(n)]
        self.rank = [1 for _ in range(n)]
    
    def get_parent(self, i):
        if i == self.parents[i]:
            return i
        else:
            return get_parent(self.parents[i])
    
    def is_connected(self, i, j):
        parent_i, parent_j = self.parents[i], self.parents[j]
        return parent_i == parent_j
    
    def merge(self, i, j):
        parent_i, parent_j = self.parents[i], self.parents[j]
        if not self.is_connected(i, j):
            if self.rank[parent_i] > self.rank[parent_j]:
                self.parents[parent_j] = parent_i
                self.rank[parent_i] += self.rank[parent_j]
            else:
                self.parents[parent_i] = parent_j
                self.rank[parent_j] += self.rank[parent_i]
            self.n -= 1
    
        
class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        N = len(grid)
        length = 4 * N * N
        uf = UnionFind(length)
        for i in range(N):
            row = grid[i]
            row_len = len(row)
            j = 0
            while j < row_len:
                char = row[j]
                index = 4 * (N * i + j)
                                
                if j + 1 < N:
                    uf.merge(index + 1, 4 * (N * i + j + 1) + 3)
                if i + 1 < N:
                    uf.merge(index + 2, 4 * (N * (i + 1) + j))

                if char == '/':
                    uf.merge(index, index + 3)
                    uf.merge(index + 1, index + 2)
                    j += 1
                elif char == '\\':
                    uf.merge(index, index + 1)
                    uf.merge(index + 2, index + 3)
                    j += 1
                else:
                    uf.merge(index, index + 1)
                    uf.merge(index + 1, index + 2)
                    uf.merge(index + 2, index + 3)
                    j += 1
        return uf.n