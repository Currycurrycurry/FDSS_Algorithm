class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m = len(heights)
        n = len(heights[0])
        parent = list(range(m*n))
        edges =[]
        def find(index):
            if parent[index]!=index:
                parent[index] = find(parent[index])
            return parent[index]
        def union(index1, index2):
            u = find(index1)
            v = find(index2)
            parent[u] = v
            
        def is_valid(x,y):
            # 判断 节点是否合理
            return 0<=x<m and 0<=y<n

        # 构建 edges 列表
        # edge 为三元组[x,y,d] ，其中d为 x与y 差的绝对值
        for i in range(m):
            for j in range(n):
                nx = i+1
                ny = j
                if is_valid(nx,ny):
                    d = abs(heights[i][j]-heights[nx][ny])
                    edges.append([i*n+j,nx*n+ny,d])
                nx= i
                ny = j+1
                if is_valid(nx,ny):
                    d = abs(heights[i][j] - heights[nx][ny])
                    edges.append([i*n+j,nx*n+ny,d])
        # 将 边 根据绝对差值 d 进行从小到大排序
        edges = sorted(edges, key=lambda x:x[-1])

        # 依次遍历 edges 并依次连通所遍历的节点，当左上与左下连通时，结束，输出所遍历过的最大 d
        cost = 0
        for edge in edges:
            if find(0)==find(m*n-1):
                break
            x,y,d = edge
            if find(x)!=find(y):
                union(x,y)
                cost=max(cost,d)
        return cost