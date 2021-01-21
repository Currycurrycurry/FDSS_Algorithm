class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.n = n
        self.rank = [1] * n
    
    def find_root(self, val):
        if val == self.parent[val]:
            return val
        else:
            return self.find_root(self.parent[val])
    
    def union(self, i, j):
        parent_i, parent_j = self.find_root(i), self.find_root(j)
        if parent_i != parent_j:
            if parent_i > parent_j:
                self.rank[parent_i] += self.rank[parent_j]
                self.parent[parent_j] = parent_i
            else:
                self.rank[parent_j] += self.rank[parent_i]
                self.parent[parent_i] = parent_j
            self.n -= 1
    
    def is_connected(self, i, j):
        parent_i, parent_j = self.find_root(i), self.find_root(j)
        return parent_i == parent_j


class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        # kruskal
        edge_len = len(edges)
        for i in range(edge_len):
            edges[i].append(i)
        edges = sorted(edges, key = lambda x:x[2])
        uf = UnionFind(n)
        mst_value = 0
        for edge in edges:
            if not uf.is_connected(edge[0], edge[1]):
                uf.union(edge[0], edge[1])
                mst_value += edge[2]
        # print(mst_value)
        # print(uf.n)
        # critical and non-critical
        ans = [[], []]
        for index in range(edge_len):
            # critical
            edge = edges[index]
            tmp_value = 0
            tmp_uf = UnionFind(n)
            for j in range(edge_len):
                m = edges[j]
                if index != j and not tmp_uf.is_connected(m[0], m[1]):
                    tmp_uf.union(m[0], m[1])
                    tmp_value += m[2]
            if (tmp_value > mst_value and tmp_uf.n == 1) or tmp_uf.n != 1:
                ans[0].append(edge[3])
                continue
            
            # non-critical
            tmp_uf = UnionFind(n)
            tmp_uf.union(edge[0], edge[1])
            tmp_value = edge[2]
            for j in range(edge_len):
                m = edges[j]
                if index != j and not tmp_uf.is_connected(m[0], m[1]):
                    tmp_uf.union(m[0], m[1])
                    tmp_value += m[2]
            if tmp_value == mst_value:
                ans[1].append(edge[3])
        return ans