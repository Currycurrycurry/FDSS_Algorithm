# one root N children 单层树 普通合并
class Basic_DSU:
    def __init__(self, N):
        self.root = [i for i in range(N)]
    
    def find(self, i):
        return self.root[i]
    
    def union(self, i, j):
        parent_i = self.find(i)
        self.root[j] = parent_i

# + 快速合并 存parent节点 多级树 
class Parent_DSU:
    def __init__(self, N):
        self.root = [0] * N
    
    def find(self, i):
        if self.root[i] != i:
            return self.find(self.root[i])
        else:
            return i
    
    def union(self, i, j):
        parent_i = self.find(i)
        parent_j = self.find(j)
        self.root[parent_j] = parent_i
    
# + 按秩合并
class Rank_DSU:
    def __init__(self, N):
        self.root = [0] * N
        self.rank = [1] * N
        self.size = N
    
    def find(self, i):
        if self.root[i] != i:
            return self.find(self.root[i])
        else:
            return i
    
    def union(self, i, j):
        parent_i = self.find(i)
        parent_j = self.find(j)

        if rank[parent_i] >= rank[parent_j]:
            self.root[parent_j] = parent_i
            self.rank[parent_i] += 1
        else:
            self.root[parent_i] = parent_j
            self.rank[parent_j] += 1
        self.size -= 1

# + 路径压缩
class Rank_DSU:
    def __init__(self, N):
        self.root = [0] * N
        self.rank = [1] * N
        self.size = N
    
    def find(self, i):
        if self.root[i] != i:
            self.root[i] = self.find(self.root[i])
            return self.root[i]
        else:
            return i
    
    def union(self, i, j):
        parent_i = self.find(i)
        parent_j = self.find(j)

        if rank[parent_i] >= rank[parent_j]:
            self.root[parent_j] = parent_i
            self.rank[parent_i] += 1
        else:
            self.root[parent_i] = parent_j
            self.rank[parent_j] += 1
        self.size -= 1

 # 朋友圈
 class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        if not M or len(M) == 0:
            return 0
        res = 0
        friends = [i for i in range(len(M))]
        rank = [0] * len(M)
        size = len(M)

        def find(i):
            if friends[i] != i:
                friends[i] = find(friends[i])
                return friends[i]
            else:
                return i

        def union(i, j):
            nonlocal size 
            nonlocal rank
            parent_i = find(i)
            parent_j = find(j)
            if parent_i == parent_j:
                return 
            if rank[parent_i] >= rank[parent_j]:
                friends[parent_j] = parent_i
                rank[parent_i] += rank[parent_j]
            else:
                friends[parent_i] = parent_j
                rank[parent_j] += rank[parent_i] 
            
            size -= 1

        for i in range(len(M)):
            for j in range(i, len(M)):
                if M[i][j] == 1:
                    union(i, j)
        return size




        


        



    



    


