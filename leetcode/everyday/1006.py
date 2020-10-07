# 无向图
## 使用邻接矩阵表示
### 求每个节点到其他节点最短距离的二维矩阵

# https://leetcode-cn.com/problems/sum-of-distances-in-tree/solution/shu-zhong-ju-chi-zhi-he-by-leetcode-solution/
# 今天又是CV工程师呢
class Solution:
    def sumOfDistancesInTree(self, N: int, edges: List[List[int]]) -> List[int]:
        # visited = [[False for _ range(N)] for _ in range(N)]
        def helper(i, j, dists):
            if i == j:
                return 0      
            for index, dist in enumerate(dists[i]):
                if dist != 0:
                    # visited[i][index] = True
                    return 1 + helper(index, j, dists)
            return 0

        dists = [[999 for _ in range(N)] for _ in range(N)]
        for edge in edges:
            dists[edge[0]][edge[1]] = 1
        for i in range(N):
            for j in range(i+1, N-i):
                if dists[i][j] < 999:
                    # dfs
                    # visited = [[False for _ range(N)] for _ in range(N)]
                    dists[i][j] = helper(i, j, dists)
        print(dists)
                   


