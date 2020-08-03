# 拓扑排序
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

# 给定一个 2 维矩阵，矩阵里的每个元素是 0 或者 1，找出该矩阵中的最大正方子矩阵
# (即行数和列数相同)，使得该正方子矩阵中的元素都是 1，并输出该正方子矩阵的行数。

# 10100 10111 11111 10010

test_matrix = [[1, 0, 1, 0, 0],
                [1, 0, 1, 1, 1],
                [1, 1, 1, 1, 1],
                [1, 0, 0, 1, 0]]
# brute force
def isAll1(matrix, row, col, length):
    for i in range(row):
        for j in range(col):
            if matrix[i][j] == 0:
                return False
    return True

def findMaxSubSquareMatrix(matrix):
    ans = min(len(matrix), len(matrix[0]))
    for i in range(ans, 0, -1):
        for row in range(i, len(matrix)+1, i):
            for col in range(i, len(matrix[0])+1, i):
                if isAll1(matrix, row, col, i):
                    return i
    return 0

print(findMaxSubSquareMatrix(test_matrix))

WHITE = 0
BLACK = 1

class Node:
    def __init__(self, val):
        self.color = WHITE
        self.children = []
        self.parent = None
        self.val = val

# graph
n, m = map(input().split(' '), int)
nodes = [Node(i) for i in range(n)]
tree = [[[0] for i in range(n)] for j in range(n)]
parents = map(input().split(' '), int)
edges = map(input().split(' '), int)

for index in range(m):
    nodes[index+1].parent = nodes[parents[index]]
    nodes[parents[index]].children.append(nodes[index+1])
    tree[index+1][parents[index]] = edges[index]
    tree[parents[index]][index+1] = edges[index]

for i in range(m):
    op_kind, node_num = map(input().split(' '), int)
    if op_kind == 1:
        # color
        nodes[node_num].color = BLACK
    elif op_kind == 2:
        # query
        print(queryDistance(nodes[node_num]))


def queryDistance(node):
    # 到所有黑色节点的距离之和
    total = 0
    for n in nodes:
        if n.color == BLACK:
            total +=  calPath(node, n)
    return total

# bad
def findLowestCommonParent(start, end):
    parent1 = start
    parent2 = end
    while parent1:
        while parent2:
            if parent2 == parent1:
                return parent1
            else:
                parent2 = parent2.parent
        parent1 = parent1.parent
        parent2 = end

# good

def calPath(start, end):
    # 找到公共父节点
    lowest_parent = findLowestCommonParent(start, end)
    return calSum(lowest_parent, start) + calSum(lowest_parent, end)


def calSum(node1, node2):
    total = 0
    node1_root_distance, node2_root_distance = -1, -1
    tmp_1, tmp_2 = node1, node2
    while tmp_1:
        node1_root_distance += 1
        tmp_1 = tmp_1.parent
    while tmp_2:
        node2_root_distance += 1
        tmp_2 = tmp_2.parent
    # abs()
    



    






