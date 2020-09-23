# 2
# 20212226543 黄佳妮
########### input processing ############
# N, M = list(map(int, input().split(' ')))
# expressions = []
# for _ in range(M):
#     board.append(input())

########### core algorithm ############
# 拓扑排序
# Sort
circle = False
from collections import defaultdict
class Graph:
    def __init__(self, V):
        self.graph = defaultdict(list)
        self.V = V
  
    def addEdge(self, u, v):
        self.graph[u].append(v)

    def topoSortRecursively(self, i, visited, stack):
        visited[i] = True
        global circle
        if circle:
            return
        for j in self.graph[i]:
            if visited[j] == False:
                self.topoSortRecursively(j, visited, stack)
            else:
                circle = True
                # print('信息包含冲突')
                # return 
        visited[i] = False
        stack.insert(0,i) 

    def topoSort(self):
        visited = [False] * self.V
        stack = []
        for i in range(self.V):
            if visited[i] == False:
                self.topoSortRecursively(i, visited, stack)
        return stack

def judgeRanking(N, M, expressions):
    if not N or not M or not expressions or len(expressions) != M:
        print('input error')
        return
    if N - M >= 2:
        print('信息不完全')
        return
    g = Graph(N)
    equals = []
    for expression in expressions:
        if '=' in expression:
            pivot = expression.index('=')
            equals.append((int(expression[:pivot]), int(expression[pivot+1:])))
        elif '<' in expression:
            pivot = expression.index('<')
            small_value, big_value = int(expression[:pivot]), int(expression[pivot+1:])
            g.addEdge(small_value, big_value)
        elif '>' in expression:
            pivot = expression.index('>')
            big_value, small_value = int(expression[:pivot]), int(expression[pivot+1:])
            g.addEdge(small_value, big_value)
    print(g.graph)
    order = g.topoSort()
    if order:
        print(order)
        if circle:
            print('信息包含冲突')
            return
        for i in range(len(order)-1):
            if order[i+1] not in g.graph[order[i]]:
                print('信息不完全')
                return
        # equals
        for equal in equals:
            if abs(order.index(equal[0]) - order.index(equal[1])) >= 2:
                print('信息包含冲突')
                return
            if equal[1] in g.graph[equal[0]] or euqal[0] in g.graph[euqal[1]]:
                print('信息包含冲突')
                return
        print('能确定')
    
########### test case 1 ############
expressions = [
    '1>2',
    '2>0',
    '0>1'
]
judgeRanking(3, 3, expressions)
# ########### test case 2 ############
# expressions = [
#     '1>0',
#     '1>2'
# ]
# judgeRanking(3, 2, expressions)
# ########### test case 3 ############
# expressions = [
#     '0>1',
#     '1<2',
#     '0>2',
# ]
# judgeRanking(3, 3, expressions)
