class Node:
    def __init__(self):
        self.children = []
        self.in_degree = 0
        self.visited = False
        self.count = 0
N = 3
M = 3
expressions = [
    '2<1',
    '0<2',
    '1<0'
]
nodes = [Node()] * M
fathers = [i for i in range(N)]
reach_node = 0
has_circle = False
flag = False
def find(num):
    if fathers[num] == num:
        return num
    else:
        fathers[num] = find(fathers[num])
        return fathers[num]

def union(num1, num2):
    father1 = find(num1)
    father2 = find(num2)
    if father1 != father2:
        fathers[num1] = father2

for expression in expressions:
    if '<' in expression:
        pivot = expression.index('<')
        small_num, big_num = int(expression[:pivot]), int(expression[pivot+1:])
        nodes[small_num].chilren.append(nodes[big_num])
        nodes[small_num].in_degree += 1
    elif '>' in expression:
        pivot = expression.index('>')
        big_num, small_num = int(expression[:pivot]), int(expression[pivot+1:])
        nodes[small_num].chilren.append(nodes[big_num])
        nodes[small_num].in_degree += 1
    elif '=' in expression:
        pivot = expression.index('=')
        num1, num2 = int(expression[:pivot]), int(expression[pivot+1:])
        union(num1, num2)

for i in range(N):
    fa = find(i)
    nodes[fa].count += 1
    nodes[i] = nodes[fa]

root = None
for node in nodes:
    if node.in_degree == 0:
        root = node
        break
if not root:
    print('conflict')

def dfs(node):
    node.visited = True
    global reach_node
    reach_node += node.count
    if reach_node == N:

    
