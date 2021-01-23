class UnionFind:
    def __init__(self, n):
        self.parents = [i for i in range(n)]
        self.ranks = [1 for i in range(n)]
        self.n = n
    
    def find_parent(self, i):
        if self.parents[i] == i:
            return i
        else:
            return self.find_parent(self.parents[i])
    
    def is_connected(self, i, j):
        return self.find_parent(i) == self.find_parent(j)
    
    def merge(self, i, j):
        parent_i, parent_j = self.find_parent(i), self.find_parent(j) 
        if parent_i > parent_j:
            self.ranks[parent_i] += self.ranks[parent_j]
            self.parents[parent_j] = parent_i
        else:
            self.ranks[parent_j] += self.ranks[parent_i]
            self.parents[parent_i] = parent_j
        self.n -= 1
    
class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        uf = UnionFind(n)
        cable_num = 0
        for connection in connections:
            if uf.is_connected(connection[0], connection[1]):
                cable_num += 1
            else:
                uf.merge(connection[0], connection[1])
        if uf.n <= cable_num + 1:
            return uf.n - 1
        else:
            return -1