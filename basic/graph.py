# 【最短路径问题】题型整理
# Sort
from collections import defaultdict

class Graph:
  def __init__(self, V):
    self.graph = defaultdict(list)
    self.V = V
  
  def addEdge(self, u, v):
    self.graph[u].append(v)

  def topoSortRecursively(self, i, visited, stack):
    visited[i] = True
    for j in self.graph[i]:
      if visited[j] == False:
        self.topoSortRecursively(j, visited, stack)
    stack.insert(0,i) 

  def topoSort(self):
    visited = [False] * self.V
    stack = []

    for i in range(self.V):
      if visited[i] == False:
        self.topoSortRecursively(i, visited, stack)

    print(stack)

g= Graph(6) 
g.addEdge(5, 2) 
g.addEdge(5, 0) 
g.addEdge(4, 0) 
g.addEdge(4, 1) 
g.addEdge(2, 3) 
g.addEdge(3, 1)

g.topoSort()

# 找到一条从start到end的路径
def findPath(graph,start,end,path=[]):   
    path = path + [start]
    if start == end:
        return path 
    for node in graph[start]:
        if node not in path:
            return findPath(graph,node,end,path)
    return 'no path!'

# 找到所有从start到end的路径
def findAllPath(graph,start,end,path=[]):
    path = path +[start]
    if start == end:
        return [path]
 
    paths = [] #存储所有路径    
    for node in graph[start]:
        if node not in path:
            newpaths = findAllPath(graph,node,end,path)
            # print('temp newpaths:{}'.format(newpaths))
            for newpath in newpaths:
                paths.append(newpath)
            # print('temp paths: {}'.format(paths))
    return paths

# 查找最短路径
def findShortestPath(graph,start,end,path=[]):
    path = path +[start]
    if start == end:
        return path
    
    shortestPath = []
    for node in graph[start]:
        if node not in path:
            newpath = findShortestPath(graph,node,end,path)
            if newpath:
                if not shortestPath or len(newpath)<len(shortestPath):
                    shortestPath = newpath
    return shortestPath


graph = [
    [1, 2],
    [2, 3],
    [3, 4],
    [4],
    []
]

print('dfs:')
for i in range(5):
    for j in range(5):
        print('find one path from {i} to {j}: {ans}'.format(i=i, j=j, ans=findPath(graph, i, j)))
        print('find all paths from {i} to {j}: {ans}'.format(i=i, j=j, ans=findAllPath(graph, i, j)))
        print('find shortest path from {i} to {j}: {ans}'.format(i=i, j=j, ans=findShortestPath(graph, i, j)))


def __dfs(self, candidates, begin, size, path, res, target):
    # 先写递归终止的情况
    if target == 0:
        # Python 中可变对象是引用传递，因此需要将当前 path 里的值拷贝出来
        # 或者使用 path.copy()
        res.append(path[:])

    for index in range(begin, size):
        residue = target - candidates[index]
        # “剪枝”操作，不必递归到下一层，并且后面的分支也不必执行
        if residue < 0:
            break
        path.append(candidates[index])
        # 因为下一层不能比上一层还小，起始索引还从 index 开始
        self.__dfs(candidates, index, size, path, res, residue)
        path.pop()

class UnionFind(object):
    '''union find set'''
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n
        self.size = n
    
    def find(self, p):
        if self.parent[p] != p:
            self.parent[p] = self.find(self.parent[p])
        return self.parent[p]

    def union(self, p, q):
        p_root = self.find(p)
        q_root = self.find(q)
        if p_root == q_root:
            return
        if self.rank[p_root] < self.rank[q_root]:
            p_root, q_root = q_root, p_root
        self.parent[q_root] = p_root
        self.rank[p] += self.rank[q]

    def is_connected(self, p, q):
        return self.find(p) == self.find(q)


class GraphTree(object):
    def __init__(self, maps):
        self.maps = maps
        self.nodenum = self.get_nodenum()
        self.edgenum = self.get_edgenum()
 
    def get_nodenum(self):
        return len(self.maps)
 
    def get_edgenum(self):
        count = 0
        for i in range(self.nodenum):
            for j in range(i):
                if self.maps[i][j] > 0 and self.maps[i][j] < 9999:
                    count += 1
        return count
 
    def kruskal(self):
        res = []
        if self.nodenum <= 0 or self.edgenum < self.nodenum-1:
            return res
        edge_list = []
        for i in range(self.nodenum):
            for j in range(i,self.nodenum):
                if self.maps[i][j] < 9999:
                    edge_list.append([i, j, self.maps[i][j]])#按[begin, end, weight]形式加入
        edge_list.sort(key=lambda a:a[2])#已经排好序的边集合
        
        group = [[i] for i in range(self.nodenum)]
        for edge in edge_list:
            for i in range(len(group)):
                if edge[0] in group[i]:
                    m = i
                if edge[1] in group[i]:
                    n = i
            if m != n:
                res.append(edge)
                group[m] = group[m] + group[n]
                group[n] = []
        return res
 
    def prim(self):
        res = []
        if self.nodenum <= 0 or self.edgenum < self.nodenum-1:
            return res
        res = []
        seleted_node = [0]
        candidate_node = [i for i in range(1, self.nodenum)]
        
        while len(candidate_node) > 0:
            begin, end, minweight = 0, 0, 9999
            for i in seleted_node:
                for j in candidate_node:
                    if self.maps[i][j] < minweight:
                        minweight = self.maps[i][j]
                        begin = i
                        end = j
            res.append([begin, end, minweight])
            seleted_node.append(end)
            candidate_node.remove(end)
        return res
 
max_value = 9999
row0 = [0,7,max_value,max_value,max_value,5]
row1 = [7,0,9,max_value,3,max_value]
row2 = [max_value,9,0,6,max_value,max_value]
row3 = [max_value,max_value,6,0,8,10]
row4 = [max_value,3,max_value,8,0,4]
row5 = [5,max_value,max_value,10,4,0]
maps = [row0, row1, row2,row3, row4, row5]
graph = GraphTree(maps)
print('邻接矩阵为\n%s'%graph.maps)
print('节点数据为%d，边数为%d\n'%(graph.nodenum, graph.edgenum))
print('------最小生成树kruskal算法------')
print(graph.kruskal())
print('------最小生成树prim算法')
print(graph.prim())


